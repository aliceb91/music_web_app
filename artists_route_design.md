# 1. Design the Route Signature
```
# Artists route
GET /artists

# Submit artist route
POST /artists
    artist_name: string
    genre: string
```

# 2. Create Examples as Tests
```python
# GET /artists
#   Expected response (200 OK):
Pixies, Abba, Taylor Swift, Nina Simone
```
```python
# POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```