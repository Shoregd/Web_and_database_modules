from lib.Peep import Peep

def test_class_setup_correct():
    test_user = Peep(1,'Test Message','2023-11-10','11:15:30',1)
    assert test_user.id == 1
    assert test_user.message == 'Test Message'
    assert test_user.post_date == '2023-11-10'
    assert test_user.post_time == '11:15:30'
    assert test_user.user_id == 1

def test_string_output_formats_correctly():
    test_user = Peep(1,'Test Message','2023-11-10','11:15:30',1)
    assert str(test_user) == "Peep(1, Test Message, 2023-11-10, 11:15:30, 1)"

def test_objects_can_be_tested_against_another_object():
    test_user = Peep(1,'Test Message','2023-11-10','11:15:30',1)
    test_user2 = Peep(1,'Test Message','2023-11-10','11:15:30',1)
    assert test_user == test_user2