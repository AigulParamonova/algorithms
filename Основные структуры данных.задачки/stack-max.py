"""Cтек-Max(Основные структуры данных)
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().
Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000.
В следующих n строках идут команды. Команды могут быть следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».
"""

class StackMax:
    def __init__(self):
        self.items = []
        self.max = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items)-1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items)-1])
        self.items.append(item)
def pop(self):
    if self.isEmpty():
        return 'error'
    self.max.pop()
    return self.items.pop()
def get_max(self):
    if self.isEmpty():
        return 'None'
    return self.max[len(self.items) - 1]    
s = StackMax()
n = int(input())
result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        s.push(command[1])
    if command[0] == 'pop':
        if pop(s) == 'error':
            result.append('error')
    if command[0] == 'get_max':
        result.append(get_max(s))
for i in result:
    print(i)
         