from math import inf
n, e, src = map(int,input().split())
edges = [[] for i in range(n)]

for i in range(e):
	s,d,w = map(int,input().split())
	edges[s].append([d,w])
	edges[d].append([s,w])


visited = [False for i in range(n)]
cost = [inf for i in range(n)]
cost[src] = 0
count = 0
visited[src] = True


for i in range(len(edges[src])):
	cost[edges[src][i][0]] = edges[src][i][1]

count+=1

while count < n:
	minimum = inf
	for i in range(n):
		if not visited[i]:
			if cost[i]<minimum:
				minimum = cost[i]
				minimumVert = i

	visited[minimumVert] = True
	for j in range(len(edges[minimumVert])):
		if not visited[edges[minimumVert][j][0]]:
			cost[edges[minimumVert][j][0]] = min(cost[edges[minimumVert][j][0]],minimum + edges[minimumVert][j][1])
	count +=1


print(cost)
for i in range(n):
	print(src," - ",i," -> ",cost[i])

"""
INPUT

5 7 2
0 1 3
1 4 1
4 3 7
3 2 2
2 0 1
1 2 7
1 3 5


OUTPUT

[1, 4, 0, 2, 5]
2  -  0  ->  1
2  -  1  ->  4
2  -  2  ->  0
2  -  3  ->  2
2  -  4  ->  5

"""
