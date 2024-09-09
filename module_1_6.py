my_dict = {'Василий': 1989, 'Вася': 2013, 'Ярик': 2015}
print(my_dict)
print(my_dict.get('Марина'))
my_dict.update({'Тася': 2023, 'Марина': 1985})
pop_ = my_dict.pop('Василий')
print(pop_)
print(my_dict)

my_set = {1, 'book', 1, 45, 'mir', 'book'}
print(my_set)
my_set.update({23, 'май'})
my_set.discard('book')
print(my_set)