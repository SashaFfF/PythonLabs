from container import Container
from function import user_input, current_command

print('Container of unique elements'
      '\n****************************')
username = input('Enter your username: ')
storage = Container(username)

print(f'****************************\n'
      f'{username}-container is available now'
      f'\n!Type "info" for more information!'
      f'\n****************************')

current = True
while current:
    command, elements = user_input()
    current = current_command(command, elements, storage)