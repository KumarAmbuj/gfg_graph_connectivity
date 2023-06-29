def isvalid(x,y,vis,m,n,arr):
    return x>=0 and x<m and y>=0 and y<n and arr[x][y]==1 and vis[x][y]==False

def dfs(i,j,vis,m,n,arr):
    vis[i][j]=True
    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    col = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        x=i+row[k]
        y=j+col[k]

        if isvalid(x,y,vis,m,n,arr):
            dfs(x,y,vis,m,n,arr)


def islands(arr):
    m=len(arr)
    n=len(arr[0])

    vis=[[False for i in range(n)] for j in range(m)]
    count=0
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1 and vis[i][j]==False:
                dfs(i,j,vis,m,n,arr)
                count+=1

    print(count)


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
islands(graph)

