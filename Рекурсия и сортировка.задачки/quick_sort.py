"""B. Эффективная быстрая сортировка. Рекурсия и сортировка финал.
Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров.
Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования
будет определяться победитель.
Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя:
количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.
Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот,
у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.
Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам
реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное
программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять
O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").

Как работает in-place quick sort
Как и в случае обычной быстрой сортировки, которая использует дополнительную память, необходимо выбрать опорный
элемент (англ. pivot), а затем переупорядочить массив. Сделаем так, чтобы сначала шли элементы, не превосходящие
опорного, а затем —– большие опорного.
Затем сортировка вызывается рекурсивно для двух полученных частей. Именно на этапе разделения элементов на
группы в обычном алгоритме используется дополнительная память. Теперь разберёмся, как реализовать этот шаг in-place.
Пусть мы как-то выбрали опорный элемент. Заведём два указателя left и right, которые изначально будут указывать
на левый и правый концы отрезка соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он
указывает на элемент, меньший опорного. Аналогично двигаем правый указатель влево, пока он стоит на элементе,
превосходящем опорный. В итоге окажется, что что левее от left все элементы точно принадлежат первой группе,
а правее от right — второй. Элементы, на которых стоят указатели, нарушают порядок. Поменяем их местами (в большинстве
языков программирования используется функция swap()) и продвинем указатели на следующие элементы.
Будем повторять это действие до тех пор, пока left и right не столкнутся.
На рисунке представлен пример разделения при pivot=5. Указатель left — голубой, right — оранжевый.
"""
def quick_sort_inplace(participants, left, right):
    pivot = participants[(left + right) // 2]
    left_idx = left - 1
    right_idx = right + 1
    while True:
        left_idx += 1
        while participants[left_idx] < pivot:
            left_idx += 1
        right_idx -= 1
        while participants[right_idx] > pivot:
            right_idx -= 1
        if left_idx >= right_idx:
            return right_idx
        participants[left_idx], participants [right_idx] = participants[right_idx], participants[left_idx]

def quick_sort(participants, left, right):
    if left < right:
        middle = quick_sort_inplace(participants, left, right)
        quick_sort(participants, left, middle)
        quick_sort(participants, middle + 1, right)
    return participants
    
def main():
    number_participants = int(input())
    participants = []
    for _ in range(number_participants):
        login, solved_tasks, penalty = input().split()
        participants.append([-int(solved_tasks), int(penalty), login])
    quick_sort(participants, 0, number_participants - 1)
    for participant in participants:
        print(participant[2])    

if __name__ == '__main__':
    main()