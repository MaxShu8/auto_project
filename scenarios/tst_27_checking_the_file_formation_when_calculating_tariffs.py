from Business_Actions import *
from Methods import *
from pages.tariffs_page import *

def checking_the_file_formation_when_calculating_tariffs(params):
    main_description = "Тест №27 - Проверка формирования файла при расчете тарифов"
    status_and_name_tst = {}

    try:
        """1. Проверка формирования файла при расчете тарифов"""
        def check_file_formation_when_calculating_tariffs():
            description = "Проверка формирования файла при расчете тарифов"

            try:
                """Переходим на страницу тарифов"""
                set_page(params, url_tariffs_ru)
                wait_page(params, url_tariffs_ru)

                find_el(params, txt_heading_specify_the_direction_for_calculating_tariffs_block_in_tariffs_page.xpath)

                # Очистим поля ввода от нас пунктов
                find_el(params, btn_clear_from_field_in_tariffs_page.xpath)
                click(params)

                # find_el(params, btn_close_located_at_the_destination_point_in_tariffs_page.xpath)
                # click(params)

                # Введем нас пункт в поля ввода откуда
                find_el(params, inp_us_points_from_in_tariffs_page.xpath)
                click(params)
                send_keys(params, cities[0])

                # Выберем нас пункт из выпадающего списка
                choice_us_item_from_drop_down_list_in_dispatch_in_create_order_page.change_xpath(cities[0])
                find_el(params, choice_us_item_from_drop_down_list_in_dispatch_in_create_order_page.xpath)
                click(params)

                choice_us_item_from_drop_down_list_in_dispatch_in_create_order_page.reset_xpath()

                # Введем нас пункт в поля ввода куда
                find_el(params, inp_us_points_to_in_tariffs_page.xpath)
                click(params)
                send_keys(params, cities[4])

                # Выберем нас пункт из выпадающего списка
                choice_us_item_from_drop_down_list_in_destination_in_create_order_page.change_xpath(cities[4])
                find_el(params, choice_us_item_from_drop_down_list_in_destination_in_create_order_page.xpath)
                click(params)

                choice_us_item_from_drop_down_list_in_destination_in_create_order_page.reset_xpath()

                find_el(params, btn_generate_in_tariffs_page.xpath)
                click(params)

                find_el(params, txt_notification_data_has_been_generated_in_tariffs_page.xpath)

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

            except Exception as e:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        status_and_name_tst = check_file_formation_when_calculating_tariffs()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()

