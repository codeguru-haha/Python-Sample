def linePatten(n, m):
    patten =".|."
    print((patten * n).center(m,'-'))

def drawingWindow(n):
    if (n%2==0):
        n+=1
    m=3*n
    for i in range(1,n,2):
        linePatten(i,m)
    print("WELCOME".center(m,'-'))
    for i in range(n-2,0,-2):
        linePatten(i,m)

n = int(input())
drawingWindow(n)
