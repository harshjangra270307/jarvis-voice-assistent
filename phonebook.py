import json
import os

class PhoneBook:
    def __init__(self, path="phonebook.json"):
        self.path = path
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load(self):
        with open(self.path, encoding='utf-8') as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def add_contact(self, name, number):
        data = self.load()
        data.append({"name": name, "number": number})
        self.save(data)

    def get_contact(self, name):
        data = self.load()
        for c in data:
            if c["name"].lower() == name.lower():
                return c
        return None

    def update_contact(self, name, new_number):
        data = self.load()
        for c in data:
            if c["name"].lower() == name.lower():
                c["number"] = new_number
                self.save(data)
                return True
        return False

    def delete_contact(self, name):
        data = self.load()
        new_data = [c for c in data if c["name"].lower() != name.lower()]
        self.save(new_data)
