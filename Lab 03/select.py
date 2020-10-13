import sys

filename1 = sys.argv[1]
inputArgs = sys.argv[1::]
try:
    file = open(filename1, 'r')
except FileNotFoundError:
    print("Unable to read from file: [Errno 2] No such file or directory:", filename1)
Lines = file.readlines()

for i in inputArgs[1:]:
    try:
        print(Lines[int(i)-1], end ="")
    except ValueError:
        print("Invalid line number specified: invalid literal for int():", i)
