from collections import defaultdict
def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Peek(s):
    return s[-1]

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
        self.time=0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,par,vis,disc,low,s):
        vis[u]=True
        child=0
        disc[u]=self.time
        low[u] = self.time
        self.time+=1

        for v in self.graph[u]:
            if vis[v]==False:
                child+=1
                par[v]=u
                s.append((u,v))
                self.dfs(v,par,vis,disc,low,s)

                low[u]=min(low[u],low[v])

                if (par[u]==-1 and child>1) or (par[u]!=-1 and low[v]>=disc[u]) :
                    w=(0,0)
                    while(w!=(u,v)):
                        w=s.pop()
                        print(w,end=' ')
                    print()


            elif v!=par[u] and low[u]>disc[v]:
                low[u]=min(low[u],disc[v])
                Push(s,(u,v))



    def findBC(self):
        par=[-1 for i in range(self.v)]
        vis=[False for i in range(self.v)]
        disc=[999 for i in range(self.v)]
        low=[999 for i in range(self.v)]

        s=[]

        for i in range(self.v):
            if vis[i]==False:
                self.dfs(i,par,vis,disc,low,s)

                if Size(s):
                    while s:
                        w=s.pop()
                        print(w,end=' ')
                print()



g = Graph(12)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(1, 5)
g.addEdge(0, 6)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(7, 8)
g.addEdge(8, 9)
g.addEdge(10,11)
g.findBC()






