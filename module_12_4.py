import logging
import unittest
from Python_proekt.pythonProject.Module_12.Module_12_1.source import Runner

logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    try:
        logging.info('"test_walk" выполнен успешно')
        runner = Runner("man", -6)
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    except:
        logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner1 = Runner(213, 3)
            for i in range(10):
                runner1.run()
            self.assertEqual(runner1.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == "__main__":
    unittest.main()
