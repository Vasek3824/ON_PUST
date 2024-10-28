def custom_write(file_name: str, strings: list):

    strings_positions = {}
    count = 1
    name = open(file_name, 'w', encoding = 'utf-8')
    for string in strings:
        byte = name.tell()
        name.write(f'{string})\n')
        strings_positions[(count, byte)] = string
        count += 1
    name.close()
    return strings_positions

if __name__ == '__main__':
    info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

