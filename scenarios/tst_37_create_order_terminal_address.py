from list_of_tst import *


def create_order_terminal_address(params):
    description = 'Тест №37 - Создание заказа Терминал --> Адрес'

    """Берем рандомно два неповторяющихся города из списка"""
    dispatch_city, destination_city = choice_cities(cities)

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        """Переходим на страницу оформления заказа"""
        find_el(params, btn_new_order.xpath)
        click(params)
        wait_page(params, url_base_dev_order_create)
        price_to_load(params)

        """Заполняем 'Отправка'"""
        find_el(params, input_dispatch_city.xpath)
        click(params)

        set_dispatch_city(params, dispatch_city)

        find_el(params, btn_dispatch_terminal.xpath)
        click(params)
        price_to_load(params)

        """Заполняем 'Прибытие'"""
        find_el(params, input_destination_city.xpath)
        click(params)

        set_destination_city(params, destination_city)

        find_el(params, btn_destination_terminal.xpath)
        click(params)
        price_to_load(params)

        """Заполняем кол-во мест"""
        find_el(params, input_value_places.xpath)
        send_keys(params, value_places)

        """Заполняем участников"""
        set_counteragent_data(params, 'sender', 'individual')
        set_counteragent_data(params, 'recipient', 'individual')

        """Нажимаем на кнопку 'Оформить'"""
        find_el(params, btn_create_order.xpath)
        click(params)
        price_to_load(params)

        """Поиск номера заказа после создания"""
        find_el(params, text_number_order_after_create.xpath)

    except Exception:
        pass

    finally:
        params.close()
        params.quit()

