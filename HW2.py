# 3 Задайте список из n чисел последовательности (1+ 1/n)n и выведите на экран их сумму.
n = int(input())
elem = [round((1+1/n)**n, 2) for n in range(1, n+1)]
print(round(sum(elem), 2))
print(elem)
