from Business_Actions import *
from Methods import *


def check_authorization_email(params):
    main_description = 'Тест №13 - Проверка авторизации (электронная почта)'
    status_and_name_tst = {}

    try:
        """1. Авторизация с помощью email на главной странице https://vozovoz.org/"""
        def authorization_by_email_on_the_main_page():
            description = "Авторизация с помощью email на главной странице https://vozovoz.org/"
            try:
                for key, value in email.items():
                    # Загружаем страницу
                    set_page(params, url_base_org)
                    wait_page(params, url_base_org)
                    price_to_load(params)

                    # Авторизовываемся
                    find_el(params, btn_personal_area.xpath)
                    click(params)
                    find_el(params, inp_login.xpath)
                    send_keys(params, key)
                    find_el(params, btn_continue.xpath)
                    click(params)
                    find_el(params, inp_password.xpath)
                    send_keys(params, value)
                    find_el(params, btn_login.xpath)
                    click(params)

                    find_el(params, img_logo_lk.xpath)

                    # Удаляем все куки и обновляем страницу
                    params.delete_all_cookies()
                    params.refresh()
                    url_contain_url(params, url_base_org_auth)

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

        """2. Авторизация с помощью email на странице https://vozovoz.org/personal/auth/"""
        def authorization_by_email_on_the_page_personal_auth():
            description = "Авторизация с помощью email на странице https://vozovoz.org/personal/auth/"
            try:
                for key, value in email.items():
                    find_el(params, inp_login.xpath)
                    send_keys(params, key)
                    find_el(params, btn_continue.xpath)
                    click(params)
                    find_el(params, inp_password.xpath)
                    send_keys(params, value)
                    find_el(params, btn_login.xpath)
                    click(params)

                    find_el(params, img_logo_lk.xpath)

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

        status_and_name_tst = authorization_by_email_on_the_main_page()
        status_and_name_tst = authorization_by_email_on_the_page_personal_auth()

    finally:
        return main_description, status_and_name_tst, params.close(), params.quit()
