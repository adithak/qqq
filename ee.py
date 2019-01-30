sm=input("enter the string")
sm1=""
sm2=""
c=0
b=0
j=len(s1)-1
sm.strip()
sm1.strip()
sm2.strip()
for i in range(len(s)):
    for j in range(i+2,len(s)):
        if sm[i]==sm[j]:
            sm1=sm[i:j+1:]
            sm2=sm1[::-1]
            if sm1==sm2:
                b=1
                break
    if b==1:
        break
    else:
        pass
if b==1:
    print(len(sm)-len(sm1))
else:
    print(len(sm))
