current_movies = {'The Grinch' : '11:00am', 'Rudolph' : '1:00pm',
                  'Frosty' : '3:00pm', 'xmas' : '5:00pm'}

print('Showing:')
for key in current_movies:
    print(key)

movie = input('What movie time?\n')
showtime = current_movies.get(movie)
if showtime == None:
    print('Wrrrooooong!')
else:
    print('Time for', movie, 'is', showtime)