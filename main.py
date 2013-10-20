from dir_search import *
from db_query import *
import os
import urllib


def main():
	paths=['/media/My_Data/Videos/Movies','/media/E494330B9432E02A/linux downloads']
	search_ready_dict=get_list(paths)
	search_ready_list=search_ready_dict.keys()
	count=0
	for i in search_ready_list:
		count+=1
		print count,
		print i+' ->'
		movie=net_search(i)
		if movie:
			print 'title- '+str(movie.title)
			print 'type- '+str(movie.type)
			print 'year- '+str(movie.year)
			print 'tagline- '+str(movie.tagline)
			print 'plot- '+str(movie.plot)
			print 'runtyme- '+str(movie.runtime)
			print 'rating- '+str(movie.rating)
			print 'genres- '+str(movie.genres)
			print 'votes- '+str(movie.votes)
			#~ print 'poster- '+str(movie.poster_url)
			#~ print 'wget -B -O '+search_ready_dict[i]+'/poster.jpg '+movie.poster_url
			details=open(search_ready_dict[i]+'/moviedata.txt','w+')
			details.write( 'title- '+str(movie.title)+'\ntype- '+str(movie.type)+'\nyear- '+str(movie.year)+'\ntagline-'+str(movie.tagline)+'\nplot-'+str(movie.plot_outline)+'\nruntyme- '+str(movie.runtime)+'\nrating- '+str(movie.rating)+'\ngenres- '+str(movie.genres)+'\nvotes- '+str(movie.votes))
			urllib.urlretrieve (movie.poster_url, search_ready_dict[i]+'/poster.jpg ')
			details.flush()
		break
		
main()
