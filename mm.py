l = []
ym=[]
n=int(input("enter:"))
for i in range(1,n+1):
  b=int(input("enter"))
  l.append(b)

  for j in range(1,n+1):
    c=int(input("enter"))
    ym.append(c)
for i in range(1,n+1):
  d=l+ym
  print(d)
print(max(d))
print(l)
print(ym)
