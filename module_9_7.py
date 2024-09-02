def is_prime(func):
    def wrapper(count_1, count_2, count_3):
        cou = func(count_1, count_2, count_3)
        is_pr = True
        for i in range(2, cou // 2 + 1):
            if cou % i == 0:
                is_pr = False
                break
        if is_pr:
            print('Простое')
        else:
            print('Составное')
        return cou
    return wrapper


@is_prime
def sum_three(count_1, count_2, count_3):
    return count_1 + count_2 + count_3


result = sum_three(2, 3, 6)
print(result)
