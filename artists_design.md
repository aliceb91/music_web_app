# 1. Extract nouns from the user stories or specification
```
As a music lover,
So I can organise my music colleciton,
I want to keep a list of artists' names.

As a music lover,
So I can organise my music collection,
I want to keep a list of artists' genres.
```
```
Nouns:
artist, name, genre
```

# 2. Infer the Table Name and Columns
| Record                | Properties                         |
| --------------------- | ---------------------------------- |
| artist                | id, artist_name , genre            |

Name of the table: artists
Column name: id, title, release_year

# 3. Decide the column types

```
id: SERIAL
artist_name: text
genre: text
```

# 4. Write the SQL
```
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
)
```

# 5. Create the table
```
psql -h 127.0.0.1 music_web_app < seeds/artists_table.sql
```