import pandas as pd


def length_stats(text):
    text = sorted(''.join([i.lower() for i in text if i.isalpha() or i == ' ']).split())
    odd = pd.Series({word: len(word) for word in text if len(word) % 2 == 1}, dtype='int64')
    even = pd.Series({word: len(word) for word in text if len(word) % 2 == 0})
    return odd, even


odd, even = length_stats('Мама мыла раму')
print(odd)
print(even)

