global n
n = int(input())

graph = []

for i in range(n):
	graph.append(list(map(int,input().split())))

in_degree = [0] * n
for i in range(n):
	for j in range(n):
		in_degree[j]+= graph[i][j]


print(in_degree)