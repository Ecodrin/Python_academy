def secret_replace(text, **keyword):
    decision = ''
    for symbol in text:
        if keyword.get(symbol):
            decision += keyword[symbol][0]
            keyword[symbol] = keyword[symbol][1:]
        else:
            decision += symbol
    return decision



result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)