from math import inf

def floyd(graph,n):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

	for i in range(n):
		print(graph[i])

n = int(input())
graph = []
for i in range(n):
	graph.append(list(map(float,input().split())))

floyd(graph,n)

"""
INPUT

5
0 2 inf 1 8
6 0 3 2 inf
inf inf 0 4 inf
inf inf 2 0 3
3 inf inf inf 0


OUTPUT

[0.0, 2.0, 3.0, 1.0, 4.0]
[6.0, 0.0, 3.0, 2.0, 5.0]
[10.0, 12.0, 0.0, 4.0, 7.0]
[6.0, 8.0, 2.0, 0.0, 3.0]
[3.0, 5.0, 6.0, 4.0, 0.0]

"""