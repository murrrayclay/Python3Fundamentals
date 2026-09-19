def find_acronym():
    look_up = input("What do you want?\n")

    found = False
    try:
        with open('AcronymsList.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('NOT FOUND error!!')
        return
    if not found:
        print('not found mate!')

def add_acronym():
    acronym = input('what u wanna add?\n')
    definition = input('what it means though?\n')
    with open('AcronymsList.txt', 'a') as my_file:
        my_file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('red or blue pill?')
    if choice == 'red':
        find_acronym()
    elif choice == 'blue':
        add_acronym()

main()
    
