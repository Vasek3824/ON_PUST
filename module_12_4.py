import logging
import unittest
import source

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(levelname)s\%(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        t_w = source.Runner('TestRunner')
        try:
            for _ in range(10):
                t_w.walk()

            self.assertEqual(t_w.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning("Неверная скорость для Runner", e)


    def test_run(self):
        t_r = source.Runner('TestRunner')
        try:
            for _ in range(10):
                t_r.run()
                self.assertEqual(t_r.distance, 100)
                logging.info('"test_run" выполнен успешно')
        except Exception as e:
                logging.warning("Неверный тип данных для объекта Runner", e)


    def test_challenge(self):
        t_w = source.Runner('TestRunner')
        t_r = source.Runner('TestRunner')

        for _ in range(10):
            t_w.walk()
            t_r.run()
        self.assertNotEqual(t_r.distance, t_w.distance)

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',encoding='UTF-8',
                        format='%(levelname)s %(message)s')
    unittest.main()

