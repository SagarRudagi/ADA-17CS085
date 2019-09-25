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
            #print(w)
            for i in range(self.c):
                if self.g[w][i]==1 and visited[i]==False:
                    visited[i]=True
                    q.append(i)
                    print(i)
                    #q.pop(0)

                
n=int(input())
g=[]
for i in range(n):
    g.append(list(map(int,input().split())))

m = graph(g,n,n)
m.bfs(2)
