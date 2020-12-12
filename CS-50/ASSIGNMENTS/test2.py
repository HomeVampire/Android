import os

directory_path = os.path.join(os.getcwd(), 'files')
if not os.path.exists(directory_path):
            os.mkdir(directory_path)

file_path = os.path.join(directory_path, 'demo.txt')

f = open(file_path, 'w')
for i in range(10):
    f.write('hello')
    f.write(' ')
f.close()