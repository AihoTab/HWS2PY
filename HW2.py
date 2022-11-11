# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Это не работает!!!

n = int(input())
num = range(-n, n+1)

with open('file.txt') as data:
    line = data.read()

prod = 1
for i in num:
    prod *= num[i]
print(prod)
print(num)
