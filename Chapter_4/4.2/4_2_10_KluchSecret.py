def secret_replace(text, **keyword):
    decision = ''
    for symbol in text:
        if keyword.get(symbol):
            decision += keyword[symbol][0]
            keyword[symbol] = list(keyword[symbol][1:]) + [keyword[symbol][0]]
        else:
            decision += symbol
    return decision



result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))