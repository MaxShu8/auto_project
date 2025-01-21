from Business_Actions import *
from Methods import *
from pages.order_create_page import *
from pages.order_details import *


def checking_the_indication_of_all_types_of_insurance(params):
    main_description = "Тест №64 - Проверка установки страхования"
    status_and_name_tst = {}

    try:
        authorization_lk(params, url_base_org, individual_phone_full, passw)

        """1. Проверка заказа без объявленной стоимости страхования при перевозке в России"""
        def checking_the_choice_without_the_declared_insurance_cost():
            description = "Проверка заказа без объявленной стоимости страхования при перевозке в России"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Выбираем БОС"""
                # Сначала проверим, что если валюта рубль, то установлено БОС
                check_text_attribute(params, txt_type_of_insurance_create_order_page.xpath, "Без объявленной стоимости")

                find_el(params, inp_insurance_create_order_page.xpath)
                click(params)

                find_el(params, choice_without_the_declared_insurance_cost_create_order_page.xpath)
                click(params)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                check_text_attribute(params, txt_Insurance_information_on_the_order_details_page.xpath, "Без объявленной стоимости")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Проверка заказа без страхования при перевозке в России"""
        def checking_without_insurance_cost():
            description = "Проверка заказа без страхования при перевозке в России"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Выбираем Без страхования"""
                find_el(params, inp_insurance_create_order_page.xpath)
                click(params)

                find_el(params, choice_without_insurance_create_order_page.xpath)
                click(params)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                check_text_attribute(params, txt_Insurance_information_on_the_order_details_page.xpath, "Без страхования")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """3. Проверка заказа c указанием страхования при перевозке в России"""
        def checking_with_insurance_cost():
            description = "Проверка заказа c указанием страхования при перевозке в России"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[2])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Указываем страхование"""
                find_el(params, inp_insurance_create_order_page.xpath)
                click(params)

                find_el(params, choice_with_insurance_create_order_page.xpath)
                click(params)

                find_el(params, inp_amount_for_specifying_the_insurance_amount_create_order_page.xpath)
                send_keys(params, "88888")
                price_to_load(params)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                check_text_attribute(params, txt_Insurance_information_on_the_order_details_page.xpath, "Страхование")
                check_text_attribute(params, data_amount_of_the_specified_insurance_in_details_page.xpath, "88888")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """4. Проверка заказа c указанием страхования при перевозке в Казахстан"""
        def checking_of_insurance_during_transportation_to_kazakhstan():
            description = "Проверка заказа c указанием страхования при перевозке в Казахстан"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities[0])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities_another_countries[2])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Указываем страхование"""
                # Проверим, что валюта тенге и выставилось страхование 1000 руб.
                check_text_attribute(params, txt_type_of_insurance_create_order_page.xpath, "Страхование груза")
                check_text_attribute(params, inp_amount_for_specifying_the_insurance_amount_create_order_page.xpath, "1000")
                find_el(params, inp_insurance_create_order_page.xpath)
                click(params)

                check_text_attribute(params, text_without_the_declared_insurance_cost_create_order_page.xpath, "disabled")

                find_el(params, choice_without_insurance_create_order_page.xpath)
                click(params)
                price_to_load(params)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Нажимаем на кнопку 'Подтвердить' в попапе"""
                find_el(params, txt_currency_confirmation_header_in_the_currency_confirmation_popup.xpath)
                find_el(params, btn_confirm_in_the_currency_confirmation_popup.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                check_text_attribute(params, txt_Insurance_information_on_the_order_details_page.xpath, "Без страхования")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """5. Проверка заказа c указанием страхования при перевозке из Казахстана"""
        def checking_of_insurance_during_transportation_from_kazakhstan():
            description = "Проверка заказа c указанием страхования при перевозке в Казахстан"

            try:
                """Переходим на страницу оформления заказа"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)
                price_to_load(params)

                """Заполняем 'Отправка'"""
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, cities_another_countries[2])

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем 'Прибытие'"""
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, cities[0])

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                """Заполняем кол-во мест"""
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                """Указываем страхование"""
                # Проверим, что валюта тенге и выставилось страхование 1000 руб.
                check_text_attribute(params, txt_type_of_insurance_create_order_page.xpath, "Страхование груза")
                check_text_attribute(params, inp_amount_for_specifying_the_insurance_amount_create_order_page.xpath, "1000")
                find_el(params, inp_insurance_create_order_page.xpath)
                click(params)

                check_text_attribute(params, text_without_the_declared_insurance_cost_create_order_page.xpath, "disabled")

                find_el(params, choice_with_insurance_create_order_page.xpath)
                click(params)
                price_to_load(params)

                find_el(params, inp_amount_for_specifying_the_insurance_amount_create_order_page.xpath)
                send_keys(params, "88888")
                price_to_load(params)

                """Заполняем участников"""
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio, individual_phone)

                """Нажимаем на кнопку 'Оформить'"""
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)

                """Нажимаем на кнопку 'Подтвердить' в попапе"""
                find_el(params, txt_currency_confirmation_header_in_the_currency_confirmation_popup.xpath)
                find_el(params, btn_confirm_in_the_currency_confirmation_popup.xpath)
                click(params)
                price_to_load(params)

                """Поиск номера заказа после создания"""
                find_el(params, text_number_order_after_create.xpath)
                check_text_attribute(params, txt_Insurance_information_on_the_order_details_page.xpath, "Страхование")
                check_text_attribute(params, data_amount_of_the_specified_insurance_in_details_page.xpath, "88888")

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        status_and_name_tst = checking_the_choice_without_the_declared_insurance_cost()
        status_and_name_tst = checking_without_insurance_cost()
        status_and_name_tst = checking_with_insurance_cost()
        status_and_name_tst = checking_of_insurance_during_transportation_to_kazakhstan()
        status_and_name_tst = checking_of_insurance_during_transportation_from_kazakhstan()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

