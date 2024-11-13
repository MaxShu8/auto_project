import time

from Business_Actions import *
from Methods import *
from pages.order_create_page import *

"""Тест №61 - Проверка категории груза"""
def checking_the_selection_of_one_category(params):
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
        check_text_attribute(params, choice_sort_category_equipment_in_calculation_and_ordering_page.xpath,
                             'Автозапчасти')

        # Сверяем, что отображается иконка ЖУ
        find_el(params, icn_rigid_packaging_icon_in_calculation_and_ordering_page.xpath)

        # Отправляем статус успешности прогона теста
        status, desc = sending_run_status(0, description)
        return status, desc

    except Exception:
        # Если какая-то ошибка - значит отправляем соответствующий статус
        send_photo_tg(params, token, chat_id, desc=description)

        # Отправляем статус о не успешности прогона теста
        status, desc = sending_run_status(1, description)
        return status, desc

# Главная функция
def checking_the_category_selection(params):
    main_description = "Тест №61 - Проверка категории груза"
    status = ""
    desc = ""

    """1. Проверка выбора категории, её смена и отображение иконки ЖУ"""
    status, desc = checking_the_selection_of_one_category(params)

    return main_description, status, desc, params.close(), params.quit()



