
def exp_filter(data, alpha):
    filtered = []
    for i in range(len(data)):
        filtered += [data[0]] if i == 0 else [round(alpha * data[i] + (1 - alpha) * filtered[i-1], 2)]

    return filtered

'Функция `exp_filter()` принимает список данных и параметр альфа, который определяет вес новых значений. '
'Она итерируется по каждому значению в списке данных и выполняет операцию фильтрации экспоненциальным методом.'
' Результат сохраняется в отдельном списке и возвращается после завершения итерации.'

data = [1, 2, 5, 7, 10]
alpha = 0.2
print(exp_filter(data, alpha))