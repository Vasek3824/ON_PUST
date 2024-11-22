import random
import time
import threading

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            plus = random.randint(50, 500)
            self.balance += plus
            print(f'Пополнение: {plus}. Баланс: {self.balance}')

            time.sleep(0.001)


    def take(self):
        for i in range(100):
            minus = random.randint(50,500)
            print(f'Запрос на {minus}')
            if self.balance >= minus:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



