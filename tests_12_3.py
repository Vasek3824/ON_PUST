import module_12_2
import source
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        t_w = source.Runner('TestRunner')

        for _ in range(10):
            t_w.walk()

        self.assertEqual(t_w.distance, 50)

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        t_r = source.Runner('TestRunner')

        for _ in range(10):
            t_r.run()

        self.assertEqual(t_r.distance, 100)

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        t_w = source.Runner('TestRunner')
        t_r = source.Runner('TestRunner')

        for _ in range(10):
            t_w.walk()
            t_r.run()
        self.assertNotEqual(t_r.distance, t_w.distance)

if __name__ == '__main__':
    unittest.main()


class TournamentTes(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usen = module_12_2.Runner('Усейн', 10)
        self.andres = module_12_2.Runner('Андрей', 9)
        self.nik = module_12_2.Runner('Ник', 3)

    @classmethod

    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print({key: str(value) for key, value in cls.all_results[test].items()})

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tournament = module_12_2.Tournament(90, self.usen, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_andres_nik(self):
        tournament = module_12_2.Tournament(90, self.andres, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)

    @unittest.skipUnless(False, 'Тесты в этом кейсе заморожены')
    def test_usain_andres_nik(self):
        tournament = module_12_2.Tournament(90, self.usen, self.andres, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)
if __name__ == '__main__':
    unittest.main()
