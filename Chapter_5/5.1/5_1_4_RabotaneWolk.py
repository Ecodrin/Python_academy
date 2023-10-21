class Programmer:

    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.count_hour = 0
        self.money = 0
        self.salary = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def work(self, time):
        self.count_hour += time
        self.money += self.salary[self.post] * time

    def rise(self):
        posts = ['Junior', 'Middle', 'Senior']
        if self.post != 'Senior':
            self.post = posts[posts.index(self.post) + 1]
        else:
            self.salary[self.post] += 1

    def info(self):
        return f'{self.name} {self.count_hour}ч. {self.money}тгр.'


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
