import multiprocessing
import os
import sys
import timeit
from math import sqrt


def find_primes(limit: int, proc: int) -> None:
    print('Идет работа...')
    primes_list = [False for i in range(limit + 1)]
    sqrt_of_limit = sqrt(limit)
    for i in range(proc, int(sqrt_of_limit + 1), 3):
        for j in range(1, int(sqrt_of_limit + 1)):  # переделать
            x = i * i
            y = j * j
            n = 4 * x + y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                primes_list[n] = True

            n -= x
            if n <= limit and n % 12 == 7:
                primes_list[n] = True

            n -= 2 * y

            if i > j and n <= limit and n % 12 == 11:
                primes_list[n] = True

    for i in range(5, int(sqrt_of_limit + 1)):
        if primes_list[i]:
            number = i * i
            for j in range(number, int(sqrt_of_limit + 1), number):
                primes_list[j] = False
    print('Идет работа...')
    if proc == 1:
        with open('one.txt', "w") as file:
            for x in primes_list:
                string = str(x) + '\n'
                file.write(string)
    elif proc == 2:
        with open('two.txt', "w") as file:
            for x in primes_list:
                string = str(x) + '\n'
                file.write(string)
    else:
        with open('three.txt', "w") as file:
            for x in primes_list:
                string = str(x) + '\n'
                file.write(string)


def write_in_file() -> None:
    print('Идет заключительная часть вычисления...')
    with open('one.txt', 'r') as one:
        first_read = one.read()
        list_1 = first_read.split("\n")
    with open('two.txt', 'r') as two:
        first_read = two.read()
        list_2 = first_read.split("\n")
    with open('three.txt', 'r') as three:
        first_read = three.read()
        list_3 = first_read.split("\n")
    os.remove('one.txt')
    os.remove('two.txt')
    os.remove('three.txt')
    dirty_list = [0] * len(list_1)
    for i in range(0, len(list_1)):
        if list_1[i] == "False":
            list_1_elem = 0
        else:
            list_1_elem = 1
        if list_2[i] == "False":
            list_2_elem = 0
        else:
            list_2_elem = 1
        if list_3[i] == "False":
            list_3_elem = 0
        else:
            list_3_elem = 1
        dirty_list[i] = (list_1_elem + list_2_elem + list_3_elem) % 2
    nums = [0] * len(dirty_list)
    for i in range(len(dirty_list)):
        if dirty_list[i] == 1:
            if i % 5 != 0:
                nums[i] = i
    nums[2] = 2
    nums[3] = 3
    nums[5] = 5
    for i in range(int(len(nums))):
        if nums[i] != 0:
            for j in range(i * i, limit + 1, i * i):
                nums[j] = 0
    print('Осталось совсем чуть-чуть...')
    nums.pop()
    with open('result.txt', 'w') as file:
        file.write('')
        result = ''
        for i in range(len(nums)):
            if nums[i] != 0:
                result += f'{nums[i]}\n'
        file.write(result)


def start(limit: int) -> None:
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(find_primes, iterable=[[limit, 1], [limit, 2], [limit, 3]])
        pool.close()


if __name__ == '__main__':
    try:
        if int(sys.argv[1]) < 0:
            raise Exception
        if int(sys.argv[1]) == 0:
            raise Exception
    except Exception:
        print('Неправильный аргумент')
    except BaseException:
        print('Скрипт завершен\nРезультат в папке с скриптом')
    else:
        limit = int(sys.argv[1])
        start_time = timeit.default_timer()
        start(limit)
        write_in_file()
        print(f'Вычисление длилось: {timeit.default_timer() - start_time} секунд\n')
        print('Скрипт завершен\nРезультат в папке с скриптом')
