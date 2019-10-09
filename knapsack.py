n = int(input()) #No of items
wv_val = []
for i in range(n):
	wt = list(map(int,input().split()))
	wv_val.append(wt)

# print(wv_val)
wv_val.sort()
# print(wv_val)
# wt_val = sorted(wt_val)

limit_wt = int(input()) #Knapsack Limit

table = [[0]*(limit_wt+1) for i in range(n)]
# print(table)

for i in range(n):
	for j in range(limit_wt+1):
		if wv_val[i][1]<=j:
			table[i][j] = max(table[i-1][j],(wv_val[i][1]+table[i-1][j-wv_val[i][0]]))
		elif wv_val[i][1]>j:
			table[i][j] = table[i-1][j]


for i in range(len(table)):
	print(table[i])
