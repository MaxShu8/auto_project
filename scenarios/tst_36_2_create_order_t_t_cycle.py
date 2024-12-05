from list_of_tst import *


def create_order_t_t_cycle(params):
    main_description = 'Тест №36.2 - Создание заказа Терминал --> Терминал (цикл заявок)'
    description = ''

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        for i in range(1, int(len(cities))*200):

            #  Берем рандомно два неповторяющихся города из списка
            dispatch_city, destination_city = choice_cities(cities)

            """Переходим на страницу оформления заказа"""
            find_el(params, btn_new_order.xpath)
            click(params)
            wait_page(params, url_base_org_order_create)
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

            """Заполняем кол-во мест, объем и вес"""
            find_el(params, input_value_places.xpath)
            set_places(params)
            price_to_load(params)

            find_el(params, input_value_weight.xpath)
            click(params)   # клик нужен, чтобы убрать фокус с предыдущего поля
            set_weight(params)
            price_to_load(params)

            find_el(params, input_value_volume.xpath)
            click(params)  # клик нужен, чтобы убрать фокус с предыдущего поля
            set_volume(params)
            price_to_load(params)

            """Заполняем участников"""
            set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
            set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

            """Нажимаем на кнопку 'Оформить'"""
            find_el(params, btn_create_order.xpath)
            click(params)
            # Возможно сюда стоит добавить price to load
            # url_contain_url(params, url_after_create_org)

            """Поиск номера заказа после создания"""
            find_number_order(params)
            success_request_for_transportation(1)

    except TimeoutException:
        pass

    except WebDriverException:
        pass

    except Exception as e:
        # Если какая-то ошибка - значит отправляем соответствующий статус
        # send_photo_tg(params, token, chat_id, desc=description)  # почему-то не отправилось
        # send_message_tg(e, token, chat_id)
        # send_message_tg(f'🔴 Заявка не записалась', token, group_id_predprod)
        pass

    finally:
        return main_description, params.close(), params.quit()
