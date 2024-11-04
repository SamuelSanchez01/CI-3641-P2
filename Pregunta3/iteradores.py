def suspenso(a, b):
    if b == []:
        yield a
    else:
        yield a + b[0]
        for x in suspenso(b[0], b[1:]):
            yield x

X,Y,Z = 0,9,3
print("suspenso")
for x in suspenso(X + Y + Z, [X, Y, Z]):
    print(x)


def misterio(n):
    if n == 0:
        yield [1]
    else:
        for x in misterio(n-1):
            r = []
            for y in suspenso(0, x):
                r = [*r, y]
            yield r

print("misterio")
for x in misterio(5):
    print(x)