from lib.album import Album
import json

# Tests for your routes go here

"""
GET /albums
"""
def test_get_all_albums(web_client, db_connection):
    # Given a GET reqest
    # It returns a list of all current albums
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.get("/albums")
    album_list = [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]
    final_list = []
    for album in album_list:
        final_list.append(album.__dict__)
    assert response.status_code == 200
    assert json.loads(response.data) == final_list

"""
POST /albums
"""
def test_create_new_album(web_client):
    # Given a post request containing album data
    # It creates a new album entry in the database and returns a 200 status code.
    response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': 2})
    assert response.status_code == 200

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
