import random
import numpy as numpy

def printWatched():
	input_file = open("movies.txt")
	total_num_movies = len(input_file.readlines())
	input_file.close()

	watched = []
	watched = numpy.loadtxt("watched.npy", dtype='str', delimiter='\n')

	for movie in watched:
		print(movie)

	print(str(len(watched))  + "/" + str(total_num_movies) + "\n")

def genMovie():
	# Get number of total movies
	input_file = open("movies.txt")
	total_num_movies = len(input_file.readlines())
	input_file.close()

	watched = []
	watched = numpy.loadtxt("watched.npy", dtype='str', delimiter='\n')

	if len(watched) == total_num_movies:
		print("You have watched all " + str(total_num_movies) + " movies")
		exit()

	to_watch = []
	to_watch = numpy.loadtxt("to_watch.npy", dtype='str', delimiter='\n')

	rand_index = random.randint(0, len(to_watch))
	todays_movie = to_watch[rand_index]
	to_watch = numpy.delete(to_watch, rand_index)

	watched = numpy.append(watched, todays_movie)
	numpy.savetxt("watched.npy", watched, fmt='%s', delimiter=' ')
	numpy.savetxt("to_watch.npy", to_watch, fmt='%s', delimiter=' ')

	print("Today's movie is:\n" + todays_movie)
	print("Number " + str(len(watched)) + " of " + str(total_num_movies) + "\n")

ask = ""
while ask != "Q" and ask != "q":
	ask = input("[G] generate movie\n[W] show watched movies\n[Q] quit\n> ")
	if ask == "G" or ask == "g":
		genMovie()
	elif ask == "W" or ask == "w":
		printWatched()

print("Goodbye")
