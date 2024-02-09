def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
numbers = input("Введите числа: ").split()
numbers = [int(x) for x in numbers]
prime_numbers = filter_prime(numbers)
print("Простые числа из списка: ", prime_numbers)
