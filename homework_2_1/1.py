def find_mid_letters(word):
    if len(word) % 2 == 0:  # проверка длины строки на четность
        result = "Mid letters are: " + word[len(word) // 2 - 1] + word[len(word) // 2]  # сохраняем последнюю букву первой
    # половины слова и первую букву второй половины
        print(result)
    else:  # если проверка на четность длины не пройдена, переход логики на эту ветку
        result = "Mid letter is: " + word[len(word) // 2]  # сохраняем букву на самой середине слова
        print(result)


any_word = input("Input any word: ")  # запрашиваем слово у пользователя
while not any_word.isalpha():  # цикл while на проверку того, что пользователь вводит именно буквы
    any_word = input("Wrong input, try with only letters: ")

find_mid_letters(any_word)
