lst = [9,4,0,3,7,1,6,2,5,8]
count = 0 

for i in range(len(lst)):
	for j in range(len(lst)-1-i):
		if lst[j]>lst[j+1]:
			count+=1
			lst[j],lst[j+1]=lst[j+1],lst[j]

print(count)
