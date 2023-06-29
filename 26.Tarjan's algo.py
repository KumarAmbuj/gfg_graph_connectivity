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
        self.time=0

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,low,disc,vis,s):
        low[u]=disc[u]=self.time
        self.time+=1
        vis[u]=True
        Push(s,u)

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,low,disc,vis,s)

                low[u]=min(low[u],low[v])
            elif vis[v]==True:
                low[u]=min(low[u],disc[v])

        if low[u]==disc[u]:
            w=-1
            while(Size(s) and w!=u):
                w=Pop(s)
                print(w,end=' ')
            print()


    def SCC(self):
        low=[999 for i in range(self.v)]
        disc=[999 for j in range(self.v)]

        vis=[False for i in range(self.v)]
        s=Stack()
        for i in range(self.v):
            if vis[i]==False:
                self.dfs(i,low,disc,vis,s)


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("SSC in first graph ")
g1.SCC()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("SSC in second graph ")
g2.SCC()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("SSC in third graph ")
g3.SCC()

g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print("SSC in fourth graph ")
g4.SCC();

g5 = Graph(5)
g5.addEdge(0, 1)
g5.addEdge(1, 2)
g5.addEdge(2, 3)
g5.addEdge(2, 4)
g5.addEdge(3, 0)
g5.addEdge(4, 2)
print("SSC in fifth graph ")
g5.SCC();
