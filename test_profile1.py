from profile1 import ProfileManager
import tempfile
import os

def test_profile_manager():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    try:
        config = {"encryption_key": "a" * 44}  # Replace with a valid Fernet key of 44 chars.
        p = ProfileManager(config, tmp.name)
        p.set_field("test", "value")
        assert p.get_field("test") == "value"
    finally:
        os.unlink(tmp.name)
