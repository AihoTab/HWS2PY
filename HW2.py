# 5 Реализуйте алгоритм перемешивания списка.
import random
lst = [random.randint(0, 99) for i in range(random.randint(5, 15))]
print(lst)
random.shuffle(lst)
print(lst)

# Решение Анатолия
# i = [int(x) for x in input().split()]
# for j, item in enumerate(i):
#     if item % 2 == 0 and j > 0:
#         i[j], i[j-1] = i[j-1], i[j]
#     elif item % 2 != 0 and j < len(i)-1:
#         i[j], i[j+1] = i[j+1], i[j]
# print(*i, sep=" ", end=" ")
