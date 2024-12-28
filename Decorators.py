import os

path_file = os.path.abspath('ola.txt')
print(path_file)

path_file_1 = os.path.dirname(__file__)
file_path = os.path.join(path_file_1, 'ola.txt')
print(file_path)