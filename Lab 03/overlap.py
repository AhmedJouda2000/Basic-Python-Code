import sys
filename1 = sys.argv[-2]
filename2 = sys.argv[-1]

list1 = []
with open(filename1) as file1:
	line = file1.readline()
	while line:
		list1.append(int(line))
		line = file1.readline()

list2 = []
with open(filename2) as file2:
	line = file2.readline()
	while line:
		list2.append(int(line))
		line = file2.readline()

overlaplist = []
for elem in list1:
	if elem in list2:
		overlaplist.append(elem)

print(overlaplist)
