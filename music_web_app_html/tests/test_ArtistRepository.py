from lib.ArtistRepository import ArtistRepository
from lib.Artist import Artist
def test_repo_returns_name_list_when_function_called(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
    result = repository.list_artists()

    assert result == [
        Artist(1,'Pixies','Rock'),
        Artist(2,'ABBA','Pop'),
        Artist(3,'Taylor Swift','Pop'),
        Artist(4,'Nina Simone','Jazz')
    ]

def test_can_add_artist_and_list_updates(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
    repository.add_artist('Wild nothing','Indie')
    assert repository.list_artists() == [
        Artist(1,'Pixies','Rock'),
        Artist(2,'ABBA','Pop'),
        Artist(3,'Taylor Swift','Pop'),
        Artist(4,'Nina Simone','Jazz'),
        Artist(5,'Wild nothing','Indie')
    ]
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = ArtistRepository(db_connection)
