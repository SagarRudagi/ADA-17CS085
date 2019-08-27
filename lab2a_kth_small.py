lst = list(map(int,input().split()))
k = int(input())

for i in range(k):
	min = i
	for j in range(i+1,len(lst)):
		if lst[min]>lst[j]:
			min = j
	lst[min],lst[j] = lst[j],lst[min]

print(lst[k])
