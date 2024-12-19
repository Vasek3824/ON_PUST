import source
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        t_w = source.Runner('TestRunner')

        for _ in range(10):
            t_w.walk()

        self.assertEqual(t_w.distance, 100)

    def test_run(self):
        t_r = source.Runner('TestRunner')

        for _ in range(10):
            t_r.run()

        self.assertEqual(t_r.distance, 100)

    def test_challenge(self):
        t_w = source.Runner('TestRunner')
        t_r = source.Runner('TestRunner')

        for _ in range(10):
            t_w.walk()
            t_r.run()
        self.assertNotEqual(t_r.distance, t_w.distance)

if __name__ == '__main__':
    unittest.main()

