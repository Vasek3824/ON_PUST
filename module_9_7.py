def is_prime(func):
    def wrapper(*args):
        flag =  True
        sum_ = func(*args)
        for i in range(2, sum_):
            if sum_ % i ==0:
                flag = False
                break
        if flag == False:
            print('Составное')
        else:
            print('Простое')
        return sum_
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)