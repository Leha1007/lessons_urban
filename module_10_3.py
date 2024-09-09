import random
import threading
import time


class Bank:

    def __init__(self, balance):
        self.lock = threading.Lock()
        self.balance = balance

    def deposit(self):
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        for _ in range(100):
            rand_count = random.randint(50, 501)
            self.balance = self.balance + rand_count
            print(f'Пополнение: {rand_count}. Баланс: {self.balance}.', end='\n')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            rand_count = random.randint(50, 501)
            print(f'Запрос на: {rand_count}.')
            self.lock.acquire()
            if rand_count <= self.balance:
                self.balance = self.balance - rand_count
                print(f'Снятие: {rand_count}. Баланс: {self.balance}.', end='\n')
            else:
                print('Запрос отклонён, недостаточно средств', end='\n')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank(0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
