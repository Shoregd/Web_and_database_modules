from lib.ArtistRepository import ArtistRepository

def test_repo_returns_name_list_when_function_called(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
    result = repository.list_artist_names()

    assert result == 'Pixies, ABBA, Taylor Swift, Nina Simone'

def test_can_add_artist_and_list_updates(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
    repository.add_artist('Wild nothing','Indie')
    assert repository.list_artist_names() == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
