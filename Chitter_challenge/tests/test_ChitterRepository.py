from lib.ChitterRepository import ChitterRepository
from lib.User import User


def test_can_add_valid_user(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    result = repository.add_user('Twizzle','terryswizzle@gmail.com')
    assert result == 'User Twizzle has been added.'

def test_list_users_returns_userlist(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    result = repository.list_users()
    assert result == [User(1,'Twizzle','terryswizzle@gmail.com')]


def test_invalid_user_not_added_to_database(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    result = repository.list_users()
    assert result == [User(1,'Twizzle','terryswizzle@gmail.com')]

def test_invalid_user_input_generates_correct_error_message(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    assert repository.add_user('Twizzle','terryswizzles@gmail.com') == 'Username has been taken. Please try another.'
    assert repository.add_user('Twizzles','terryswizzle@gmail.com') == 'Email has been taken. Please try another.'
    assert repository.add_user('Twizzle','terryswizzle@gmail.com') == 'Username and Email has been taken. Please try another.'

def test_sign_in_returns_true_for_valid_user(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    result,username = repository.sign_in('Twizzle','terryswizzle@gmail.com')

    assert result == True
    assert username == 'Twizzle'

def test_sign_in_returns_false_for_incorrect_user(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    result,username = repository.sign_in('Twizzles','terryswizzle@gmail.com')
    assert result == False
    assert username == None

def test_sign_out_returns_correctly(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    result,username = repository.sign_out()
    assert result == False
    assert username == None

def test_user_can_add_peep_and_list_them(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    repository.add_peep('Test Message', 1)
    repository.add_peep('Test Message', 1)
    repository.add_peep('Test Message', 1)
    result = repository.list_peeps()
    assert result[0].message == 'Test Message'
    assert result[0].user_id == 'Twizzle'

def test_get_user_id_returns_correct_id(db_connection):
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzle@gmail.com')
    repository.add_user('Twizzles','terryswizzles@gmail.com')
    repository.add_user('Twizzl','terrywizzle@gmail.com')
    assert repository.get_user_id('Twizzles') == 2
    db_connection.seed('seeds/chitter_test.sql')
    repository = ChitterRepository(db_connection)
    repository.add_user('Twizzle','terryswizzles@gmail.com')
