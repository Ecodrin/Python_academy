string = 'Яндекс использует Python во многих проектах'
print(sorted(string.split(), key=lambda x: (len(x), x.lower())))
