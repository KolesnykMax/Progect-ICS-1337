"""формування заявок на устаткування по магазину
"""

# підключити функції з модуля `data_service`
from data_service import get_clients, get_orders

# структура накопичувача записів вихідних даних
zajavka = {

    'oborud_name'   : '',    # назва устаткування   
    'client_name'   : '',    # назва клієнта
    'order_number'  : '',    # номер заказу
    'kol'           : 0,     # кількість
    'price'         : 0.0,   # ціна
    'total'         : 0.0    # сума
}


orders = get_orders()
clients = get_clients()

def create_zajavka():
    """формування заявок на устаткування
    """
    def get_client_name(client_code):
        """повертає назву клієнта по його коду

        Args:
            client_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """

        for client in clients:
            if client[0] == client_code:
                return client[1]

        return "*** код клієнта не знайдений"
    
    
    
    # накопичувач заявок 
    zajavka_list = []

    for order in orders:
        
        # створити копію шаблона
        zajavka_tmp = zajavka.copy()

        zajavka_tmp['oborud_name']    = order[2]
        zajavka_tmp['order_number']   = order[1]
        zajavka_tmp['kol']            = order[3]
        zajavka_tmp['price']          = order[4]
        zajavka_tmp['total']          = zajavka_tmp['kol'] * zajavka_tmp['price']
        zajavka_tmp['client_name'] = get_client_name(order[0])

        zajavka_list.append(zajavka_tmp)

    return zajavka_list

result = create_zajavka()

for r in result:
    print(r)

