def moghadas(num):
    num1 = str(num)
    if '3' in num1 and '5' in num1 and '7' in num1:
        for i in num1:
            if i not in ['3', '5', '7']:
                return False
        return True

def shomaresh(n):
    x = 0
    for i in range(1, n+1):
        if moghadas(i):
            x += 1
    return x

n = int(input())
result = shomaresh(n)
print(result)
