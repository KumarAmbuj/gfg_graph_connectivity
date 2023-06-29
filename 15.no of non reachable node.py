from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis):
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)


    def countNonReach(self,s):
        vis=[False for i in range(self.v)]

        self.dfs(s,vis)

        count=0

        for i in range(self.v):
            if vis[i]==False:
                count+=1
        print(count)

g = Graph(8)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(6, 7)
g.countNonReach(2)