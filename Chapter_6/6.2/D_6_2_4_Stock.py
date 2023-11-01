import pandas as pd
from C_6_2_3_Check2 import cheque


def discount(in_cheque: pd.DataFrame):
    new_cheque = in_cheque.copy()
    if len(in_cheque) > 2:
        for i in range(len(new_cheque)):
            if new_cheque.loc[i, "number"] > 2:
                new_cheque.loc[i, "cost"] *= 0.5
    return new_cheque


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
with_discount = discount(result)
print(result)
print(with_discount)
