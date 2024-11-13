import time
import Settings
from Business_Actions import check_try
from Methods import *
from Settings import *
from pages.documents_page import *
from pages.payment_page import *


def check_payment_counteragent(params):
    main_description = "Тест 17 - Проверка оплаты банковской картой"
    send_message_tg(f"🔔 {main_description}", token, group_id_for_message_bot)

    try:
        authorization_lk(params, url_base_ru)

        set_page(params, url_contractors_ru)

        find_el(params, btn_top_up_account_counteragent.xpath)
        click(params)

        find_el(params, btn_top_up_in_modal_counteragent.xpath)
        click(params)

        # Дождемся исчезновение лоадера
        enable_loader(params)

        def verification_of_payment_by_bank_card_alfa():
            try:
                description = "17.1 - Проверка оплаты банковской картой Альфа"

                # Перейдем на открывшуюся страницу Альфы
                switch_to_next_or_previous_tab(params)
                url_contain_url(params, url_alfa)

                # Заполним платежные данные тестовой карты

                find_el(params, btn_pay_alfa_prod.xpath)
                click(params)

                find_el(params, input_number_card_alfa_prod.xpath)
                click(params)

                send_keys(params, number_card_alfa)
                send_keys(params, Keys.TAB, False)  # Передадим False, чтобы при нажатии на TAB не удалялись ранее введенные данные

                find_el(params, input_expiration_date_alfa_prod.xpath)
                click(params)
                send_keys(params, expiration_date_alfa)

                click(params)
                send_keys(params, Keys.TAB, False)

                find_el(params, input_cvv_cvc_code_prod.xpath)
                click(params)

                send_keys(params, cvv_cvc_code_alfa)
                send_keys(params, Keys.TAB, False)

                # Нажимаем кнопку "Оплатить картой"
                find_el(params, btn_pay_alfa_after_input_data_prod.xpath)
                click(params)

                find_el(params, text_code_sms_on_phone_alfa_prod.xpath)
                print('Смс с Альфы успешно отправлено...')

            except Exception:
                check_try(0, 1, 2)
                send_photo_tg(params, token, group_id_for_message_bot, desc=description)
                # send_message_tg(f"{description}\n{e}", token, chat_id)
                pass

        def verification_of_payment_by_bank_card_vtb():
            try:
                description = "17.2 - Проверка оплаты банковской картой ВТБ"

                set_page(params, url_contractors_ru)

                find_el(params, btn_top_up_account_counteragent.xpath)
                click(params)

                find_el(params, btn_top_up_in_modal_counteragent.xpath)
                click(params)

                # Дождемся исчезновение лоадера
                enable_loader(params)

                # Перейдем на открывшуюся страницу
                switch_to_next_or_previous_tab(params)
                url_contain_url(params, url_vtb)

                # Заполним платежные данные тестовой карты

                find_el(params, btn_pay_alfa_prod.xpath)
                click(params)

                find_el(params, input_number_card_alfa_prod.xpath)
                click(params)

                send_keys(params, number_card_vtb)
                send_keys(params, Keys.TAB, False)  # Передадим False, чтобы при нажатии на TAB не удалялись ранее введенные данные

                find_el(params, input_expiration_date_alfa_prod.xpath)
                click(params)
                send_keys(params, expiration_date_vtb)

                click(params)
                send_keys(params, Keys.TAB, False)

                find_el(params, input_cvv_cvc_code_prod.xpath)
                click(params)

                send_keys(params, cvv_cvc_code_vtb)
                send_keys(params, Keys.TAB, False)

                # Нажимаем кнопку "Оплатить картой"
                find_el(params, btn_pay_alfa_after_input_data_prod.xpath)
                click(params)

                find_el(params, inp_confirm_sms_code_vtb_prod.xpath)

                print('Смс с ВТБ успешно отправлено...')

            except Exception:
                send_photo_tg(params, token, group_id_for_message_bot, desc=description)
                # send_message_tg(f"{description}\n{e}", token, chat_id)
                check_try(0, 1, 2)
                pass

        verification_of_payment_by_bank_card_alfa()
        verification_of_payment_by_bank_card_vtb()

    except Exception:
        # Если какая-то ошибка - значит отправляем соответствующий статус
        send_photo_tg(params, token, group_id_for_message_bot, desc=main_description)
        # send_message_tg(e, token, chat_id)
        pass

    finally:
        params.close(), params.quit()


def main_monitoring_func():
    # Вывод дня недели
    time_now = datetime.datetime.now()
    current_time_hour = time_now.hour

    # Вывод дня недели
    week_day = datetime.datetime.today().weekday()

    if current_time_hour == 8 and week_day <= 4:
        check_payment_counteragent(Settings.driver_start())  # запуск без --headless


main_monitoring_func()

