"""формування заявок на розрахунок валового доходу по магазину
"""
# підключити функції з модуля `data_service`
from data_service import get_tovaroobig, get_dovidnyk

dohid = {
    'tovar_name'   : '',                 # назва товарної группи
    'year'   : 0,                        # рік
    'plan1'  : 0,                        # план 1
    'plan2'  : 0,                        # план 2
    'ochikyeme_vukonanya1'   : 0,        # кількість1
    'ochikyeme_vukonanya2'   : 0,        # кількість2
    'znijka'         : 0.0,              # знижка

}

tovaroobigs = get_tovaroobig()
dovidnyks = get_dovidnyk()

def dohid_val():
    """ Формування валового доходу універмагу
    """

    def get_dovidnyk_name(dovidnyk_code):
        """ Повертає назву засоба по його коду
        Args:
            dovidnyk_name ([type]): код засоба
        Returns:
            [type]: назва засобу
        """

        for dovidnyk in dovidnyks:
            if dovidnyk[0] == dovidnyk_code:
                return dovidnyk[1]

        return "*** Код не знайдений"
    
    def get_dovidnyk_znijka(dovidnyk_znijka):
        """ Повертає скидку товару по його коду
        Args:
            dovidnyk_znijka ([type]): код засоба
        Returns:
            [type]: скидка товару
        """

        for dovidnyk in dovidnyks:
            if dovidnyk[0] == dovidnyk_znijka:
                return dovidnyk[2]

        return "*** Код не знайдений"

    # Накопичувач валового доходу універмагу
    dohid_list = []

    for tovaroobig in tovaroobigs:

        # Створити копію шаблона
        dohid_tmp = dohid.copy()

        dohid_tmp['year'] = tovaroobig[3]
        dohid_tmp['plan1'] = tovaroobig[1]
        dohid_tmp['ochikyeme_vukonanya1'] = tovaroobig[2]
        dohid_tmp['tovar_name'] = get_dovidnyk_name(tovaroobig[0])
        dohid_tmp['znijka'] = get_dovidnyk_znijka(tovaroobig[0])
        dohid_tmp['plan2'] = float(dohid_tmp['plan1']) * float(dohid_tmp['znijka']) 
        dohid_tmp['ochikyeme_vukonanya2'] = float(dohid_tmp['ochikyeme_vukonanya1']) * float(dohid_tmp['znijka'])

        dohid_list.append(dohid_tmp)

    return dohid_list

result = dohid_val()

for r in result:
    print(r)