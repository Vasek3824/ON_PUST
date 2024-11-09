first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
mix_strings = first_strings + second_strings

first_result = [len(i) for i in first_strings if len(i) >= 5]
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
third_result = {i: len(i) for i in mix_strings if len(i) % 2 == 0}

print(first_result)
print(second_result) #[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result) #{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}