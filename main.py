""" Головний модуль задачі
1 Виводить розрахункову табліцю на екран та в файл
2 Виводить первинні данні на екран
"""

import os
from process_data import dohid_val
from data_service import show_dovidnyks, show_tovaroobigs, get_dovidnyk, get_tovaroobig

MAIN_MENU = \
""" 
~~~~~~~~~~   РОЗРАХУНОК ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ   ~~~~~~~~~
1 - Вивід таблиці валового доходу універмагу на екран
2 - Запис таблиці валового доходу універмагу в файл
3 - Вивід списка товарообігу універмагу
4 - Вивід списка довідника товарних груп
0 - Завершення роботи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "ВАЛОВИЙ ДОХІД УНІВЕРМАГУ НА ПОТОЧНИЙ РІК"

HEADER = \
"""
---------------------------------------------------------------------------------------------------------------------
Найменування        |   Рік   |        Товарообіг, тис.грн.        |   Торгова   |     Валовий дохід, тис.грн.
товарної групи      |         |   План1   |  Очіковане виконання1  |  знижка, %  |   План2   |  Очіковане виконання2
---------------------------------------------------------------------------------------------------------------------
"""

FOOTER =  \
'''
----------------------------------------------------------------------------------------------------------------------
'''

STOP_MESSAGE = 'Для продовження натисніть <Enter> '

def show_dohid(dohid_list):
    """ Виводить таблицю валового доходу
    Args:
        dohid_list ([type]): Список доходу
    """
    print(f"\n\n{TITLE:^113}")
    print(HEADER)

    for dohid in dohid_list:
        print(f"{dohid['tovar_name']:20}",
              f"{dohid['year']:^9}",
              f"{dohid['plan1']:^10}",
              f"{dohid['ochikyeme_vukonanya1']:^23}",
              f"{dohid['znijka']:^17}",
              f"{dohid['plan2']:^10}",
              f"{dohid['ochikyeme_vukonanya2']:^21}")

    print(FOOTER)

def write_dohid(dohid_list):
    """ Записує список валового доходу у текстовий файл
    Args:
        dohid_list ([type]): список доходу
    """

    with open('./data/dohid.txt', 'w', encoding="utf8" ) as dohid_file:
        for dohid in dohid_list:
            line = \
               dohid['tovar_name']                + ';' +      \
               str(dohid['year'])                 + ';' +      \
               str(dohid['plan1'])                + ';' +      \
               str(dohid['ochikyeme_vukonanya1']) + ';' +      \
               str(dohid['znijka'])               + ';' +      \
               str(dohid['plan2'])                + ';' +      \
               str(dohid['ochikyeme_vukonanya2']) + '\n' 
               
            dohid_file.write(line)  
            
    print('Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('Програма завершила роботу')
        exit(0)

    elif command_number == '1':
        dohid_list = dohid_val()
        show_dohid(dohid_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        dohid_list = dohid_val()
        write_dohid(dohid_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        tovaroobigs = get_tovaroobig()
        show_tovaroobigs(tovaroobigs)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidnyks = get_dovidnyk()
        show_dovidnyks(dovidnyks)
        input(STOP_MESSAGE)