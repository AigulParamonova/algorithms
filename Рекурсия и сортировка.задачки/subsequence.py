"""C. Подпоследовательность. Рекурсия и сортировка.
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки, и нужно понять, является ли первая из них
подпоследовательностью второй. Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.
"""
def subsequence(short_string, long_string):
    position = -1
    for i in short_string:
        position = long_string.find(i, position + 1)
        if position == - 1:
            return False
    return True

if __name__ == '__main__':
    short_string = input()
    long_string = input()
    print(subsequence(short_string, long_string))