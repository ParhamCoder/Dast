n = str(input())
if '3' and '5' and '7' in n:
    a = True
    for i in n:
        if i not in ['3', '5', '7']:
            a = False
else:
    a = False
print(a)


