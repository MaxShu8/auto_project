import time

from Business_Actions import *
from Methods import *
from pages.order_create_page import *
from pages.contractors_page import *
from pages.list_of_orders_page import *


def hiding_the_payer(params):
    main_description = "Тест №116 - Скрытие плательщика в заказе"
    status_and_name_tst = {}

    #  Берем рандомно два неповторяющихся города из списка
    dispatch_city, destination_city = choice_cities(cities)

    try:
        """1. Проверка скрытия плательщика - автор созданной заявки плательщик"""
        def checking_hiding_the_payer_the_author_of_the_created_application_is_the_payer():
            description = "Проверка скрытия плательщика - автор созданной заявки плательщик"

            try:
                authorization_lk(params, url_base_org, individual_phone_full, passw)

                """Оформляем заказ за первого пользователя"""
                find_el(params, btn_new_order.xpath)
                click(params)
                wait_page(params, url_base_org_order_create)

                # Заполняем 'Отправка'
                find_el(params, input_dispatch_city.xpath)
                click(params)

                set_dispatch_city(params, dispatch_city)

                find_el(params, btn_dispatch_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем 'Прибытие'
                find_el(params, input_destination_city.xpath)
                click(params)

                set_destination_city(params, destination_city)

                find_el(params, btn_destination_terminal.xpath)
                click(params)
                price_to_load(params)

                # Заполняем кол-во мест
                find_el(params, input_value_places.xpath)
                send_keys(params, value_places)

                # Заполняем участников
                set_counteragent_data(params, 'sender', 'individual', individual_fio, individual_phone)
                set_counteragent_data(params, 'recipient', 'individual', individual_fio_2, individual_phone_2)

                # Выбираем плательщика отправителя
                find_el(params, btn_the_sender_button_in_the_payer_block.xpath)
                click(params)

                # Нажимаем на кнопку 'Оформить'
                find_el(params, btn_create_order.xpath)
                click(params)
                price_to_load(params)
                enable_skeleton(params)

                # Поиск номера заказа после создания
                find_el(params, text_number_order_after_create.xpath)
                a = get_the_text(params, text_number_order_after_create.xpath)
                number_of_order = extract_numbers(a)   # Получим номер заказа

                # Переходим в "Контрагенты" и проверяем активен ли переключатель "Скрыть стоимость"
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)
                find_el(params, f"//span[@title='{individual_phone_full}']")
                click(params)

                find_el(params, btn_hide_payer_button_card_contractor.xpath)

                # Проверим активирована ли кнопка "Скрыть плательщика"
                if check_text_attribute(params, btn_hide_payer_button_card_contractor.xpath, 'active', True) is True:
                    pass
                else:
                    click(params)

                # Удаляем все куки и обновляем страницу
                params.delete_all_cookies()
                params.refresh()
                url_contain_url(params, url_base_org_auth)

                """Авторизуемся за второго пользователя, кот. не должен видеть стоимость заказа"""
                authorization_lk(params, url_base_org, individual_phone_2_full, passw2)
                wait_page(params, url_base_org_LK)

                waiting_for_the_order_to_be_visible_to_the_user(params, number_of_order)

                # Проверим есть ли данная карточка заказа с надписью о плательщике в списке заказов и перейдем в неё
                find_el(params, f"//div[contains(text(), '{number_of_order}')]/../../../..//div[contains(text(), 'Плательщиком заказа является Шумилейко Максим Валерьевич')]")
                click(params)

                # В детализации заказа проверим, что имеется текст 'Плательщиком является...'
                find_el(params, txt_the_payer_is_on_the_order_details_page.xpath)

                # Удаляем все куки и обновляем страницу
                params.delete_all_cookies()
                params.refresh()
                url_contain_url(params, url_base_org_auth)

                # Отправляем статус успешности прогона теста
                status, desc = tst_passed(True, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst, number_of_order

            except Exception:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)

                # Отправляем статус о не успешности прогона теста
                status, desc = tst_passed(False, description)
                status_and_name_tst[desc] = status
                return status_and_name_tst

        """2. Проверка, что скрытие плательщика выключается"""
        def checking_that_the_payer_hiding_is_turned_off(number):
            description = "Проверка, что скрытие плательщика выключается"

            try:
                authorization_lk(params, url_base_org, individual_phone_full, passw)

                # Переходим в "Контрагенты" и проверяем активен ли переключатель "Скрыть стоимость"
                set_page(params, url_contractors_org)
                wait_page(params, url_contractors_org)
                find_el(params, f"//span[@title='{individual_phone_full}']")
                click(params)

                find_el(params, btn_hide_payer_button_card_contractor.xpath)
                click(params)
                check_text_attribute(params, btn_hide_payer_button_card_contractor.xpath, 'vz-toggler-button primary')

                # Удаляем все куки и обновляем страницу
                params.delete_all_cookies()
                params.refresh()
                url_contain_url(params, url_base_org_auth)

                """Авторизуемся за второго пользователя, кот. снова должен видеть стоимость заказа"""
                authorization_lk(params, url_base_org, individual_phone_2_full, passw2)
                wait_page(params, url_base_org_LK)

                # Проверим есть ли данный заказ со стоимостью в списке заказов и перейдем в неё
                find_el(params, f"//div[contains(text(), '{number}')]/../../..//div[contains(text(), 'Сумма заказа')]")
                click(params)

                # В детализации заказа проверим, что имеется отображение стоимости
                find_el(params, txt_the_text_of_total_in_the_block_the_cost_in_the_order_details.xpath)

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

        status_and_name_tst, number_of_order = checking_hiding_the_payer_the_author_of_the_created_application_is_the_payer()
        status_and_name_tst = checking_that_the_payer_hiding_is_turned_off(number_of_order)

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()


