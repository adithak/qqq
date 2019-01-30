def army():
    nm = int(input())
    x = int(input())
    y = int(input())
    z = int(input())
    if nm == x + y + z:
        print('none')
    elif nm == x + y:
        print(z)
    elif nm == y + x:
        print(y)
    elif nm == y + z:
        print(x)
    else:
        print('none')


try:
    army()
except:
    print('invalid')
