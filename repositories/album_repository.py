from db.run_sql import run_sql
import repositories.artist_repository as artist_repository

from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING * "
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return 





# # def select_all():  
#     albums = [] 

#     sql = "SELECT * FROM albums"
#     results = run_sql(sql)

#     for row in results:

#         artist = artist_repository.select(row['artists_id'])

#         album = Album(row['title'], row['genre'] ,artist , row['id'] )
#         albums.append(album)
#     return albums 