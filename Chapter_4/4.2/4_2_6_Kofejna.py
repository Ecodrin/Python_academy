def order(*wishes):
    global in_stock
    for drink in wishes:
        if drink == 'Эспрессо' and in_stock['coffee'] >= 1:
            in_stock['coffee'] -= 1
            return 'Эспрессо'
        if drink == 'Капучино' and in_stock['coffee'] >= 1 and in_stock['milk'] >= 3:
            in_stock['coffee'] -= 1
            in_stock['milk'] -= 3
            return 'Капучино'
        if drink == 'Макиато' and in_stock['coffee'] >= 2 and in_stock['milk'] >= 1:
            in_stock['coffee'] -= 2
            in_stock['milk'] -= 1
            return 'Макиато'
        if drink == 'Кофе по-венски' and in_stock['coffee'] >= 1 and in_stock['cream'] >= 2:
            in_stock['coffee'] -= 1
            in_stock['cream'] -= 2
            return 'Кофе по-венски'
        if drink == 'Латте Макиато' and in_stock['coffee'] >= 1 and in_stock['milk'] >= 2\
                and in_stock['cream'] >= 1:
            in_stock['coffee'] -= 1
            in_stock['milk'] -= 2
            in_stock['cream'] -= 1
            return 'Латте Макиато'
        if drink == 'Кон Панна' and in_stock['coffee'] >= 1 and in_stock['cream'] >= 1:
            in_stock['coffee'] -= 1
            in_stock['cream'] -= 1
            return 'Кон Панна'
    return 'К сожалению, не можем предложить Вам напиток'


in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))