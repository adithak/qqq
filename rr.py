nm,q= map(int,input().split())
N=[int(i) for i in input().split()]
for _ in range(q):
    u,v=map(int,input().split())
    print(max(N[u-1:v]))
