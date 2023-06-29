from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v,w):
        self.graph[u].append([v,w])
        self.graph[v].append([u,w])

    def dfs(self,u,vis,psf,k):

        vis[u] = True
        if psf>=k:
            return True

        for x in self.graph[u]:
            v=x[0]
            w=x[1]

            if vis[v]==False:
                if self.dfs(v,vis,psf+w,k):
                    return True

        vis[u]=False
        return psf>k

    def ispossible(self,src,k):
        vis=[False for i in range(self.v)]

        if self.dfs(src,vis,0,k):
            return True

        return False


V = 9
g = Graph(V)

#  making above shown graph
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

src = 0
k = 62
if g.ispossible(src, k):
    print("Yes")
else:
    print("No")

k = 60
if g.ispossible(src, k):
    print("Yes")
else:
    print("No")
