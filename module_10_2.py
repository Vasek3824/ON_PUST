import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
    def run(self):
        count = 0
        print(f'{self.name}, на нас напали!')

        while self.enemies > 0:
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            count += 1
            print(f'{self.name} сражается {count} день(дня)..., осталось {self.enemies} воинов.')
            if self.enemies == 0 :
                print(f'{self.name} одержал победу спустя {count} дней(дня)!')

            time.sleep(1)


first_knight = Knight('Sir Lancelot', 11 )
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
