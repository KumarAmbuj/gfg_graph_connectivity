from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,d,vis):

        if u==d:
            return True

        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                if self.dfs(v,d,vis):
                    return True
        return False

    def isReachable(self,s,d):

        vis=[False for i in range(self.v)]

        if self.dfs(s,d,vis):
            print('yes')
        else:
            print('no')

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.isReachable(1,3)