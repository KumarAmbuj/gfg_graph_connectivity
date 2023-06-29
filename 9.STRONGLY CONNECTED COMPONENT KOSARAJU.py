from collections import defaultdict
def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,vis,s):

        vis[u]=True
        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis,s)

        Push(s,u)

    def findtranspose(self):

        g=Graph(self.v)

        for u in self.graph:
            for v in self.graph[u]:
                g.addEdge(v,u)
        return g

    def findnode(self,u,vis,l):
        l.append(u)
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis,l)

    def SCC(self):

        s=Stack()
        vis=[False for i in range(self.v)]

        for i in range(self.v):
            if vis[i]==False:
                self.dfs(i,vis,s)

        gr=self.findtranspose()

        vis=[False for i in range(self.v)]

        while(Size(s)):
            u=Pop(s)
            if vis[u]==False:
                l=[]
                gr.findnode(u,vis,l)
                print(l)

g = Graph(5)
g.addEdge(1, 0) 
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.SCC()