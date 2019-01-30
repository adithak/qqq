num,k = input().split()
num = int(num)
k = int(k)
l = []
(s1,s2) = ([],[])
l = list(map(int,input().split()))
if(num%2!=0):
    s1=l[:num-1]
    s2=l[num-1:num]
else:
    s1=l[:num//2]
    s2=l[num//2:num]
print(max(min(s1),min(s2)))
