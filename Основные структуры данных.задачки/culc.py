"""Калькулятор(Основные структуры данных.Финал)
Задание связано с обратной польской нотацией. Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.
"""

OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x // y,
        '*': lambda x, y: x * y
    }

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        raise IndexError('Stack is empty')

def calculator(polish_notation):
    stack = Stack()
    for i in polish_notation:
        if i in OPERATORS:
            a, b = stack.pop(), stack.pop()
            stack.push(OPERATORS[i](b, a))
        else:
            stack.push(int(i))     
    return stack.pop()

if __name__ == '__main__':
    polish_notation = input().split()
    print(calculator(polish_notation))