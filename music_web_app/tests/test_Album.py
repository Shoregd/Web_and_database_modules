from lib.Album import Album

def test_init_of_class_is_correct():
    test_album = Album(1,'Test Title',1337,1)
    assert test_album.id == 1
    assert test_album.title == 'Test Title'
    assert test_album.release_year == 1337
    assert test_album.artist_id == 1
    
def test_class_formats_correctly():
    test_album = Album(1,'Test Title',1337,1)
    assert str(test_album) == 'Album(1, Test Title, 1337, 1)'

def test_class_can_be_tested_against_other_class():
    test_album = Album(1,'Test Title',1337,1)
    assert test_album == Album(1,'Test Title',1337,1)