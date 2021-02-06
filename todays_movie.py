import csv
import random
import readline
import numpy as numpy

input_file = open("/Users/trevorbonas/Desktop/Todays_Movie/movies.txt")

len = 0

movies = []

for line in input_file:
	datalist = line.splitlines()

	movies += datalist


#print(movies)

ask = input("Generate movie? [yn]\n")

if not ("y" in ask or "Y" in ask or "Yes" in ask or "YES" in ask):
	print("Okay, goodbye")
	exit()

reserved = []
reserved = numpy.loadtxt("/Users/trevorbonas/Desktop/Todays_Movie/movie_history.npy", dtype=int)

#with open("movie_history.txt") as f:
#		reserved += f.readlines()

rand_index = 0
while True:
	rand_index = random.randint(0, 1209)
	if rand_index not in reserved:
		break
	if rand_index in reserved and reserved.size == 1222:
		print("You have watched all 1222 movies")
		exit()

reserved = numpy.append(reserved, rand_index)

numpy.savetxt("/Users/trevorbonas/Desktop/Todays_Movie/movie_history.npy", reserved, fmt='%d')

#print(reserved.size)

#print(reserved)


todays_movie = movies[rand_index]

print("Today's movie is:\n" + todays_movie)
print("Number " + str(reserved.size) + " of 1222")



