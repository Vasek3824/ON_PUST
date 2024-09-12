numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(2, numbers[i]):
        is_primes = True
        if numbers[i] % j == 0:
            is_primes = False
            break
    else:
        is_primes = True
    if is_primes == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(f'primes: {primes}')
print(f'not_primes: {not_primes}')
