import pandas as pd


def cheque(price: pd.Series, **kwargs):
    table_list = {"product": [], "price": [], "number": [], "cost": []}
    for product, number in sorted(kwargs.items(), key=lambda x: x[0]):
        table_list["product"].append(product)
        table_list["price"].append(price[product])
        table_list["number"].append(number)
        table_list["cost"].append(number * price[product])
    return pd.DataFrame(table_list)
