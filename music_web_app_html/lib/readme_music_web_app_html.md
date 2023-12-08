Test-drive a GET /albums route that connects with an AlbumRepository and the database to return a result like this:

<!-- GET /albums -->

<html>
  <head></head>
  <body>
    <h1>Albums</h1>

    <div>
      Title: Doolittle
      Released: 1989
    </div>
    #HTML revision here:
    <a href="/albums/1>Get info for this Album.</a>
    <div>
      Title: Surfer Rosa
      Released: 1988
    </div>
    <a href="/albums/2>Get info for this Album.</a>
    <!-- ... -->
  </body>
</html>

<!-- Example for GET /albums/1 -->

<html>
  <head></head>
  <body>
    <h1>Doolittle</h1>
    <p>
      Release year: 1989
      Artist: Pixies
    </p>
  </body>
</html>

<!-- Example for GET /albums/2 -->

<html>
  <head></head>
  <body>
    <h1>Surfer Rosa</h1>
    <p>
      Release year: 1988
      Artist: Pixies
    </p>
  </body>
</html>

Test-drive and implement a form page to add a new artist.

You should then be able to use the form in your web browser to add a new artist, and see this new artist in the artists list page.

--- ROUTE LAYOUT ---
GET /albums
    No inputs. Returns html listed above.

tables/seeds/classes already created and imported.

html code needs compiling to allow for dynamic input. Tests need to be written for the app.py

GET /albums/<id>
    No inputs besides specifying the album from the address. Will return similar  HTML to what is above. Additional HTML will add a link to the current albums get info page. No changes needed to the class or what it returns. Just a change to albums.html

GET /artists/new
    Directs the user to a form to fill out to create a new artist in the database.
    It will validate the input to ensure that the form is filled out correctly and either tell the user that they're errors or redirect them to the newly created artist page at /artists/<newid>. HTML design will be located in artists/new_artist.html. HTML for /artists will need to be amended to have a link to create a new artist. This will then send the user to the POST method for /artists explained below.

POST /artists
  Will collect the information from the form provided by the user and, if it is valid, will create a new Artist object. Otherwise, it will redirect back to the form and inform the user of the errors in the last submission.
  Artist model class will need a isvalid() function and a generate_errors() function
    

--- CLASS REVISION ---

AlbumRepository - Repository Class

  * get_album_info(): Takes albumid:integer as input. Returns a single album object and the artist name. No side effects.
  executes '''SELECT 
                  albums.id,
                  albums.title,
                  albums.release_year,
                  albums.artist_id,
                  artists.name
              FROM albums
              JOIN artists ON albums.artist_id = artists.id
              WHERE albums.id = %s''',[albumid]

  i.e get_album_info(1) would return Album(1,'Doolittle',1989,1),'Pixies' these can then be used by the route to feed into the HTML.

Artist - Model Class
  * isvalid() - Checks the values of name and genre to ensure they are not empty. No inputs. Returns True or False based on validity. No side effects.
  * generate_errors() - appends an error message to a error_list to then return to the user based on any blank entries. No inputs. Returns a string containing error text. No side effects.

  


