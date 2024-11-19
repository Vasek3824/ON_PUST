import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self, enemies = 100):
        count = 0
        print(f'{self.name}, на нас напали!')

        while enemies > 0:
            enemies -= self.power

            count += 1
            print(f'{self.name} сражается {count} день(дня)..., осталось {enemies} воинов.')
            if enemies == 0:
                print(f'{self.name} одержал победу спустя {count} дней(дня)!')
            time.sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
