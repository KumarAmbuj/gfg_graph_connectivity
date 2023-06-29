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
    def iseuleriancp(self):
        vis=[False for i in range(self.v)]
        self.dfs(0,vis)

        for i in range(self.v):
            if len(self.graph[i])>0 and vis[i]==False:
                return 0

        odd=0
        for x in self.graph:
            if len(self.graph[x])%2==1:
                odd+=1

        if odd==0:
            return 2
        if odd==2:
            return 1
        if odd>2:
            return 0

g1 = Graph(5);
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
res=g1.iseuleriancp()
if res==0:
    print('not eulerian')
elif res==1:
    print('eulerian path')
elif res==2:
    print('eulerian cycle')

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
res=g2.iseuleriancp()
if res==0:
    print('not eulerian')
elif res==1:
    print('eulerian path')
elif res==2:
    print('eulerian cycle')

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
res=g3.iseuleriancp()
if res==0:
    print('not eulerian')
elif res==1:
    print('eulerian path')
elif res==2:
    print('eulerian cycle')

g4 = Graph(3)
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
res=g4.iseuleriancp()
if res==0:
    print('not eulerian')
elif res==1:
    print('eulerian path')
elif res==2:
    print('eulerian cycle')

# Let us create a graph with all veritces
# with zero degree
g5 = Graph(3)

