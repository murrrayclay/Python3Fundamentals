acronym = input('what u wanna add?\n')
definition = input('what it means though?\n')
with open('AcronymsList.txt', 'a') as my_file:
    my_file.write(acronym + ' - ' + definition + '\n')

