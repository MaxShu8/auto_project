import time

from Business_Actions import *
from Methods import *
from pages.order_create_page import *


def checking_the_category_selection(params):
    main_description = "Тест №61 - Проверка категории груза"
    status_and_name_tst = {}

    try:
        """1. Проверка выбора категории, её смена и отображение иконки ЖУ"""
        def checking_the_selection_of_one_category():
            description = "Проверка выбора категории"

            try:
                """Переходим на страницу расчета заказа"""
                set_page(params, url_base_dev_order_create_public)
                wait_page(params, url_base_dev_order_create_public)

                find_el(params, txt_order_in_calculation_and_ordering_page.xpath)

                """Взаимодействие с категорией груза"""
                # Выбираем категорию
                find_el(params, inp_cargo_category_in_calculation_and_ordering_page.xpath)
                click(params)

                # Выбираем "Игрушки" в раскрывшемся списке
                find_el(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath)
                click(params)

                find_el(params, choice_sort_category_toys_in_calculation_and_ordering_page.xpath)
                click(params)

                price_to_load(params)

                # Сверяем, что выбралась/отображается верная категория
                check_text_attribute(params, choice_sort_subcategory_toys_in_calculation_and_ordering_page.xpath, 'Игрушки')

                # Выбираем новую категорию "Оборудование"
                find_el(params, inp_cargo_category_in_calculation_and_ordering_page.xpath)
                click(params)
                click(params)

                find_el(params, choice_sort_subcategory_equipment_in_calculation_and_ordering_page.xpath)
                click(params)

                find_el(params, choice_sort_category_equipment_in_calculation_and_ordering_page.xpath)
                click(params)

                price_to_load(params)

                # Сверяем, что выбралась/отображается верная категория
                check_text_attribute(params, choice_sort_category_equipment_in_calculation_and_ordering_page.xpath, 'Автозапчасти')

                # Сверяем, что отображается иконка ЖУ
                find_el(params, icn_rigid_packaging_icon_in_calculation_and_ordering_page.xpath)

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

        status_and_name_tst = checking_the_selection_of_one_category()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


