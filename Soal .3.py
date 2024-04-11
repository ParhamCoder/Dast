a, b, c = map(float, input().split())
if a == b == c:
    print("Motesaviolazla")
elif a == b or a == c or b == c:
    print("Motesaviossagheyn")
else:
    print("Mokhtalefolazla")