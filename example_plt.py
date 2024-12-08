import matplotlib.pyplot as plt

# Демонстрация №1
def histogram(y):
    x = [i for i in range(1, len(y)+1)]
    plt.bar(x, y)
    plt.xlabel('Ось x', fontsize = 10, color = 'b')
    plt.ylabel('Ось y', fontsize = 10, color = 'g')
    plt.title('Это пробная версия графика, где Василий Александрович учился творить гистограмму=)', fontsize = 8, color = 'r')

    return  plt.show()
y=[5, 24, 35, 67, 12]
histogram(y)


# Демонстрация №2
def chart(x, y):

    plt.xlabel('Ось x')
    plt.ylabel('Ось y')
    plt.title('Просто график')
    plt.plot(x, y, color = 'r', linewidth=3, label='Линия №1')
    plt.plot(x1, y1, color = 'g', linewidth=6, label='Линия №2')
    plt.legend()
    plt.show()

x = [10, 30, 14]
y = [5, 34, 4]
x1 = [25, 12, 14]
y1 = [18, 35, 13]

chart(x, y)
