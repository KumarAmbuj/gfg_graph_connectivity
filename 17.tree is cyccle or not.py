from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCycle(self,u,vis,par):
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                par[v]=u
                if self.isCycle(v,vis,par):
                    return True

            elif v!=par[u]:
                return True

        return False


    def isTree(self):

        vis=[False for i in range(self.v)]
        par=[-1 for i in range(self.v)]

        if self.isCycle(0,vis,par):
            return False

        for i in range(self.v):
            if vis[i]==False:
                return False

        return True


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Graph is a Tree" if g1.isTree() == True \
    else "Graph is a not a Tree")

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
print("Graph is a Tree" if g2.isTree() == True \
    else "Graph is a not a Tree")