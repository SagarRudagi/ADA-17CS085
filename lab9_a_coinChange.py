# paid = int(input())
# price = int(input())
change = int(input())
denoms = list(map(int,input().split()))

ls = []

for i in range(len(denoms)):
	ls.append([0]*(change+1))

for i in range(change+1):
	ls[0][i] = int(i/denoms[0])

for i in range(1,len(denoms)):
	for j in range(change+1):
		if denoms[i]>j:
			ls[i][j] = ls[i-1][j]
		else:
			ls[i][j] = min(ls[i-1][j],1 + ls[i][j-denoms[i]])

print(ls[len(denoms)-1][change])

print(ls)