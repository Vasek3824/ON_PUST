from multiprocessing import Pool
import threading
import time
import glob

def read_info(name):
    all_data = []
    for file in glob.glob(r'c:\Users\Dns\Documents\Python_proekt\pythonProject\files\*txt'):
        with open(file, 'r') as f:
            line = f.readline()
            if not line:
                break
            all_data.append(line)


filename = [f'./file{number}.txt' for number in range(1, 5)]

#if __name__ == '__main__':
 #   start = time.time()
  #  for i in filename:
   #     thread1 = threading.Thread(target=read_info, args=(len(i),))
    #    thread1.start()
    #print(time.time() - start, 'линейный')

if __name__ == '__main__':
    start = time.time()
    with Pool(processes=1) as pool:
        pool.map(read_info, filename)
    print(time.time() - start, 'многопроцессный')

