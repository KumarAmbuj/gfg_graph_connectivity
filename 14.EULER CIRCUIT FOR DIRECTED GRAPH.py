from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
        self.indegree=[0 for i in range(self.v)]
        self.outdegree=[0 for i in range(self.v)]

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.outdegree[u]+=1
        self.indegree[v]+=1

    def dfs(self,u,vis):
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)

    def transpose(self):

        g=Graph(self.v)

        for u in self.graph:
            for v in self.graph[u]:
                g.addEdge(v,u)
        return g

    def isEuler(self):

        vis=[False for i in range(self.v)]

        self.dfs(0,vis)

        for i in range(self.v):
            if vis[i]==False:
                return False

        gr=self.transpose()

        vis=[False for i in range(self.v)]

        gr.dfs(0,vis)

        for i in range(self.v):
            if vis[i]==False:
                return False


        for i in range(self.v):
            if self.indegree[i]!=self.outdegree[i]:
                return False

        return True

g = Graph(5);
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(3, 4);
g.addEdge(4, 0);
if g.isEuler():
    print('Euler cycle')
else:
    print('not found')