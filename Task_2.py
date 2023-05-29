matr1 = [[1, 2, 3],
       [4,5,6],
       [7,8,9]]


matr2 = [[3, 24, 35, 46, 57, 68, 79],
        [4, 55, 56, 67, 78, 79, 80],
        [7, 58, 60, 70, 80, 85, 91],
        [10, 63, 65, 77, 88, 94, 99]]

def search_element(matr, element):

       if matr == [] or len(matr) == 0 or len(matr[0]) == 0:
              print('Введена некорректная матрица')
              return -1

       m = len(matr)
       n = len(matr[0])
       i = 0
       j = n-1
       while i < m and j > -1:
              if matr[i][j] == element:
                     print(f'Элемент {element} найден на позиции [{i+1}, {j+1}]')
                     return -1

              elif matr[i][j] > element:
                     j -= 1

              else:
                     i += 1
       print(f'Элемента {element} не нашлось в матрице.')


search_element(matr1, 2)
search_element(matr1, 7)
search_element(matr1, 12)
search_element(matr2, 2)
search_element(matr2, 70)
search_element(matr2, 100)





