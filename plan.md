# User Story
```
As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of album's release years.
```

# Nouns
albums, titles, release_years

# Columns

| Record                | Properties                         |
| --------------------- | ---------------------------------- |
| album                 | id, title, release year, artist_id |

# Types

album:
    id: SERIAL
    title: text
    release_year: int
    artist_id: int

# Route Signature
```
# Request
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response
(200 OK)
(No content)
```