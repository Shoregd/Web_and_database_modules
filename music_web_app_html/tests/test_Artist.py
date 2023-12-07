from lib.Artist import Artist

def test_init_of_class_is_correct():
    test_artist = Artist(1,'Test Artist','Test Genre')
    assert test_artist.id == 1
    assert test_artist.name == 'Test Artist'
    assert test_artist.genre == 'Test Genre'
   
    
def test_class_formats_correctly():
    test_artist = Artist(1,'Test Artist','Test Genre')
    assert str(test_artist) == 'Artist(1, Test Artist, Test Genre)'

def test_class_can_be_tested_against_other_class():
    test_artist = Artist(1,'Test Artist','Test Genre')
    assert test_artist == Artist(1,'Test Artist','Test Genre')