from lib.Artist import Artist

class ArtistRepository:
    def __init__(self,connection):
        self._connection = connection

    def list_artists(self):
        rows = self._connection.execute('SELECT * FROM artists')
        artistlist = []
        for row in rows:
            data = Artist(row['id'],row['name'],row['genre'])
            artistlist.append(data)

        return artistlist
    def add_artist(self,artistname,artistgenre):
        self._connection.execute('INSERT INTO artists (name,genre) VALUES(%s,%s)',[artistname,artistgenre])
        rows = self._connection.execute('SELECT * FROM artists')
        row = rows[-1]
        return Artist(row['id'],row['name'],row['genre'])
    def get_artist(self,artist_id):
        rows = self._connection.execute('SELECT * FROM artists WHERE id=%s',[artist_id])
        row = rows[0]
        return Artist(row['id'],row['name'],row['genre'])