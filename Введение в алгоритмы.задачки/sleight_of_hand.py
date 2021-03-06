""" Ловкость рук.Введение в алгоритмы. Финальные задачи
Гоша и Тимофей нашли необычный тренажёр для скоростной печати и хотят освоить его.
Тренажёр представляет собой поле из клавиш 4× 4, в котором на каждом раунде появляется конфигурация цифр и
точек. На клавише написана либо точка, либо цифра от 1 до 9. В момент времени t игрок должен одновременно
нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k
клавиш каждый. Если в момент времени t были нажаты все нужные клавиши, то игроки получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.
"""

def sleight_of_hand(number, trainer):
    symbol = []
    for i in range(4):
        for j in trainer[i]:
            if j == '.':
                continue
            symbol.append(int(j))
    entry = 2 * number
    score = sum(0 < symbol.count(num) <= entry for num in range(1,10))
    return score

number = int(input())
trainer = [str(input()) for i in range(4)]
print(sleight_of_hand(number, trainer))