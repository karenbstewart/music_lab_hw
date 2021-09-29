import pdb 
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository  

artist1 = Artist("pink")
artist_repository.save(artist1)
artist2 = Artist("greenday")
artist_repository.save(artist2)

album1 = Album("Funhouse", "pop", artist1)
album_repository.save(album1)

artist_list = artist_repository.select_all()
print(artist_list)



pdb.set_trace()