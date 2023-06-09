

input_word = input("Введите слово: ")
list_letter = list(input_word.upper())
count_bonus = 0
for i in range(len(list_letter)):
    if list_letter[i] == "A" or list_letter[i] == "E" or list_letter[i] == "I" or list_letter[i] == "O" or list_letter[i] == "L" or list_letter[i] == "N" or list_letter[i] == "S" or list_letter[i] == "T" or list_letter[i] == "R" or list_letter[i] == "А" or list_letter[i] == "В" or list_letter[i] == "Е" or list_letter[i] == "И" or list_letter[i] == "Н" or list_letter[i] == "О" or list_letter[i] == "Р" or list_letter[i] == "С" or list_letter[i] == "Т":
        count_bonus += 1
    else:
        if list_letter[i] == "D" or list_letter[i] == "G" or list_letter[i] == "Д" or list_letter[i] == "К" or list_letter[i] == "Л" or list_letter[i] == "М" or list_letter[i] == "П" or list_letter[i] == "У":
            count_bonus += 2
        else:
            if list_letter[i] == "B" or list_letter[i] == "C" or list_letter[i] == "M" or list_letter[i] == "P" or list_letter[i] == "Б" or list_letter[i] == "Г" or list_letter[i] == "Ё" or list_letter[i] == "Ь" or list_letter[i] == "Я":
                count_bonus += 3
            else:
                if list_letter[i] == "F" or list_letter[i] == "H" or list_letter[i] == "V" or list_letter[i] == "W" or list_letter[i] == "Y" or list_letter[i] == "Й" or list_letter[i] == "Ы":
                    count_bonus += 4
                else:
                    if list_letter[i] == "K" or list_letter[i] == "Ж" or list_letter[i] == "З" or list_letter[i] == "Х" or list_letter[i] == "Ц" or list_letter[i] == "Ч":
                        count_bonus += 5
                    else:
                        if list_letter[i] == "J" or list_letter[i] == "X" or list_letter[i] == "Ш" or list_letter[i] == "Э" or list_letter[i] == "Ю":
                            count_bonus += 8
                        else:
                            if list_letter[i] == "Q" or list_letter[i] == "Z" or list_letter[i] == "Ф" or list_letter[i] == "Щ" or list_letter[i] == "Ъ":
                                count_bonus += 10
print(f"Слово {input_word} стоит {count_bonus} баллов")