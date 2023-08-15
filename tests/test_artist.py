from lib.artist import Artist

def test_creates_new_artist():
    # Given artist data
    # It creates an artist object.
    artist = Artist(1, "Hello", "Goodbye")
    assert artist.id == 1
    assert artist.name == "Hello"
    assert artist.genre == "Goodbye"
