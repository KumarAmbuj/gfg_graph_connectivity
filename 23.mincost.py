def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def findmincost(arr,s,d):

    queue=Queue()
    Enqueue(queue,s)

    dis=[99999 for i in range(len(arr))]

    dis[s]=0

    while(Size(queue)):
        u=Dequeue(queue)



        for i in range(len(arr[u])):
            if i==u:
                continue
            if arr[u][i]!='inf':
                v=i
                w=arr[u][i]

                if dis[v]>dis[u]+w:
                    dis[v]=dis[u]+w

                    Enqueue(queue,v)

    print(dis[d])


cost = [ [0, 15, 80, 90],
         [float("inf"), 0, 40, 50],
         [float("inf"), float("inf"), 0, 70],
         [float("inf"), float("inf"), float("inf"), 0]
        ]
findmincost(cost,0,3)