from phonebook import PhoneBook

def test_add_and_get_contact():
    pb = PhoneBook("test_phonebook.json")
    pb.add_contact("Test User", "5551234")
    assert pb.get_contact("Test User")['number'] == "5551234"

def test_update_contact():
    pb = PhoneBook("test_phonebook.json")
    pb.add_contact("Test Update", "1234")
    pb.update_contact("Test Update", "7777")
    assert pb.get_contact("Test Update")['number'] == "7777"

def test_delete_contact():
    pb = PhoneBook("test_phonebook.json")
    pb.add_contact("Delete Me", "0000")
    pb.delete_contact("Delete Me")
    assert pb.get_contact("Delete Me") is None
