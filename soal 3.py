a = str(input())
k = int(input())
a = sorted(a)
b = sorted(a)
b.sort(reverse=True)
# def stringa(a):
#     text = ''
#     for i in a:
#         text = text + str(i)
#     return text
# def stringb(b):
#     text = ''
#     for i in b:
#         text = text + str(i)
#     return text


for j in range(1, (k+1)) :
    v = a - b

