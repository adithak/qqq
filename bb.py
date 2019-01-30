m=int(input("Enter a count value:"))
b=[]
sum=0
sum1=0
for x in range(n):
	i=int(input())
	a.append(i)
for x in range(0,m,2):
	sum=sum+b[x]
for x in range(1,m,2):
	sum1=sum1+b[x]
print(max(sum,sum1))
