from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
        self.time=0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis):
        vis[u]=True
        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)

    def isAP(self,u,vis,par,disc,low):
        vis[u]=True
        disc[u]=self.time
        low[u]=self.time
        self.time+=1
        child=0

        for v in self.graph[u]:
            if vis[v]==False:
                par[v]=u
                child+=1

                if self.isAP(v,vis,par,disc,low):
                    return True

                low[u]=min(low[u],low[v])

                if par[u]==-1 and child>1:
                    return True

                if par[u]!=-1 and low[v]>=disc[u]:
                    return True

            elif v!=par[u]:
                low[u]=min(low[u],disc[v])
        return False




    def isBC(self):
        vis=[False for i in range(self.v)]

        self.dfs(0,vis)

        for i in range(self.v):
            if vis[i]==False:
                return False

        par=[-1 for i in range(self.v)]
        vis=[False for i in range(self.v)]
        disc=[999 for i in range(self.v)]
        low=[999 for i in range(self.v)]

        return not self.isAP(0,vis,par,disc,low)

g1 =  Graph(2)
g1.addEdge(0, 1)
print(g1.isBC())

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(2, 4)
print("Yes" if g2.isBC() else "No")

g3 = Graph(3)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
print("Yes" if g3.isBC() else "No")

g4 = Graph(5)
g4.addEdge(1, 0)
g4.addEdge(0, 2)
g4.addEdge(2, 1)
g4.addEdge(0, 3)
g4.addEdge(3, 4)
print("Yes" if g4.isBC() else "No")

g5 = Graph(3)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 0)
print("Yes" if g5.isBC() else "No")