from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,vis,d,k,psf,count):
        if len(psf)-1>k:
            return
        if u==d:
            if len(psf)-1==k:
                print(psf)
                count[0]+=1
            return
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis,d,k,psf+str(v),count)

        vis[u]=False

    def findkedges(self,s,d,k):

        vis=[False for i in range(self.v)]
        count=[0]
        self.dfs(s,vis,d,k,str(s),count)
        print(count[0])


graph = [[0, 1, 1, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 1, ],
         [0, 0, 0, 0]]

g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,3)


u = 0;
v = 3;
k = 2
g.findkedges(u,v,k)

