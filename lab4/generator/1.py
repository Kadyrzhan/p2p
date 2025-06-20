def generate_squares(n):
    for i in range(n + 1):
        yield i * i

print("1. Квадраты чисел до N:")
for square in generate_squares(5):
    print(square, end=" ")
print("\n")


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print("2. Чётные числа до N (ввод с консоли):")
n = int(input("Введите число: "))
print(", ".join(str(num) for num in even_numbers(n)))
print("\n")


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("3. Числа, делящиеся на 3 и 4 до N:")
for num in divisible_by_3_and_4(50):
    print(num, end=" ")
print("\n")


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print("4. Квадраты чисел от A до B:")
for val in squares(3, 7):
    print(val, end=" ")
print("\n")


def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("5. Обратный отсчёт от N до 0:")
for i in countdown(5):
    print(i, end=" ")