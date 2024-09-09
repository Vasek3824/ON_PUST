grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# сортируем множество по алфавиту
students_s = sorted(students)

# вычесляем средний бал каждой группы оценок
grades_g = [sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]

# выводим результат преобразовав список в словарь, изночально разбив два списка по парам по интексам
print(dict(zip(students_s, grades_g)))
