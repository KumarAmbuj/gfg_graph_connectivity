from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def removeEdge(self,u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def dfs(self,u,vis):
        count=1
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                count+=self.dfs(v,vis)
        return count


    def isvalid(self,u,v):
        if len(self.graph[u])==1:
            return True
        else:
            vis = [False for i in range(self.v)]

            count1 = self.dfs(u, vis)

            self.removeEdge(u, v)

            vis = [False for i in range(self.v)]

            count2 = self.dfs(u, vis)

            self.addEdge(u, v)

            return False if count1 > count2 else True



    def findeuler(self,u):
        for v in self.graph[u]:
            if self.isvalid(u,v):
                print('{}-{} '.format(u,v),end=' ')
                self.removeEdge(u,v)
                self.findeuler(v)

    def findeulerian(self):

        u=0
        for i in range(self.v):
            if len(self.graph[i])%2==1:
                u=i
                break

        self.findeuler(u)

g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.findeulerian()
print()

g2 = Graph(3)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.findeulerian()
print()

g3 = Graph(5)
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(3, 2)
g3.addEdge(3, 1)
g3.addEdge(2, 4)
g3.findeulerian()
print()