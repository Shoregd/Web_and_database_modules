# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

---ROUTE LAYOUT ---
* albums route
POST /albums
    title:string
    release_year:int
    artist_id:int
GET /albums
    returns list of album objects

GET /artists
    returns string of artist names.

POST /artists
    name: string
    genre: string



--- NOUNS ---

albums,title,release_year,artist_id,artists,name,genre


--- TABLE LAYOUT ---

RECORD | PROPERTIES

albums | id, title, release_year, artist_id

artists | id, name, genre


--- DATA TYPES ---

albums:
    * id: SERIAL
    * title: text
    * release_year: int
    * artist_id: int

artists:
    * id:SERIAL
    * name: text
    * genre: text

Seed data can be located in music_web_app.sql
Test data can be located in music_web_app_test.sql

--- CLASS BREAKDOWN ---

Album - Model Class
    * __init__: id,title,release_year,artist_id as input params and stored in self variables.
    * __repr__: 'Album(id, title, release_year, artist_id)'
    * __eq__: Allows for testing.

Artist - Model Class
    *__init__: id,name,genre as input params and stored in self
    *__repr__: 'Artist(id, name, genre)
    *__eq__: Allow for testing

AlbumRepository - Repository Class
    * __init__: initialises database connection.
    * list_albums(): Will return a list of albums from the database. Takes no input. Returns a list of Album objects. No side effects.
                     executes 'SELECT * FROM albums'
    * add_album() Will add an album to the database with the given parameters. Inputs: albumtitle:string,releaseyear:int,artistid:int. Returns nothing. Side effect: Adds an album to the
                  database.
                  executes 'INSERT INTO albums (title,release_year,artist_id) VALUES(%s,%s,%s)',[albumtitle,releaseyear,artistid]

ArtistRepository - Repository Class
    *__init__: initialises database connection
    *list_artist_name(): Will return a string of the artist names i.e 'Pixies,ABBA,
                         etc.' takes no inputs. No side effects.
                         executes 'SELECT artists.name from artists'
    *add_artist(): Will accept inputs for artistname:string artistgenre:string. Returns nothing. Side effects adds an artist to the database with the given parameters. i.e Posting name='wild nothing' genre='indie' would return 
        'Pixies, ABBA, Taylor Swift, Nina Simone, wild nothing' when the GET request is made. 
        execute 'INSERT INTO artists (name,genre) VALUES(%s,%s)',[artistname,artistgenre]

