from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
        self.time=0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge(self,u,vis,low,disc,l,par):
        vis[u]=True
        low[u]=disc[u]=self.time
        self.time+=1

        for v in self.graph[u]:
            if vis[v]==False:
                par[v]=u

                self.bridge(v,vis,low,disc,l,par)

                low[u]=min(low[u],low[v])

                if low[v]>disc[u]:
                    l.append((u,v))
            elif v!=par[u]:
                low[u]=min(low[u],disc[v])

    def findbridges(self):

        vis=[False for i in range(self.v)]
        low=[999 for i in range(self.v)]
        disc=[999 for i in range(self.v)]
        par=[-1 for i in range(self.v)]
        l=[]

        for i in range(self.v):
            if vis[i]==False:
                self.bridge(i,vis,low,disc,l,par)

        for x in l:
            print(x,end=' ')
        print()


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

print("Bridges in first graph ")
g1.findbridges()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nBridges in second graph ")
g2.findbridges()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nBridges in third graph ")
g3.findbridges()