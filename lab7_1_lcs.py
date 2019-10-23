str1 = input()
len1 = len(str1)
str2 = input()
len2 = len(str2)

graph = [[0]*(len2+1) for i in range(len1+1)]
# print(graph)

for i in range(len1+1):
	for j in range(len2+1):
		if i==0 or j==0:
			graph[i][j]=0
		elif str1[i-1] == str2[j-1]:
			graph[i][j] = graph[i-1][j-1] + 1
		else:
			graph[i][j]=max(graph[i-1][j],graph[i][j-1])

print(graph[len1][len2])
# print(graph)

i = len1
j = len2
index = graph[len1][len2]
global lcs
lcs = [None for i in range(index)]
# print(lcs)
while i>0 and j>0:
	if str1[i-1] == str2[j-1]:
		lcs[index-1] = (str1[i-1])
		i-=1
		j-=1
		index-=1
	elif graph[i-1][j]>graph[i][j-1]:
		i-=1
	else:
		j-=1

print("".join(lcs))
