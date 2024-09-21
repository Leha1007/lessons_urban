import multiprocessing
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            read_line = f.readline()
            all_data.append(read_line)
            if not read_line:
                break


file_names = []

for i in range(1, 5):
    file_names.append(f'file {i}.txt')

if __name__ == '__main__':
    t_start = time()

    #for name in file_names:
        #read_info(name)

    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, file_names)

    t_end = time()
    print(t_end - t_start)
