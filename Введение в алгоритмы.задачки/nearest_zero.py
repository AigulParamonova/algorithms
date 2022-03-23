"""Ближайший ноль.Введение в алгоритмы. Финальные задачи
Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
На каждом участке либо уже построен дом, либо участок пустой. Тимофей ищет место для строительства своего дома
Он очень общителен и не хочет жить далеко от других людей, живущих на этой улице.
Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого участка знать расстояние до
ближайшего пустого участка. (Для пустого участка эта величина будет равна нулю –— расстояние до самого себя).
Ваша задача –— помочь Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не
упорядочены. Пустые участки обозначены нулями.
"""

def nearest_zero(house_num):
    zero_dist = 0
    zero_index = None
    for i in range(len(house_num)):
        if house_num[i] != 0 and zero_index is None:
            house_num[i] = len(house_num)
        elif house_num[i] != 0:
            zero_dist += 1
            house_num[i] = zero_dist
        elif house_num[i] == 0:
            zero_dist = 0
            zero_index = i
    for i in range(len(house_num) - 1, -1, -1):
        if i >= zero_index:
            continue
        elif house_num[i] == 0:
            zero_dist = 0
        elif house_num[i] == len(house_num):
            zero_dist += 1
            house_num[i] = zero_dist
        elif house_num[i] != 0:
            house_num[i] = min(house_num[i], house_num[i + 1] + 1)
    return ' '.join(map(str, house_num))


input()
house_num = list(map(int, input().strip().split()))
print(nearest_zero(house_num))