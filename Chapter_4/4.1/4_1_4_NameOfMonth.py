def month(n, language):
    ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май',
          'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    en = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if language == 'ru':
        return ru[n - 1]
    else:
        return en[n - 1]


print(month(7, 'ru'))