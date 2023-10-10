def merge(a, b):
    s = list(a + b)
    for i in range(1, len(s)):
        for j in range(len(s)):
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
    return tuple(s)


print(merge((7, 12), (1, 9, 50)))