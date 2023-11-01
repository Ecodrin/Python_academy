import pandas as pd


def length_stats(text: str):
    text = sorted(''.join([i.lower() for i in text if i.isalpha() or i == ' ']).split())
    library = pd.Series({word: len(word) for word in text})
    return library


print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
