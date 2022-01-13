import csv
import random
import readline
import numpy as numpy

input_file = open("movies.txt")

movies = []

for line in input_file:
	datalist = line.splitlines()
	movies += datalist

reserved = []
reserved = numpy.loadtxt("movie_history.npy", dtype=int)

def printWatched(reserved, movies):
	for num in reserved:
		print(str(num) + " " + movies[num])
	print(str(len(reserved))  + "/" + str(len(movies)) + "\n")

def genMovie(reserved, movies):
	rand_index = 0
	while True:
		rand_index = random.randint(0, 1209)
		if rand_index not in reserved:
			break
		if rand_index in reserved and reserved.size == movies.size:
			print("You have watched all " + str(movies.size) + " movies")
			exit()

	reserved = numpy.append(reserved, rand_index)

	numpy.savetxt("movie_history.npy", reserved, fmt='%d')

	todays_movie = movies[rand_index]

	print("Today's movie is:\n" + todays_movie)
	print("Number " + str(len(reserved)) + " of 1222\n")

ask = ""
while ask != "Q" and ask != "q":
	ask = input("[G] generate movie\n[W] show watched movies\n[Q] quit\n> ")
	if ask == "G" or ask == "g":
		genMovie(reserved, movies)
	elif ask == "W" or ask == "w":
		printWatched(reserved, movies)

print("Goodbye")





