"""Большое число. Рекурсия и сортировка.
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.
"""
def big_number(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            x = numbers[j] + numbers[j+1]
            y = numbers[j+1] + numbers[j]
            if x < y:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return "".join(numbers)


numbers_length = int(input())
numbers = input().split(' ')
print(big_number(numbers))