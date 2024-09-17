import queue
import random
import time
from threading import Thread


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 11))


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = queue.Queue()
        self.tables = []
        for table in tables:
            self.tables.append(table)
        self.guests_list = []

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            self.guests_list.append(guest)
            if len([t.number for t in self.tables if None == t.guest]) > 0:
                table_num = random.choice([t.number for t in self.tables if None == t.guest])
                print([t.number for t in self.tables if None == t.guest])
                for t in self.tables:
                    if t.number == table_num:
                        t.guest = guest.name
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table_num}')
            else:

                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while self.queue.empty() or len({t.guest for t in self.tables}) > 1:
            for guest in self.guests_list:
                for t in self.tables:
                    if guest.name == t.guest and guest.is_alive():
                        print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {t.number} свободен')
                        t.guest = None
                        guest.join()
                        if not self.queue.empty():
                            guest_new = self.queue.get()
                            t.guest = guest_new.name
                            print(f'{guest_new.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}')
                            guest_new.start()

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
