"""Два велосипеда(рекурсия и сортировки)
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка,
в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.
У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.
Ваша задача — по заданной стоимости велосипеда определить  первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).
"""

def binarySearch(cash, bicycle_cost, left, right):
    if right <= left and left != 0: # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if (cash[mid] >= bicycle_cost and (cash[mid - 1] < bicycle_cost or mid == 0)):
        return mid + 1
    elif  bicycle_cost <= cash[mid]: # искомый элемент меньше центрального
        return binarySearch(cash, bicycle_cost, left, mid) # значит следует искать в левой половине
    else: # иначе следует искать в правой половине
        return binarySearch(cash, bicycle_cost, mid + 1, right)

days = int(input())
cash = [int(num) for num in input().split(' ')]
bicycle_cost = int(input())
# изначально мы запускаем двоичный поиск на всей длине массива
print(binarySearch(cash, bicycle_cost, left = 0, right = len(cash)), end=' ')
print(binarySearch(cash, bicycle_cost * 2, left = 0, right = len(cash)), end=' ')
