from lib.album import Album

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, album):
        # Creates a new entry in the albums table
        #
        # Parameters:
        #   album: An Album object
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Inserts the data from the Album object as a row in the albums table.
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)',
            [album.title, album.release_year, album.artist_id]
        )

    def delete(self, album_id):
        # Removes the specified entry from the albums table
        #
        # Parameters:
        #   album_id: The target album for deletion.
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Removes the requested album from the albums table.
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s',
            [album_id]
        )