arr = []
f = open("lab0Add.txt", "r")
for line in f:
	arr.append(line.split(" "))

print(arr)