from math import sqrt

def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j],end=" ") 
        print () 

def findUnassigned(graph,l):
	#global n
	for i in range(9):
		for j in range(9):
			if(graph[i][j]==0):
				l[0] = i
				l[1] = j
				return True
	return False

def inRow(graph,row,num):
	#global n
	for i in range(9):
		if(graph[row][i]==num):
			return True
	return False

def inCol(graph,col,num):
	#global n
	for i in range(9):
		if(graph[i][col]==num):
			return True
	return False

def inSubGrid(graph,row,col,num):
	#global n
	for i in range(int(sqrt(9))):
		for j in range(int(sqrt(9))):
			if(graph[i+row][j+col]==num):
				return True
	return False

def isSafe(graph,row,col,num):
	return not inRow(graph,row,num) and not inCol(graph,col,num) and not inSubGrid(graph,row-row%int(sqrt(9)),col-col%int(sqrt(9)),num)

def solveSudoku(graph):
	#global n
	l = [0,0]
	if(not findUnassigned(graph,l)):
		return True
	row = l[0]
	col = l[1]
	for k in range(1,10):
		if(isSafe(graph,row,col,k)):
			graph[row][col] = k
			if(solveSudoku(graph)):
				return True
			graph[row][col]=0
	return False

if __name__ =="__main__":
	n = int(input())
	graph=[]
	for i in range(n):
		graph.append(list(map(int,input().split())))
	if solveSudoku(graph):
		print_grid(graph)
	else:
		print("Some mistake")
	#	print_grid(graph)