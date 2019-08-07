arr = []
n = int(input("Number of elements : "))
print("Elements : ")

for i in range(n):
	arr.append(int(input()))

arr.sort()
key = int(input("Key : "))
if key in arr:
	print("Found at position ",arr.index(key))
else :
	print("Not found")
