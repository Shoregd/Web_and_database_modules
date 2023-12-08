import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.AlbumRepository import AlbumRepository
from lib.ArtistRepository import ArtistRepository
from lib.Album import Album
from lib.Artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


@app.route('/albums',methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    result = repository.list_albums()
    return render_template('album/albums.html', albums=result)

@app.route('/albums',methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    new_album = Album(None,title,release_year,artist_id)
    if not new_album.isvalid():
        return render_template('album/new_album.html',errors=new_album.generate_errors()), 400
    new_album = repository.add_album(new_album.title,new_album.release_year,new_album.artist_id)

    return redirect(f'/albums/{new_album.id}')

@app.route('/albums/<int:id>', methods=['GET'])
def get_album_info(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album,artistname = repository.get_album_info(id)
    return render_template('album/albuminfo.html',album=album,artistname=artistname)

@app.route('/albums/new',methods=['GET'])
def create_new_album():
    return render_template('album/new_album.html')

@app.route('/artists',methods=['GET'])
def get_artist_names():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.list_artists()
    return render_template('artists/list_artists.html',artists=artists)

@app.route('/artists',methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    new_artist = Artist(None,name,genre)
    if not new_artist.isvalid():
        return render_template('artists/new_artist.html',errors = new_artist.generate_errors()),400
    new_artist = repository.add_artist(new_artist.name,new_artist.genre)
    return redirect(f'/artists/{new_artist.id}')


@app.route('/artists/new',methods=['GET'])
def create_new_artist():
    return render_template('artists/new_artist.html')

@app.route('/artists/<int:id>',methods=['GET'])
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.get_artist(id)
    return render_template('artists/artist_info.html',artist=artist)
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
