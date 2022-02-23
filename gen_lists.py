import numpy

input_file = open("movies.txt") # Reopen movies file in case a change has been made
movies = []
# Fill movies array with title(year) of movies in list
for line in input_file:
	datalist = line.splitlines()
	movies += datalist
input_file.close()

watched = []
watched = numpy.loadtxt("watched.npy", dtype='str', delimiter='\n')

# Remove already seen movies from movies array
to_watch = []
for movie in movies:
    if movie not in watched:
        to_watch.append(movie)

numpy.savetxt("to_watch.npy", to_watch, fmt='%s', delimiter=' ')