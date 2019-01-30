def main():
    sm = 0
    l = []
    n = int(input())
    for i in range(n):
        l.append(int(input()))
    sub = n // 2
    for i in range(sub):
        sm += l[i]
    sub1 = sm / sub
    sm = 0
    for i in range(sub, n):
        sm += l[i]
    sub2 = sm / (n - sub)
    print(sub1, sub2)
    if sub1 == sub2:
        print('yes')
    else:
        print('no')


main()
