"""1. Реализовать программу для вывода последовательности
чисел Фибоначчи до определённого числа в последовательности.
Номер числа, до которого нужно выводить, задаётся пользователем
с клавиатуры. Для реализации последовательности использовать
генераторную функцию"""

number = int(input("Введите число : "))
some_generator = (i for i in range(number))
print(some_generator)
fib1 = fib2 = 1
for i in some_generator:
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end= " ")
print()


"""2. Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся пользователем с
клавиатуры."""

n = int(input())
some_generator1 = (i for i in range(n))
print(some_generator1)
for count in some_generator1:
    while count == True:
         print(count, end=" ")


