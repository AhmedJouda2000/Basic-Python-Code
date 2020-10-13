import sys
import random

filename1 = sys.argv[1]
rand_num_req = sys.argv[2]
try:
    file = open(filename1, 'r')
except FileNotFoundError:
    print("Unable to read from file: [Errno 2] No such file or directory:", filename1)
Lines = file.readlines()

if int(rand_num_req) > len(Lines):
    raise ValueError("ValueError exception thrown")

list_wanted = random.sample(range(1, len(Lines)), int(rand_num_req))
for i in list_wanted:
    print(Lines[i], end = "")
