'''Для решения этой задачи можно воспользоваться алгоритмом "Сортировка подсчётом".

Алгоритм:
1. Находим максимальный элемент в массиве.
2. Создаём массив "подсчёта" размером в максимальный элемент.
3. Проходим по массиву и для каждого элемента увеличиваем соответствующий элемент в массиве "подсчёта".
4. Проходим по массиву "подсчёта" и ищем первый элемент, равный 0.
Его индекс + 1 будет наименьшим пропущенным числом.
5. Если все элементы в массиве "подсчёта" не равны 0, значит, пропущенных чисел нет.
Возвращаем максимальный элемент + 1.
'''



def find_missing_number(arr):
    # находим максимальный элемент
    max_num = max(arr)

    # создаём массив "подсчёта"
    counts = [0] * max_num

    # заполняем "подсчёт"
    for num in arr:
        print(num - 1)
        counts[num - 1] += 1


    # ищем пропущенное число
    answer = 1
    for count in counts:
        if count == 0:
            return answer
        answer += 1

    # если все числа присутствуют
    return max_num + 1


''' Алгоритм работает за время O(n), так как проходим по массиву всего два раза.
первый раз для нахождения максимального элемента, второй раз для заполнения массива "подсчёта".
Поиск пропущенного числа в "подсчёте" также выполняется за O(n).
'''

testArr = [3, -1, 4, 0, 1, 5]
print(find_missing_number(testArr))