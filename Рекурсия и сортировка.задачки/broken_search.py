"""
Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере.
Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала
данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности.
Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за 
O(log n).Можно предполагать, что в массиве только уникальные элементы.

Бинарный поиск в 'сломанном' списке.
    Args:
        nums (List): массив, бывший отсортированным в кольцевой структуре
        target ([type]): искомый эл-т
    Returns:
        int: индекс искомого эл-та, или -1 если не найден
    Алгоритм поиска:
    Массив делится на две части посередине.
    Одна точно должна быть упорядоченна.
    Если часть отсортирована, легко проверяется, входит ли в неё X.
    Итого:
    За left, right берутся индексы первого и последнего эл-тов.
    В цикле пока диапазон не схлопнется:
    Делим на части.
    Проверяем mid == X.
    Если левая сортирована:
        если X входит:
            индексы левой для след. итерации
        иначе:
            индексы правой для след. итерации
    иначе:
        если X входит:
            индексы правой для след. итерации
        иначе:
            индексы левой для след. итерации
    след. итерация
    При сужении диапазона до двух эл-тов, проверка на сортированность
    сравнивает один и тот же эл-т с собой. В условии необходимо '='.
"""

def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
    # левая часть
        if nums[left] <= nums[pivot]:
            if nums[left] <= target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        else:  # правая часть
            if nums[pivot] < target <= nums[right]:
                left = pivot + 1
            else:
                right = pivot - 1
    return -1
    
if __name__ == '__main__':
    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6
