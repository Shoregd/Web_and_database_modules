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

def test_isvalid_for_album():
    assert Album(1,None,None,None).isvalid() == False
    assert Album(1,'',None,None).isvalid() == False
    assert Album(1,'','',None).isvalid() == False
    assert Album(1,'',None,'').isvalid() == False
    assert Album(1,'Test','','').isvalid() == False
    assert Album(1,'',2022,'').isvalid() == False
    assert Album(1,'','',1).isvalid() == False
    assert Album(1,'',2022,1).isvalid() == False
    assert Album(1,'Test','',1).isvalid() == False
    assert Album(1,'Test',2022,1).isvalid() == True
    assert Album(None,'Test',2022,1).isvalid() == True

def test_generate_errors():
    assert Album(1,None,None,None).generate_errors() == ''\
    +"Title can't be blank, \n"\
    +"Release year can't be blank, \n"\
    +"Artist id can't be blank"
    assert Album(1,'Test',None,None).generate_errors() == ""\
        +"Release year can't be blank, \n"\
    +"Artist id can't be blank"
    assert Album(1,'Test',2022,None).generate_errors() == "Artist id can't be blank"
    assert Album(1,'Test',2022,1).generate_errors() == None