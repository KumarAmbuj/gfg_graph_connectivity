from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def noofedge(self):

        odd=0

        for u in self.graph:
            if len(self.graph[u])%2==1:
                odd+=1

        if odd%2==1:
            print('not possible')
        else:
            print(odd//2)

g=Graph(3)
g.addEdge(1,2)
g.addEdge(2,3)
g.noofedge()
