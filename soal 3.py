a = str(input())
k = int(input())
b = a
x = a
y = 0
while not y == k:
    a = str(a)
    b = str(b)
    a = x
    a = sorted(a)
    b = sorted(a)
    b.sort(reverse=True)
    def stringa(a):
        text = ''
        for i in a:
            text = text + str(i)
        return text
    def stringb(b):
        text = ''
        for i in a:
            text = text + str(i)
        return text

    a = stringa(a)
    b = stringb(b)
    a = int(a)
    b = int(b)
    x = b - a




print(x)
