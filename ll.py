nm,p,q,r=input().split()
nm=int(nm)
p=int(p)
q=int(q)
r=int(r)
l=[]
max=-1
l=list(map(int,input().split()))
l.sort()
for i in range(nm):
	for j in range(nm):
            for k in range(nm):
                sum=(p*l[i])+(q*l[j])+(r*l[k])
                if max<sum:
                        max=sum
print(sum)

