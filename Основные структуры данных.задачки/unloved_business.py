"""Нелюбимое дело(Основные структуры данных)

Вася размышляет, что ему можно не делать из того списка дел, который он составил.
Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка
и номер удаляемого дела и возвращает голову обновлённого списка.
"""

# Comment it before submitting
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def get_node_by_index(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node

def solution(node, idx):
    if idx == 0:
        node = node.next_item
    else:
        previous_node = get_node_by_index(node, idx-1)
        next_node = get_node_by_index(node, idx+1)
        previous_node.next_item = next_node
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    # result is node0 -> node2 -> node3