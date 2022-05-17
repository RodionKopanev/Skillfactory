def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

array = input('Введите последовательность чисел через пробел: ').split()
sort_array = merge_sort(list(map(int, array)))

while True:
    try:
        element = int(input('Введите число из последовательности: '))
        if element not in sort_array:
            raise Exception
        break
    except Exception:
        print('\n!Ошибка: Число не входит в заданную последовательность!\n')

result = binary_search(sort_array, element, 0, len(sort_array))
print('Отсортированный список:', sort_array)
print(f'Индекс искомого числа: {result - 1}')
