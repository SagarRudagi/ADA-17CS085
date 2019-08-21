lst = list(map(int,input().split()))
k = int(input())

for i in range(k):
	for j in range(len(lst)-1-i):
		if lst[j]>lst[j+1]:
			lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst[-k:])
