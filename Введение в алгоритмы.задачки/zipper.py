"""Застёжка-молния(Пробные задачи по алгоритмам)

Даны два массива чисел длины n. Составьте из них один массив длины 2n,
в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён.
"""
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
for i in zip(a, b):
    print(*i, end=' ')
