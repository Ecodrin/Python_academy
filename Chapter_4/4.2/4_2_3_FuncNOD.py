def gcd(*args):
    s = list(args)
    i = 1
    while i < len(s):
        a = s[i - 1]
        b = s[i]
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        s[i] = a
        del s[i - 1]
    i += 1
    return s[0]


print(gcd(36, 48, 156, 100500))