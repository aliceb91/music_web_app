# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

#def test_create_new_album(web_client):
#    # Given a post request containing album data
#    # It creates a new album entry in the database and returns a 200 status code.
#    response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': 2})
#    assert response.status_code == 200

# === End Example Code ===
