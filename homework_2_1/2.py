'''
Метод sort_names сортирует список имен пузырьковой сортировкой (но это не точно)
'''
def sort_names(names):
    counter = len(names) - 2  # счетчик попарных сравнений для каждой итерации, каждая итерация уменьшает счетчик на 1
    while counter > 0:
        for i in range(counter):
            if names[i] < names[i + 1]:  # если первый элемент меньше второго, то переходим к следу
                continue
            else:
                names[i], names[i + 1] = names[i + 1], names[i]
        counter -= 1

    print("Sorted names: ", names)
    return names

'''
Метод find find_pair_for_everyone создает пары, если количество парней и девушек одинаковое
в ином случае выводит предупреждение в консоль
'''
def find_pair_for_everyone(list_1, list_2):
    if len(list_1) != len(list_2):  # если число парней и девушек не совпадает
        print("Внимание, кто-то может остаться без пары!")  # выводим предупреждение
    else:  # в ином случае печатаем пары в консоль
        pairs = zip(list_1, list_2)
        print("Идеальные пары:")
        for pair in pairs:
            print(pair[0] + " and " + pair[1])

# список парней и девушек для успешного сценария
#list_of_boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
#list_of_girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

# список парней и девушек для НЕ успешного сценария
list_of_boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
list_of_girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

find_pair_for_everyone(sort_names(list_of_girls), sort_names(list_of_boys))
