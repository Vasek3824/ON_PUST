import module_12_2
import unittest

class TournamentTes(unittest.TestCase):

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

    def test_usain_nik(self):
        tournament = module_12_2.Tournament(90, self.usen, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)

    def test_andres_nik(self):
        tournament = module_12_2.Tournament(90, self.andres, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)

    def test_usain_andres_nik(self):
        tournament = module_12_2.Tournament(90, self.usen, self.andres, self.nik)
        result = tournament.start()
        TournamentTes.all_results[self._testMethodName] = result
        self.assertTrue(list(result.values())[-1], self.nik.name)
if __name__ == '__main__':
    unittest.main()





