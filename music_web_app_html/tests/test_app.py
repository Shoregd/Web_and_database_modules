from playwright.sync_api import Page, expect
from lib.Album import Album

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

'''
We can get the title and release year for each album with the GET command.
'''

def test_get_albums(page,test_web_address):
    page.goto(f'http://{test_web_address}/albums')
    albums = [
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
    #test_location = []
    #for loadalbums in range(1,len(albums)+1):
    #    print('albums '+str(loadalbums))
    #    test_location.append(page.locator('albums '+str(loadalbums)))
    test_location = []
    for locators in range(0,len(albums)):
        test_location.append(page.locator('.album_'+str(locators+1)))
    
        expect(test_location[locators]).to_have_text(f'Title: {albums[locators].title}\nReleased: {albums[locators].release_year}')
    

def test_get_album_info(page,test_web_address):
    page.goto(f'http://{test_web_address}/albums/1')
    test_location = page.locator('h1')
    expect(test_location).to_have_text('Doolittle')
    test_location = page.locator('p')
    expect(test_location).to_have_text('Release year: 1989\nArtist: Pixies')
    

def test_link_can_be_accessed(page,test_web_address,db_connection):
    db_connection.seed('seeds/music_web_app_test.sql')
    page.goto(f'http://{test_web_address}/albums')
    print(test_web_address)
    page.click("text=Title: Doolittle")
    
   
    test_location = page.locator('h1')
    expect(test_location).to_have_text('Doolittle')
    test_location = page.locator('p')
    expect(test_location).to_have_text('Release year: 1989\nArtist: Pixies')
  

    
