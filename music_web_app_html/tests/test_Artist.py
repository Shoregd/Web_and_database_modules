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

def test_isvalid_function_returns_correctly():
    assert Artist(1,None,None).isvalid() == False
    assert Artist(1,'',None).isvalid() == False
    assert Artist(1,None,'').isvalid() == False
    assert Artist(1,'','').isvalid() == False
    assert Artist(1,'Test','').isvalid() == False
    assert Artist(1,'','Test').isvalid() == False
    assert Artist(1,'Test','Test').isvalid() == True
    assert Artist(None,'Test','Test').isvalid() == True

def test_generate_errors_returns_correctly():
    assert Artist(1,None,None).generate_errors() == ''\
            +"Name can't be blank,\n"\
            +"Genre can't be blank"
    assert Artist(1,'Test',None).generate_errors() == ''\
            +"Genre can't be blank"
    assert Artist(1,None,'Test').generate_errors() == ''\
            +"Name can't be blank"
    assert Artist(1,'Test','Test').generate_errors() == None
    assert Artist(None,'Test','Test').generate_errors() == None
    