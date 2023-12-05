import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.AlbumRepository import AlbumRepository
from lib.ArtistRepository import ArtistRepository
# Create a new Flask app
app = Flask(__name__)

@app.route('/albums',methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albumtitle = request.form['title']
    releaseyear = request.form['release_year']
    artistid = request.form['artist_id']
    repository.add_album(albumtitle,releaseyear,artistid)
    return ('')

@app.route('/albums',methods=['GET'])
def list_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
   
    return repository.list_albums()

@app.route('/artists', methods=['GET'])
def get_artist_names():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return repository.list_artist_names()

@app.route('/artists', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artistname = request.form['name']
    artistgenre = request.form['genre']
    repository.add_artist(artistname,artistgenre)
    return ('')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))