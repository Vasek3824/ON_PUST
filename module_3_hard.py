
def sum_lines(data_structure):
    total_sum = 0

    if isinstance(data_structure, (int, float)):
        total_sum += data_structure
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_part= sum_lines(key)
            total_sum += sum_part
            sum_part = sum_lines(value)
            total_sum += sum_part
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            sum_part = sum_lines(i)
            total_sum += sum_part


    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum = sum_lines(data_structure)
print(total_sum)
