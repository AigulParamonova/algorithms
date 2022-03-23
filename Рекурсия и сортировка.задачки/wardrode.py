"""G.Гардероб. Рекурсия и сортировка.
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового. Помогите Рите справиться с
этой задачей.
Примечание: попробуйте решить задачу за один проход по массиву!
"""
def wardrobe(color_array):
    counted_values = [0] * 3
    for value in color_array:
        counted_values[value] += 1
    return [0] * counted_values[0] + [1] * counted_values[1] + [2] * counted_values[2]

clothes_number = int(input())
color_array = list(map(int, input().strip().split()))
print(*wardrobe(color_array))