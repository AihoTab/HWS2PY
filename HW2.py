# 5 Реализуйте алгоритм перемешивания списка.
import random
lst = [random.randint(0, 99) for i in range(random.randint(5, 15))]
print(lst)
random.shuffle(lst)
print(lst)
