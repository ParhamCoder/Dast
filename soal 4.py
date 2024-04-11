a = 0
b = 0
x = 0
while not x == -1:
    x = int(input())
    if not x == -1:
        if x % 2 == 0:
            a += 1
        else:
            b += 1
if a > b :
    print('even')
elif b > a :
    print('odd')
else :
    print('equal')
