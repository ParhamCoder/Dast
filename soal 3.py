def number_no (k) :
    n = str(k)
    if '3' in n and '5' in n and '7' in n :
        a = True
        for i in n:
            if i not in ['3', '5', '7']:
                a = False
    else :
        a = False

def count_num (a) :
    count = 0
    for k in range(1, (a+1)):
        if number_no (k) :
            count += 1
        return count

x = int(input())
y = count_num(x)
print(y)
