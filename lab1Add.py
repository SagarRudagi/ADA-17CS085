lst = []
lst.extend(map(int,input().split(" ")))
key = int(input())
first,last = 0,0
count = 0
start, end = 0, len(lst)-1
while start<=end:
	mid = int((start+end)/2)
	if lst[mid]==key:
		for i in range(mid,end+1):
			if lst[i]==key:
				count = count + 1
				last = i
			else:
				break
		for j in range(mid,start,-1):
			if lst[j]==key:
				count = count + 1
				first = j
			else:
				break
		print(first," ",last," ",(count-1))
		break
	elif key>lst[mid]:
		start = mid + 1
	else:
		end = mid - 1

