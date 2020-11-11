""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_dovidnyk():
    """ Повертає вміст файла "dovidnyk.txt" у вигляді списка
    Returns:
        move_mean_list - список рядків файла
    """

    with open('./data/dovidnyk.txt', encoding="utf8") as dovidnyk_file:
        dovidnyk_list = dovidnyk_file.readlines()

    # Накопичувач руху основних засобів
    dovidnyk_drive = []

    for line in dovidnyk_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # Видаляє '\n' в кінці
        dovidnyk_drive.append(line_list)


    return dovidnyk_drive


def show_dovidnyks(dovidnyks):
    """ Виводить список руху основних засобів
    Args:
        dovidnyk (list): список руху основних засобів
    """

    # Задати інтервал виводу
    dovidnyk_code_from = input("З якого кода товару виводити?")
    dovidnyk_code_to = input("По який код товару виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnyk in dovidnyks:
        if dovidnyk_code_from <= dovidnyk[0] <= dovidnyk_code_to:
            print("Код: {:6} Товар: {:17} Знижка: {:5}".format(dovidnyk[0], dovidnyk[1], dovidnyk[2]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товару нічого не знайдено.")


dovidnyks = get_dovidnyk()
show_dovidnyks(dovidnyks)

def get_tovaroobig():
    """ Повертає вміст файла "tovaroobigs.txt" у вигляді списка
    Returns:
        tovaroobig_list - список рядків файла
    """

    with open('./data/tovaroobig.txt') as tovaroobig_file:
        tovaroobig_list = tovaroobig_file.readlines()

    # Накопичувач довідника основних засобів
    tovaroobig_drive = []

    for line in tovaroobig_list:
        line_list = line.split(';')
        line_list[3] = line_list[3][:-1]
        tovaroobig_drive.append(line_list)


    return tovaroobig_drive


def show_tovaroobigs(tovaroobigs):
    """ Виводить список довідника
    Args:
        tovaroobigs (list): список довідника
    """

    # Задати інтервал виводу
    tovaroobig_code_from = input("З якого кода довідника виводити?")
    tovaroobig_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for tovaroobig in tovaroobigs:
        if tovaroobig_code_from <= tovaroobig[0] <= tovaroobig_code_to:
            print("Код: {:6} Вид: {:6} Код: {:6} Вид: {:6}".format(tovaroobig[0], tovaroobig[1], tovaroobig[2], tovaroobig[3]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товарообігу нічого не знайдено.")


tovaroobigs = get_tovaroobig()
show_tovaroobigs(tovaroobigs)
