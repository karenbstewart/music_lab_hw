from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (artists_name) VALUES (%s) RETURNING *"
    values = [artist.artists_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['artists_name'])
        artists.append(artist)
    return artists 



