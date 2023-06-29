from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
        self.time=0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,disc,low,ap,vis,par):
        vis[u]=True

        disc[u]=self.time
        low[u]=self.time
        self.time+=1
        child=0

        for v in self.graph[u]:
            if vis[v]==False:
                par[v] = u
                child += 1
                self.dfs(v,disc,low,ap,vis,par)

                low[u]=min(low[u],low[v])

                if par[u]==-1 and child>1:
                    ap[u]=True

                if par[u]!=-1 and  low[v]>=disc[u]:
                    ap[u]=True





            elif v !=par[u]:
                low[u]=min(low[u],disc[v])


    def findAP(self):

        disc=[-1 for i in range(self.v)]
        low=[-1 for i in range(self.v)]
        ap=[False for i in range(self.v)]
        vis=[False for i in range(self.v)]
        par=[-1 for i in range(self.v)]

        for i in range(self.v):
            if vis[i]==False:
                self.dfs(2, disc, low, ap, vis, par)

        for i in range(self.v):
            if ap[i]==True:
                print(i,end=' ')
        print()

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.findAP()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)

g2.findAP()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)

g3.findAP()
