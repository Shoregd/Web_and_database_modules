from lib.Album import Album
'''
POST /albums
'''

'''
When: I make a POST request to /albums
And: I send a title, release_year and artist_id
Then: I should get a 200 response with no content
'''

def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title':'Voyage','release_year':2022,'artist_id':2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

'''
When: I make a GET request to /albums
Then: I get a list of album objects.
'''
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    result = response.data.decode('utf-8')
    print(result)
    assert result == ''\
    +'["Album(1, Doolittle, 1989, 1)","Album(2, Surfer Rosa, 1988, 1)","Album(3, Waterloo, 1974, 2)","Album(4, Super Trouper, 1980, 2)","Album(5, Bossanova, 1990, 1)","Album(6, Lover, 2019, 3)","Album(7, Folklore, 2020, 3)","Album(8, I Put a Spell on You, 1965, 4)","Album(9, Baltimore, 1978, 4)","Album(10, Here Comes the Sun, 1971, 4)","Album(11, Fodder on My Wings, 1982, 4)","Album(12, Ring Ring, 1973, 2)","Album(13, Voyage, 2022, 2)"]'\
    +'\n'

'''
When: I make a GET request to /artists
Then: I get a string with a list of artist names.
'''

def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

'''
When: I make a POST request to /artists
And: I supply the artist name and genre.
Then: I get a 200 ok response and the GET function returns the added artists
'''

def test_add_artist(web_client):
    post_response = web_client.post('/artists', data={'name':'Wild nothing','genre':'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ''
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'
