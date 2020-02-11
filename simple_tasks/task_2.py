import os
filename = input("Enter:").split()
if os.path.isabs(filename[1]):
    f = filename[1]
else:
    f = os.getcwd().join(filename[1])
if filename[0] == 'cd':
    try:
        print(os.getcwd())
        os.chdir(filename[1])
        print(os.getcwd())
    except FileNotFoundError:
        print("File not found")

if filename[0] == 'append':
    file = open(filename[1], 'a')
    file.write(input("Enter what you want to write in file:"))
    file.close()
