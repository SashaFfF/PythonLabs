from container import Container


def user_input():
    command_input = input('Enter the command: ').split(maxsplit=1)
    command = command_input[0]
    elements = str()

    if len(command_input) > 1:
        elements = command_input[1]

    return command, elements


def current_command(command, elements, storage: Container):
    if command == 'add':
        element = elements.split()
        for i in element:
            storage.add(i)
    elif command == 'remove':
        if elements in storage.list():
            storage.remove(elements)
        else:
            print(f'Element {elements} not found')
    elif command == 'find':
        element = elements.split()
        for i in element:
            el = storage.find(i)
            if el:
                print(f'Element "{el}" found')
            else:
                print(f'Element "{el}" not found')
    elif command == 'list':
        print(storage.list())
    elif command == 'grep':
        element = storage.grep(elements)
        if len(element) != 0:
            print('Found values: ', element)
    elif command == 'save':
        storage.save()
    elif command == 'load':
        storage.load()
    elif command == 'switch':
        answer = input('Do you want save container before exit? (y/n) ')
        if answer == 'y':
            storage.save()
        storage.switch(elements)
        answer = input('Do you want load container before exit? (y/n) ')
        if answer == 'y':
            storage.load()
    elif command == 'load':
        storage.load()
    elif command == 'info':
        print('INFO:'
              '\n****************************'
              '\nadd <key> [key, ...] - add one or more elements to the container'
              '\nremove <key> - delete key from container'
              '\nfind - <key> [key, ...] - check if the element is presented in the container'
              '\nlist - print all elements of container'
              '\ngrep <regex> - check the value in the container by regular expression'
              '\nsave - save container to file'
              '\nswitch - switches to another user'
              '\n****************************')
    elif command == 'stop':
        answer = input('Do you want save container before exit? (y/n) ')
        if answer == 'y':
            storage.save()
        return False
    else:
        print(f'There is no such command: {command}')

    return True