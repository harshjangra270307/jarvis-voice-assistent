import json
from cryptography.fernet import Fernet
import os

class ProfileManager:
    def __init__(self, config, path="encrypted_profile.json"):
        self.path = path
        self.fernet = Fernet(config["encryption_key"].encode())
        if not os.path.exists(path):
            self.write_profile({"name": "", "email": ""})

    def load_profile(self):
        if not os.path.exists(self.path):
            return {}
        with open(self.path, "rb") as f:
            ct = f.read()
        try:
            pt = self.fernet.decrypt(ct).decode()
            return json.loads(pt)
        except Exception:
            return {}

    def write_profile(self, data):
        pt = json.dumps(data).encode()
        ct = self.fernet.encrypt(pt)
        with open(self.path, "wb") as f:
            f.write(ct)

    def set_field(self, key, value):
        data = self.load_profile()
        data[key] = value
        self.write_profile(data)

    def get_field(self, key):
        return self.load_profile().get(key, "")
