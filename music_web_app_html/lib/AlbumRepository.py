from lib.Album import Album
class AlbumRepository:
    def __init__(self,connection):
        self._connection = connection

    def list_albums(self):
        albumlist = []
        rows = self._connection.execute('SELECT * FROM albums')
        for row in rows:
            data = Album(row['id'],row['title'],row['release_year'],row['artist_id'])
            albumlist.append(data)
        return albumlist
    def add_album(self,albumtitle,releaseyear,artistid):
        self._connection.execute(
            'INSERT INTO albums (title,release_year,artist_id) VALUES (%s,%s,%s)',[albumtitle,releaseyear,artistid]
        )
    def get_album_info(self,albumid):
        rows = self._connection.execute(
            '''SELECT 
                  albums.id,
                  albums.title,
                  albums.release_year,
                  albums.artist_id,
                  artists.name
              FROM albums
              JOIN artists ON albums.artist_id = artists.id
              WHERE albums.id = %s''',[albumid]
        )
        row = rows[0]
        data = Album(row['id'],row['title'],row['release_year'],row['artist_id'])
        return data,row['name']
        
        