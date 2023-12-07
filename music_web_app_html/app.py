import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.AlbumRepository import AlbumRepository

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
    return render_template('albums.html', albums=result)


@app.route('/albums/<int:id>', methods=['GET'])
def get_album_info(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album,artistname = repository.get_album_info(id)
    return render_template('albuminfo.html',album=album,artistname=artistname)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))