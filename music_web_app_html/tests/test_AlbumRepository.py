from lib.AlbumRepository import AlbumRepository
from lib.Album import Album

'''
Test that repository can return a list of the current albums reprs when given the list_albums() call.
'''

def test_list_albums_returns_correct_list(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = AlbumRepository(db_connection)
    result = repository.list_albums()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

'''
Test that an album can be added. Nothing is returned, but, the list is updated.
'''

def test_album_added_successfully_to_database(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = AlbumRepository(db_connection)
    assert repository.add_album('Voyage',2022,2) == Album(13, 'Voyage', 2022, 2)
    result = repository.list_albums()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Voyage', 2022, 2)
    ]
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = AlbumRepository(db_connection)

'''
Test that the system can return a single album object and the associated artist name
'''

def test_get_album_info_returns_album_object_and_artist_name(db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    repository = AlbumRepository(db_connection)
    assert repository.get_album_info(1) == (Album(1, 'Doolittle', 1989, 1),'Pixies')
    