from imdbpie import Imdb

def net_search(name):
	#input=movie name
	#output=movie id from imdb
	
	imdb = Imdb({'anonymize': False})
	#~ movie = imdb.find_movie_by_id("tt0382932")
	#~ print movie.title

	if len(name)>0:
		details=imdb.find_by_title(name)
		if len(details)>0:
			#~ return imdb.find_movie_by_id(details[0]['imdb_id'])
			imdb_id=details[0]['imdb_id']
			#~ print imdb_id
			movie=imdb.find_movie_by_id(imdb_id)
			return movie
		else:
			#~ return NULL
			return -1
		
