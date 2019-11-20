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
minimum = inf

for i in range(len(edges[src])):
	cost[edges[src][i][0]] = edges[src][i][1]
print(cost)
count+=1

while count < n:
	for i in range(n):
		if not visited[i]:
			if cost[i]<minimum:
				minimum = cost[i]
				minimumVert = i


for i in range(n):
	print(edges[i])