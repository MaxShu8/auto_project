from Business_Actions import *
from Methods import *


def check_mini_calculator(params):
    main_description = 'Тест №14 - проверка мини-калькулятора'
    description = ''

    try:
        # Главная страница
        set_page(params, url_base_org)
        wait_page(params, url_base_org)
        price_to_load(params)

        """Тест 14.1"""
        description = "14.1 - Расчет цены: терминал-терминал (ТК VZ-T1)"

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

        """Тест 14.2"""
        description = "14.2 - Расчет цены: терминал-адрес (ТК VZ-T2)"

        find_el(params, btn_from_address.xpath)
        click(params)

        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка
        check_price(params, currency_rub)

        """Тест 14.3"""
        description = "14.3 - Расчет цены: терминал-пвз (ТК VZ-T3)"

        find_el(params, btn_to_pvz.xpath)
        click(params)

        price_to_load(params)

        check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка
        check_price(params, currency_rub)

        """Тест 14.4"""
        description = "14.4 - Расчет цены: адрес-терминал (ТК VZ-T4)"

        find_el(params, btn_from_address.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

        find_el(params, btn_to_terminal.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')  # проверим нажата ли кнопка
        check_price(params, currency_rub)

        """Тест 14.5"""
        description = "14.5 - Расчет цены: адрес-адрес (ТК VZ-T5)"

        find_el(params, btn_to_address.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_to_address.xpath, 'active')  # проверим нажата ли кнопка
        check_price(params, currency_rub)

        """Тест 14.6"""
        description = "14.6 - Расчет цены: адрес-пвз (ТК VZ-T6)"

        find_el(params, btn_to_pvz.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_to_pvz.xpath, 'active')  # проверим нажата ли кнопка
        check_price(params, currency_rub)

        """Тест 14.7"""
        description = "14.7 - Расчет цены: Россия-Казахстан (ТК VZ-T7)"

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

        """Тест 14.8"""
        description = "14.8 - Расчет цены: Казахстан-Россия (ТК VZ-T8)"

        find_el(params, btn_change_city.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')
        check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')
        check_price(params, currency_kzt)

        """Тест 14.9"""
        description = "14.9 - Расчет цены: Беларусь-Россия (ТК VZ-T9)"

        find_el(params, input_from_mini.xpath)
        click(params)
        set_dispatch_city(params, city_by)

        price_to_load(params)
        check_price(params, currency_ber)

        find_el(params, btn_from_terminal.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')

        """Тест 14.10"""
        description = "14.10 - Расчет цены: Россия-Беларусь (ТК VZ-T10)"

        find_el(params, btn_change_city.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')
        check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

        check_price(params, currency_ber)

        """Тест 14.11"""
        description = "14.11 - Выбор валюты Расчет цены: Россия-Беларусь (ТК VZ-T11)"

        find_el(params, btn_currency_mini_rub.xpath)
        click(params)

        price_to_load(params)
        check_price(params, currency_rub)

        find_el(params, btn_currency_mini_ber.xpath)
        click(params)

        price_to_load(params)
        check_price(params, currency_ber)

        """Тест 14.12"""
        description = "14.12 - Смена одной зарубежной валюты на другую при перевозке Казахстан - Беларусь (ТК VZ-T26)"

        find_el(params, input_from_mini.xpath)
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

        """Тест 14.13"""
        description = "14.13 - Проверка расчета перевозки при одинаковом населенном пункте: - от терминала до терминал"

        set_page(params, url_base_org)
        wait_page(params, url_base_org)
        price_to_load(params)

        """Тест 14.14"""
        description = "14.14 - Проверка расчета перевозки при одинаковом населенном пункте: - от терминала до адреса"

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

        """Тест 14.16"""
        description = "14.16 - Проверка расчета перевозки при одинаковом населенном пункте: - от адреса до терминала"

        find_el(params, btn_change_city.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # вместо ПВЗ в Откуда будет кнопка Адрес
        check_text_attribute(params, atr_btn_to_terminal.xpath, 'active')

        """Тест 14.17"""
        description = "14.17 - Проверка расчета перевозки при одинаковом населенном пункте: - от адреса до адреса"

        find_el(params, btn_to_address.xpath)
        click(params)

        price_to_load(params)

        check_text_attribute(params, atr_btn_to_address.xpath, 'active')

        """Тест 14.15"""
        description = "14.15 - Проверка расчета перевозки при одинаковом населенном пункте: - от терминала до ПВЗ"

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

        """Тест 14.18"""
        description = "14.18 - Проверка расчета перевозки при одинаковом населенном пункте: - от адреса до ПВЗ"

        find_el(params, btn_from_address.xpath)
        click(params)

        price_to_load(params)
        check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

        """Тест 14.22"""
        description = "14.22 - Проверка кнопки 'Поменять местами нас. пункты' - от терминала до ПВЗ"

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

        """Тест 14.23"""
        description = "14.23 - Проверка кнопки 'Поменять местами нас. пункты' - от адреса до терминала"

        find_el(params, btn_change_city.xpath)  # до нажатия: Адрес --> Терминал
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_terminal.xpath, 'active')
        check_text_attribute(params, atr_btn_to_address.xpath, 'active')

        """Тест 14.24"""
        description = "14.24 - Проверка кнопки 'Поменять местами нас. пункты' - от адреса до адреса"

        find_el(params, btn_from_address.xpath)
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')  # проверим нажата ли кнопка

        find_el(params, btn_change_city.xpath)  # до нажатия: Адрес --> Адрес
        click(params)
        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')
        check_text_attribute(params, atr_btn_to_address.xpath, 'active')

        """Тест 14.25"""
        description = "14.25 - Проверка, что кнопка 'до терминала' у нас.пункта в 'Куда', где нет терминала - неактивна"

        #  Ищем поле Куда и устанавливаем там город
        find_el(params, input_to_mini.xpath)
        click(params)
        set_destination_city(params, city_by1)

        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')
        check_text_attribute(params, atr_btn_to_address.xpath, 'active')
        check_text_attribute(params, atr_btn_to_terminal.xpath, 'disabled')

        """Тест 14.26"""
        description = "14.26 - Проверка, что кнопка 'от терминала' у нас.пункта в 'Откуда', где нет терминала - неактивна"

        find_el(params, btn_change_city.xpath)
        click(params)
        price_to_load(params)

        price_to_load(params)

        check_text_attribute(params, atr_btn_from_address.xpath, 'active')
        check_text_attribute(params, atr_btn_from_terminal.xpath, 'disabled')
        check_text_attribute(params, atr_btn_to_address.xpath, 'active')

        sending_run_status(1, main_description)

    except Exception:
        send_photo_tg(params, token, chat_id, desc=description)
        sending_run_status(0, description)
        pass

    finally:
        return main_description, params.close(), params.quit()
