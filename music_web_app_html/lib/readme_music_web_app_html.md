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

--- ROUTE LAYOUT ---
GET /albums
    No inputs. Returns html listed above.

tables/seeds/classes already created and imported.

html code needs compiling to allow for dynamic input. Tests need to be written for the app.py

GET /albums/<id>
    No inputs besides specifying the album from the address. Will return similar  HTML to what is above. Additional HTML will add a link to the current albums get info page. No changes needed to the class or what it returns. Just a change to albums.html

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

  


