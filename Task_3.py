def is_safe(board, row, col):
    # Проверить ряд по горизонтали слева от ферзя.
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Проверить левую верхнюю диагональ выше ферзя.
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Проверить левую нижнюю диагональ ниже ферзя.
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col, solutions):
    # Все ферзи оказались расставлены успешно, добавить решение в список.
    if col == 8:
        solutions.append([row[:] for row in board])
        return

    # Попробовать рассчитать расстановку ферзей для каждой строки сверху вниз.
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1, solutions)
            board[i][col] = 0


board = [[0 for _ in range(8)] for _ in range(8)]
solutions = []
solve(board, 0, solutions)

print(f'Всего найдено {len(solutions)} возможных расстановок ферзей.')
for i, solution in enumerate(solutions):
    print(f'Решение {i + 1}:')
    for row in solution:
        print(row)


'''В этом коде функция is_safe() проверяет, можно ли установить ферзя в указанной строке и столбце без нарушения правил. Если нет, то ферзь не устанавливается.
Функция solve() использует рекурсию для расстановки ферзей на каждую горизонтальную линию, начиная с первой и двигаясь по порядку слева направо. 
Если ферзь можно установить на текущей горизонтали и столбце, то он устанавливается на доске и рекурсивный поиск продолжается для следующего столбца. 
Если ферзь невозможно установить, то функция возвращает False.
Когда все ферзи успешно расставлены, функция solve() добавляет решение в список решений. 
В конце скрипта мы выводим количество найденных решений и каждое решение в отдельности.'''