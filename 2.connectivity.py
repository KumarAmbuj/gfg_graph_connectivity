from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,vis):
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)

    def findtranspose(self):

        g=Graph(self.v)

        for u in self.graph:
            for v in self.graph[u]:
                g.addEdge(v,u)
        return g


    def isSC(self):

        vis=[False for i in range(self.v)]

        self.dfs(0,vis)

        for i in range(self.v):
            if vis[i]==False:
                return False

        gr=self.findtranspose()

        vis=[False for i in range(self.v)]
        gr.dfs(0,vis)

        for i in range(self.v):
            if vis[i]==False:
                return False
        return True

g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print(g1.isSC())

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print(g2.isSC())
