import time
import  threading

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
        time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

time_ = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_1 = time.time()
print(time_1 - time_)

time_2 = time.time()

threa = []
threa.append(threading.Thread(target=write_words, args = (10, 'example5.txt')))
threa.append(threading.Thread(target=write_words, args = (20, 'example6.txt')))
threa.append(threading.Thread(target=write_words, args = (200, 'example7.txt')))
threa.append(threading.Thread(target=write_words, args = (100, 'example8.txt')))

for th in threa:
    th.start()
for th in threa:
    th.join()
time_3 = time.time()
print(time_3 - time_2)
