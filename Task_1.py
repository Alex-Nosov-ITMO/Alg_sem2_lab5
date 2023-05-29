def check_winner(game):
    # Проверяем горизонтальные линии
    for row in game:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Проверяем вертикальные линии
    for column in range(3):
        if game[0][column] == game[1][column] == game[2][column] != ' ':
            return game[0][column]

    # Проверяем диагонали
    if game[0][0] == game[1][1] ==game[2][2] != ' ':
        return game[0][0]

    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return game[0][2]

    # Ничья
    if all(game[row][column] != ' ' for row in range(3) for column in range(3)):
        return 'Ничья'

    # Игра не завершена
    return None

# Пример использования
game1 = [
    ['O', 'O', 'O'],
    [' ', 'X', 'O'],
    [' ', 'X', 'X']
]
'''
game2 = [
    ['O', ' ', 'O'],
    [' ', 'X', 'O'],
    [' ', 'X', 'X']
]

game3 = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['O', 'X', 'X']
]

game4 = [
    ['O', 'X', 'O'],
    ['X', 'X', 'O'],
    ['O', 'O', 'X']
]
'''
winner = check_winner(game1)
if winner:
    print('Победитель:', winner)
else:
    print('Игра не завершена')
  