# module_2_4.py
# 22.09.2024 Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in numbers:
    is_prime = True
    if n == 1:
        continue
    elif n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
print("Primes: ", primes)
print("Not Primes: ", not_primes)
