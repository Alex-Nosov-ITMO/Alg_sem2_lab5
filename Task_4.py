n = int(input('Введите количество ступенек в лестнице: '))

def count_options(quantity):
    save_quantity = [0] * 1000000
    for i in range(0, quantity+1):
        if i == 0 or i == 1:
            save_quantity[0] = 1
            save_quantity[1] = 1

        elif i == 2:
            save_quantity[2] = 2

        else:
            save_quantity[i] = save_quantity[i-1] + save_quantity[i-2] + save_quantity[i-3]

    return save_quantity[quantity]

print(f'Ребенок может подняться по лестнице, в которой {n} ступеней, {count_options(n)} способами!')
