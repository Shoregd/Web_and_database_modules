from lib.User import User

def test_class_setup_correct():
    test_user = User(1,'User Name','User Email')
    assert test_user.id == 1
    assert test_user.name == 'User Name'
    assert test_user.email == 'User Email'

def test_string_output_formats_correctly():
    test_user = User(1,'User Name','User Email')
    assert str(test_user) == "User(1, User Name, User Email)"

def test_objects_can_be_tested_against_another_object():
    test_user = User(1,'User Name','User Email')
    test_user2 = User(1,'User Name','User Email')
    assert test_user == test_user2