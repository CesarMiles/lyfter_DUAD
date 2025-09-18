def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == '__main__':
    numbers_list = [1, 4, 6, 7, 13, 9, 67]
    prime_list = [num for num in numbers_list if is_prime(num)]

    print(f'Numeros primos en la lista: {prime_list}')