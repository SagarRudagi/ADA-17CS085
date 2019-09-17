class graph:
    def __init__(self,g,r,c):
        self.g=g
        self.r=r
        self.c=c
    def bfs(self,v):
        visited=[]
        for i in range(self.r):
            visited.append(False)
        
        q=[]
        visited[v]=True
        q.append(v)
        print(v)
        while(len(q)!=0):
            w=q.pop(0)
            for i in range(self.c):
                if self.g[v][i]==1 and visited[i]==False:
                    visited[i]=True
                    q.append(i)
                    print(i)
                    q.pop(0)
                
g=[[1,1,1,0],[1,0,0,0],[1,1,1,0],[0,0,0,1]]
m=graph(g,4,4)
m.bfs(2)