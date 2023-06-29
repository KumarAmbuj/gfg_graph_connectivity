from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,hash):
        hash.add(u)

        for v in self.graph[u]:
            if v not in hash:
                if self.dfs(v,hash):
                    return True
            elif v in hash:
                return True
        return False


    def iscycle(self,arr):

        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue

                if arr[i][-1]==arr[j][0]:
                    self.graph[arr[i]].append(arr[j])

        hash=set()

        for x in self.graph:
            if x not in hash:
                if self.dfs(x,hash):
                    return True
        return False

arr = ["geek", "king"]
g=Graph(len(arr))
print(g.iscycle(arr))

arr = ["for", "geek", "rig", "kaf"]
g=Graph(len(arr))
print(g.iscycle(arr))