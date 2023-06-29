def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

def isvalid(u,v,hash):
    c=0

    for i in range(len(u)):
        if u[i]!=v[i]:
            c+=1

    return c==1 and v not in hash



def findladder(dic,s,end):

    queue=Queue()
    hash=set()
    Enqueue(queue,[s,1])

    while(Size(queue)):
        rem=Dequeue(queue)

        u=rem[0]

        if u==end:
            print(rem[1])
            return

        if u in hash:
            continue

        hash.add(u)

        for x in dic:

            if isvalid(u,x,hash):

                Enqueue(queue,[x,rem[1]+1])


Dic = {'POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN'}
s = 'TOON'
end = 'PLEA'
findladder(Dic,s,end)


Dic = {'ABCD', 'EBAD', 'EBCD', 'XYZA'}
s = 'ABCV'
end = 'EBAD'
findladder(Dic,s,end)





