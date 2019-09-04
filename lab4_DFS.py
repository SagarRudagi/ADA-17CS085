# Uses dfs.txt as input

n = int(input())
adjacent=[]
for i in range(n):
	adjacent.append(list(map(int,input().split())))


visited=[]
for i in range(n):
	visited.append(0)


def DFS(v):
	print(v," ",end="")
	visited[v]=1
	for i in range(n):
		#print(i)
		if(adjacent[v][i]==1 and visited[i]==0):
			DFS(i)


for i in range(n):
	if(visited[i]==0):
		#print(i," ", end="")
		DFS(i)
		print()



