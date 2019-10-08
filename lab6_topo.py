global n
n = int(input())

graph = []

for i in range(n):
	graph.append(list(map(int,input().split())))

in_degree = {}
for i in range(n):
	for j in range(n):
		in_degree[j] = in_degree.get(j,0) + graph[i][j]

seq = dict(sorted(in_degree.items(), key = lambda x : x[1]))
print(list(seq.keys()))
