class Masters:
    def __init__(self, team1_num, score_1, team1_time):
        self.team1_num = team1_num
        self.score_1 = score_1
        self.team1_time = team1_time

class Wizards():
    def __init__(self, team2_num, score_2, team2_time):
        self.team2_num = team2_num
        self.score_2 = score_2
        self.team2_time = team2_time

class Results(Masters, Wizards):
    def __init__(self, team1_num, score_1, team1_time, team2_num, score_2, team2_time):
        Masters.__init__(self, team1_num, score_1, team1_time)
        Wizards.__init__(self, team2_num, score_2, team2_time)

    def win(self):
        if self.score_1 > self.score_2 or self.score_1 == self.score_2 and self.team1_time > self.team2_time:
            return 'Победа команды Мастера кода!'
        elif self.score_1 < self.score_2 or self.score_1 == self.score_2 and self.team1_time < self.team2_time:
            return 'Победа команды Волшебники Данных!'
        else:
            return 'Ничья!'

    def tasks_total(self):
       return self.score_1 + self.score_2

    def time_avg(self):
        return (self.team1_time + self.team2_time) / 82




master = Masters( team1_num = 5, score_1=40, team1_time = 1552.512)
wizard = Wizards(team2_num = 6, score_2=42, team2_time = 2153.31451)
results = Results(team1_num=master.team1_num, score_1=master.score_1, team1_time=master.team1_time,
                  team2_num=wizard.team2_num, score_2=wizard.score_2, team2_time=wizard.team2_time)
print('В команде Мастера кода участников: %s' % master.team1_num)
print('Итого сегодня в командах участников: %(master)s и %(wizird)s' % {'master': master.team1_num,
'wizird': wizard.team2_num})
print('Команда Волшебники данных решила задач: {}!'.format(wizard.score_2))
print('Волшебники данных решили задачи за {} с.!'.format(wizard.team2_time))
print(f'Команды решили {master.score_1} и {wizard.score_2} задач.')
print(f'Сегодня было решено {results.tasks_total()} задач,'
      f' в среднем по {round(results.time_avg(), 1)} секунды на задачу!')
print(f'Результат битвы: {results.win()}')
