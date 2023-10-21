class RedButton:

    def __init__(self, count_k=0):
        self.count_k = count_k

    def count(self):
        return self.count_k

    def click(self):
        self.count_k += 1
        print('Тревога!')


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
