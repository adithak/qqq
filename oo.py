sr=str(input())
for x in range(1,len(sr)):
    if sr[x:]>sr:
        print(sr[x:])
        break
