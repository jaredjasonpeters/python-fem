from pprint import pprint as pp

import os

my_folder = os.getcwd()

print('Here are the files in my directory: ')
pp(my_folder)

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f' - {entry.name}')
