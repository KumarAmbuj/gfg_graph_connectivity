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


    def removeEdge(self,u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def dfs(self,u,s,l):

        if len(self.graph[u])==0:
            l.append(u)
            if Size(s):
                self.dfs(Pop(s),s,l)
        else:
            v=self.graph[u][0]
            Push(s,u)
            self.removeEdge(u,v)
            self.dfs(v,s,l)


    def findeuler(self):
        u=0
        for i in range(self.v):
            if len(self.graph[i])%2==1:
                u=i
                break

        s=Stack()
        l=[]



        self.dfs(u,s,l)

        print(l)

graph1 = [ [ 0, 1, 0, 0, 1 ],
               [ 1, 0, 1, 1, 0 ],
               [ 0, 1, 0, 1, 0 ],
               [ 0, 1, 1, 0, 0 ],
               [ 1, 0, 0, 0, 0 ] ]
g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(4,0)
g.findeuler()



