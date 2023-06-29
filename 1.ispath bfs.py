from collections import defaultdict
def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)



    def isReachable(self,s,d):

        vis=[False for i in range(self.v)]

        queue=Queue()

        Enqueue(queue,s)

        while(Size(queue)):
            u=Dequeue(queue)

            if u==d:
                return True

            if vis[u]==True:
                continue

            vis[u]=True

            for v in self.graph[u]:
                if vis[v]==False:
                    Enqueue(queue,v)
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.isReachable(1,3))