n = str(input())
if '3' and '5' and '7' in n:
    a = True
    for i in n:
        if i not in ['3', '5', '7']:
            a = False
else:
    a = False

x = 0
n = int(n)
for j in range(n):
    j = str(j)
    if '3' and '5' and '7' in j:
        x += 1
        for i in j:
            if i not in ['3', '5', '7']:
                x += 0
    else:
        x += 0
print(x)
