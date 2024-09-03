from threading import Thread
from time import sleep

ending_dict = {1: 'ень', 2: 'ня', 3: 'ня', 4: 'ня'}
first_num = [11, 12, 13, 14]


def ending(days):
    if days in ending_dict.keys():
        return ending_dict[days]
    elif days % 100 in first_num:
        return 'ней'
    elif days % 10 in ending_dict.keys():
        return ending_dict[days % 10]
    else:
        return 'ней'


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            sleep(1)
            enemies -= self.power
            if enemies > 0:
                print(f'{self.name} сражается {days} д{ending(days)}, осталось {enemies} врагов')
            else:
                print(f'{self.name} сражается {days} д{ending(days)}, осталось 0 врагов')
        print(f'{self.name} одержал победу через {days} д{ending(days)}')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
