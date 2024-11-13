import time
from Business_Actions import *
from Methods import *
from pages.order_create_page import *


def checking_the_choice_of_another_currency(params):
    main_description = "Тест №45 - проверка смены валюты при международной перевозке"
    status_and_name_tst = {}

    try:
        """1. Проверка установки корректной валюты, исходя из страны"""

        def installation_of_the_correct_currency_based_on_the_country():
            description = "Проверка установки корректной валюты"

            try:
                """Переходим на страницу расчета заказа"""
                set_page(params, url_base_dev_order_create_public)
                wait_page(params, url_base_dev_order_create_public)

                find_el(params, txt_order_in_calculation_and_ordering_page.xpath)

                # Заполняем "Отправка" - устанавливаем другую страну
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, city_by)

                price_to_load(params)

                # Проверка, что установилась "бел. руб." в услугах в блоке "Стоимость"
                find_el(params, displaying_the_currency_bel_ru_in_the_cost_block.xpath)  # Проверяем есть ли элемент с тенге
                check_text_attribute(params, displaying_the_total_currency_in_the_cost_block.xpath, "бел")

                # Проверка, что установилась "бел. руб." в кнопках Адрес
                check_text_attribute(params, displaying_the_cost_on_the_from_address_button_in_the_cost_block.xpath, "бел")
                check_text_attribute(params, displaying_the_cost_on_the_to_address_button_in_the_cost_block.xpath, "бел")

                # Поменяем на рос. рубль и проверим, что в блоке все корректно пересчиталось
                find_el(params, btn_currency_change_button_in_the_cost_block.xpath)
                click(params)

                find_el(params, btn_currency_change_ru_in_the_cost_block.xpath)
                click(params)

                check_text_attribute(params, displaying_the_currency_ru_in_the_cost_block.xpath, "₽")
                check_text_attribute(params, displaying_the_total_currency_in_the_cost_block.xpath, "₽")

                # Проверим отображение корректной валюты в кнопке "Адрес"
                check_text_attribute(params, displaying_the_cost_on_the_from_address_button_in_the_cost_block.xpath, "₽")
                check_text_attribute(params, displaying_the_cost_on_the_to_address_button_in_the_cost_block.xpath, "₽")

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

        status_and_name_tst = installation_of_the_correct_currency_based_on_the_country()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


