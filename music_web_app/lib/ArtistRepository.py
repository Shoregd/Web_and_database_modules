class ArtistRepository:
    def __init__(self,connection):
        self._connection = connection

    def list_artist_names(self):
        rows = self._connection.execute('SELECT artists.name FROM artists')
        nameslist = []
        for row in rows:
            nameslist.append(row['name'])

        return ', '.join(nameslist)
    def add_artist(self,artistname,artistgenre):
        self._connection.execute('INSERT INTO artists (name,genre) VALUES(%s,%s)',[artistname,artistgenre])