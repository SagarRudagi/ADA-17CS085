lst = [9,4,0,3,7,1,6,2,5,8]
count = 0 

for i in range(len(lst)):
	min = i
	for j in range(0,len(lst)):
		if lst[min]>lst[j]:
			count+=1
			min = j
	lst[min],lst[j] = lst[j],lst[min]

print(count)