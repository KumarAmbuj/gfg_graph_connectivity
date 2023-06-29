def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)

def fun(s):
    sk1 = Stack()
    sk2 = Stack()
    i = 0
    while (i < len(s)):
        if s[i].isdigit():
            x=''
            while(s[i].isdigit()):
                x=x+s[i]
                i+=1

            i-=1

            Push(sk1,int(x))

        elif s[i]=='[':
            Push(sk2,s[i])
        elif s[i]==']':
            x=''
            z=Pop(sk2)
            while(z!='['):
                x=z+x
                z=Pop(sk2)
            n=1
            if Size(sk1):
                n = Pop(sk1)
            res=n*x
            Push(sk2,res)
        else:
            Push(sk2,s[i])
        i+=1
    res=''
    while(Size(sk2)):
        x=Pop(sk2)
        res=x+res
    return res





s="10[a]2[bc]"
print(fun(s))


