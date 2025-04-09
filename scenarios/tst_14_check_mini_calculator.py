from Business_Actions import *
from Methods import *


def check_mini_calculator(params):
    main_description = 'Тест №14 - проверка мини-калькулятора'
    status_and_name_tst = {}

    try:

        """1. Расчет цены: терминал-терминал"""
        def price_calculation_address_terminal_pvz():

            try:
                description = "14.1 - Расчет цены: терминал-терминал"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                """Проверка расчета цены"""
                # Ищем поле Откуда и устанавливаем там город
                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, city_from)

                price_to_load(params)

                # Ищем кнопку от терминала и кликаем
                find_el(params, btn_from_terminal.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')  # проверим нажата ли кнопка

                # Ищем поле Куда и устанавливаем там город
                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_to)

                price_to_load(params)

                # Ищем кнопку до терминала и кликаем
                find_el(params, btn_to_terminal.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')  # проверим нажата ли кнопка

                """14.2 - Расчет цены: терминал-адрес"""
                description = "14.2 - Расчет цены: терминал-адрес"

                find_el(params, btn_from_address.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка
                check_price(params, currency_rub)

                """14.3 - Расчет цены: терминал-пвз"""
                description = "14.3 - Расчет цены: терминал-пвз"

                find_el(params, btn_to_pvz.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка
                check_price(params, currency_rub)

                """14.4 - Расчет цены: адрес-терминал"""
                description = "14.4 - Расчет цены: адрес-терминал"

                find_el(params, btn_from_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, btn_to_terminal.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')  # проверим нажата ли кнопка
                check_price(params, currency_rub)

                """14.5 - Расчет цены: адрес-адрес"""
                description = "14.5 - Расчет цены: адрес-адрес"

                find_el(params, btn_to_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_address.xpath, 'active')  # проверим нажата ли кнопка
                check_price(params, currency_rub)

                """14.6 - Расчет цены: адрес-пвз"""
                description = "14.6 - Расчет цены: адрес-пвз"

                find_el(params, btn_to_pvz.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка
                check_price(params, currency_rub)

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

        """2. Расчет цены: Россия-Казахстан, Казахстан-Россия, Россия-Беларусь, Беларусь-Россия"""
        def price_calculation_russia_kazakhstan_belarus():

            try:
                """Россия-Казахстан"""
                description = "14.7 - Расчет цены: Россия-Казахстан и наоборот"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                find_el(params, btn_to_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_to_address.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_kz)

                price_to_load(params)
                check_price(params, currency_kzt)

                find_el(params, btn_change_city.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')
                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')
                check_price(params, currency_kzt)

                """Россия-Беларусь"""
                description = "14.8 - Расчет цены: Россия-Беларусь и наоборот"

                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, city_by)

                price_to_load(params)
                check_price(params, currency_ber)

                find_el(params, btn_from_terminal.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')

                find_el(params, btn_change_city.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')
                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

                check_price(params, currency_ber)

                find_el(params, btn_currency_mini_rub.xpath)
                click(params)

                price_to_load(params)
                check_price(params, currency_rub)

                find_el(params, btn_currency_mini_ber.xpath)
                click(params)

                price_to_load(params)
                check_price(params, currency_ber)

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

        """3. Смена одной зарубежной валюты на другую при перевозке Казахстан - Беларусь"""
        def exchange_currency_kazakhstan_belarus():

            try:
                description = "Смена одной зарубежной валюты на другую при перевозке Казахстан - Беларусь"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, city_by)

                price_to_load(params)

                find_el(params, input_to_mini.xpath)
                click(params)
                set_dispatch_city(params, city_kz1)

                price_to_load(params)
                check_price(params, currency_kzt)

                find_el(params, btn_currency_mini_ber.xpath)
                click(params)

                price_to_load(params)
                check_price(params, currency_ber)

                find_el(params, btn_currency_mini_rub.xpath)
                click(params)

                price_to_load(params)
                check_price(params, currency_rub)

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

        """4. Проверка расчета перевозки при одинаковом населенном пункте"""
        def checking_the_transportation_calculation_for_the_same_locality():

            try:
                """1."""
                description = "Проверка расчета перевозки при одинаковом населенном пункте: от терминала до адреса"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_ru3)

                price_to_load(params)

                find_el(params, btn_to_address.xpath)
                click(params)

                price_to_load(params)
                check_text_attribute(params, atr_btn_to_address.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, city_ru3)

                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')

                find_el(params, btn_change_city.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath,
                                     'active')  # вместо ПВЗ в Откуда будет кнопка Адрес
                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

                """2"""
                description = "Проверка расчета перевозки при одинаковом населенном пункте: - от адреса до адреса"

                find_el(params, btn_to_address.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_address.xpath, 'active')

                """3"""
                description = "Проверка расчета перевозки при одинаковом населенном пункте: - от терминала до ПВЗ"

                find_el(params, input_from_mini.xpath)
                click(params)
                set_dispatch_city(params, city_to)

                price_to_load(params)

                find_el(params, btn_from_terminal.xpath)
                click(params)

                price_to_load(params)
                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_to)

                price_to_load(params)

                find_el(params, btn_to_pvz.xpath)
                click(params)

                price_to_load(params)
                check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка

                """4"""
                description = "Проверка расчета перевозки при одинаковом населенном пункте: - от адреса до ПВЗ"

                find_el(params, btn_from_address.xpath)
                click(params)

                price_to_load(params)
                check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

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

        """5. Проверка кнопки 'Поменять местами нас. пункты'"""
        def checking_the_swap_cities_button():

            try:
                """1"""
                description = "Проверка кнопки 'Поменять местами нас. пункты' - от терминала до ПВЗ"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                #  Ищем поле Куда и устанавливаем там город
                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_to)

                price_to_load(params)

                find_el(params, btn_to_pvz.xpath)
                click(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, btn_change_city.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # вместо ПВЗ в Откуда будет кнопка Адрес
                check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

                """2"""
                description = "Проверка кнопки 'Поменять местами нас. пункты' - от адреса до терминала"

                find_el(params, btn_change_city.xpath)  # до нажатия: Адрес --> Терминал
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')
                check_text_attribute(params, atr_btn_to_address.xpath, 'active')

                """3"""
                description = "Проверка кнопки 'Поменять местами нас. пункты' - от адреса до адреса"

                find_el(params, btn_from_address.xpath)
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

                find_el(params, btn_change_city.xpath)  # до нажатия: Адрес --> Адрес
                click(params)
                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')
                check_text_attribute(params, atr_btn_to_address.xpath, 'active')

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

        """6. Проверка неактивности кнопок: терминал/адрес"""
        def checking_button_inactivity_terminal_address():

            try:
                """Нективность кнопки терминал в Куда"""
                description = "14.25 - Проверка, что кнопка 'до терминала' у нас.пункта в 'Куда', где нет терминала - неактивна"

                set_page(params, url_base_org)
                wait_page(params, url_base_org)
                price_to_load(params)

                #  Ищем поле Куда и устанавливаем там город
                find_el(params, input_to_mini.xpath)
                click(params)
                set_destination_city(params, city_by1)

                price_to_load(params)

                check_text_attribute(params, atr_btn_to_address.xpath, 'active')
                check_text_attribute(params, atr_btn_to_terminal.xpath, 'disabled')

                """Нективность кнопки терминал в Откуда"""
                description = "14.25 - Проверка, что кнопка 'до терминала' у нас.пункта в 'Куда', где нет терминала - неактивна"

                find_el(params, btn_change_city.xpath)
                click(params)
                price_to_load(params)

                price_to_load(params)

                check_text_attribute(params, atr_btn_from_address.xpath, 'active')
                check_text_attribute(params, atr_btn_from_terminal.xpath, 'disabled')

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

        status_and_name_tst = price_calculation_address_terminal_pvz()
        status_and_name_tst = price_calculation_russia_kazakhstan_belarus()
        status_and_name_tst = checking_the_transportation_calculation_for_the_same_locality()
        status_and_name_tst = exchange_currency_kazakhstan_belarus()
        status_and_name_tst = checking_the_swap_cities_button()
        status_and_name_tst = checking_button_inactivity_terminal_address()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()
