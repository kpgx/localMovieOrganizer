import os
import re


def get_list(PATHS):
	#input=list of strings,each string containing path of a movie folder
	#output=search ready alphabatically sorted movie name list
	#needed=movie names have to bo more optimized to search for getting more accurate results(target 100%)
	paths=PATHS
	name_list_dirty=[]
	path_list={}
	name_list_clean=[]
	
	def clean_(name):
		name=name.replace('.',' ')
		name=name.replace('_',' ')
		wordList = re.sub("[^\w]", " ",  name).split()
		clean_name=''
		omit_list=['xvid','720p','avi','dvdrip','br','mkv','3d','divx','mp4','wmv']
		for word in wordList:
			if (word.isdigit() and len(word)==4) or word.lower() in omit_list:
				if len(clean_name)>0:
					break
				else:
					continue
			clean_name+=word+' '
					
		return clean_name
	
	for PATH in PATHS:
		for dirpath, dirnames, filenames in os.walk(PATH):
			for f in filenames:
				movie_path= os.path.join(dirpath, f)		
				file_size= os.path.getsize(movie_path)			
				size_limit=107434370*5 # ~500mb
				if file_size>size_limit:
					name_list_dirty.append(f)
					f_clean=clean_(f)									
					name_list_clean.append(f_clean)				
					path_list[f_clean]=dirpath
	name_list_clean=list(set(name_list_clean))
	#~ name_list_clean.sort()		
	#~ return name_list_clean
	return path_list


