import math
lst = []
key = int(input())
for i in range(key+1):
	lst.append(i)
root = int(math.sqrt(key))
start, end = 0, key
while start<=end:
	mid = int((start+end)/2)
	if lst[mid] == root:
		print(lst[mid])
		break
	elif root>lst[mid]:
		start = mid + 1
	else :
		end = mid - 1



