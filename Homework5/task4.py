# 4. Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


fib_gen = fibonacci_generator(int(input((f"Введите количество чисел последовательности, которое нужно вывести: "))))
print(fib_gen)


