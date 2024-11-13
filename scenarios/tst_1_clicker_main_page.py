from Business_Actions import *
from Methods import *


def clicker_main_page(params):
    main_description = 'Тест №1 - кликер страниц (ГЛАВНАЯ СТРАНИЦА)'
    description = ''

    try:
        # Главная страница
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        def click_header_main_page():
            description = 'Тест №1.1 - Прокликивание ссылок в Хедере страницы'

            try:
                # Город
                find_el(params, btn_choice_city.xpath)
                click(params)
                find_el(params, text_choice_city.xpath)
                find_el(params, btn_close_choice_city.xpath)
                click(params)

                # Тема (светлая/темная)
                find_el(params, btn_choice_color_theme.xpath)
                click(params)
                find_el(params, attribute_choice_dark_theme.xpath)
                find_el(params, btn_choice_color_theme.xpath)
                click(params)

                # Кнопка "Рассчитать"
                find_el(params, btn_calculate_button.xpath)
                click(params)
                find_el(params, text_placing_an_order.xpath)
                set_page(params, url_base_org)  # возврат на главную страницу
                wait_page(params, url_base_org)

                # Кнопка "Отследить"
                find_el(params, btn_track_button.xpath)
                click(params)
                find_el(params, text_track_page.xpath)
                set_page(params, url_base_org)  # возврат на главную страницу
                wait_page(params, url_base_org)

                # Кнопка "Контакты"
                find_el(params, btn_contacts_button.xpath)
                click(params)
                find_el(params, text_contacts_page.xpath)
                set_page(params, url_base_org)  # возврат на главную страницу
                wait_page(params, url_base_org)

            except Exception as e:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)
                pass

        def click_header_services_menu():
            description = 'Тест №1.2 - Прокликивание ссылок в меню УСЛУГИ'

            try:
                """УСЛУГИ"""
                # Услуги - Адресная доставка
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_address_delivery.xpath)
                click(params)
                find_el(params, text_on_address_delivery.xpath)

                # Услуги - Упаковка
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_wrapping.xpath)
                click(params)
                find_el(params, icon_on_wrapping.xpath)

                # Услуги - Ответственное хранение
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_safe_custody.xpath)
                click(params)
                find_el(params, text_on_safe_custody.xpath)

                # Услуги - Страхование
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_insurance.xpath)
                click(params)
                find_el(params, text_on_insurance.xpath)

                # Услуги - ПРР
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_cargo_loading.xpath)
                click(params)
                find_el(params, text_on_cargo_loading.xpath)

                # Услуги - Яндекс-маркет
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_yandex_market.xpath)
                click(params)
                find_el(params, banner_on_yandex_market.xpath)

                # Услуги - OZON
                find_el(params, btn_header_services.xpath)
                click(params)
                find_el(params, btn_header_ozon.xpath)
                click(params)
                find_el(params, banner_on_ozon.xpath)

            except Exception as e:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)
                pass

        def click_header_cargo_transportation_menu():
            description = 'Тест №1.3 - Прокликивание ссылок в меню ГРУЗОПЕРЕВОЗКИ'

            try:
                """ГРУЗОПЕРЕВОЗКИ"""
                # Грузоперевозки - Доставка в торговые сети
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_networkshops.xpath)
                click(params)
                find_el(params, text_on_networkshops.xpath)

                # Грузоперевозки - Доставка для интернет-магазинов
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_online_store.xpath)
                click(params)
                find_el(params, text_on_online_store.xpath)

                # Грузоперевозки - Доставка сборных грузов
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_delivery_russia.xpath)
                click(params)
                find_el(params, text_on_delivery_russia.xpath)

                # # Грузоперевозки - Бесплатный ГЗ
                # find_el(params, btn_header_directions.xpath)
                # click(params)
                # find_el(params, btn_header_free_group_pickup.xpath)
                # click(params)
                # find_el(params, banner_on_free_group_pickup.xpath)

                # Грузоперевозки - Грузоперевозки Беларусь
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_cargo_belarus.xpath)
                click(params)
                find_el(params, text_on_cargo_belarus.xpath)

                # Грузоперевозки - Грузоперевозки Казахстан
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_cargo_kazakhstan.xpath)
                click(params)
                find_el(params, text_on_cargo_kazakhstan.xpath)

                # Грузоперевозки - Грузоперевозки Китай
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_cargo_china.xpath)
                click(params)
                find_el(params, text_on_cargo_china.xpath)

                # Грузоперевозки - Типы грузоперевозок
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_header_shipping_types.xpath)
                click(params)
                find_el(params, text_on_shipping_types.xpath)

                # # Грузоперевозки - Доставка между столицами
                # find_el(params, btn_header_directions.xpath)
                # click(params)
                # find_el(params, btn_header_fast_delivery_capital.xpath)
                # click(params)
                # find_el(params, text_on_fast_delivery_capital.xpath)

                # Грузоперевозки - Направления перевозок
                find_el(params, btn_header_directions.xpath)
                click(params)
                find_el(params, btn_directions_in_cargo_transportation.xpath)
                click(params)
                find_el(params, text_on_directions.xpath)

            except Exception as e:
                # Если какая-то ошибка - значит отправляем соответствующий статус
                send_photo_tg(params, token, chat_id, desc=description)
                pass

        # Информация - Документы
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        # Информация - Сроки доставки
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_run_schedule.xpath)
        click(params)
        find_el(params, text_on_run_schedule_page.xpath)

        # Информация - Способы оплаты
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_payment_methods.xpath)
        click(params)
        find_el(params, text_on_payment_methods_page.xpath)

        # Информация - Тарифы
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_tariffs.xpath)
        click(params)
        find_el(params, text_on_tariffs_page.xpath)

        # Информация - Грузы, не принимаемые к доставке
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_prohibited_goods.xpath)
        click(params)
        find_el(params, text_on_prohibited_goods_page.xpath)




        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_info_docs.xpath)
        click(params)
        find_el(params, text_header_info_docs.xpath)

        # Информация - Часто задаваемые вопросы
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_info_help.xpath)
        click(params)
        find_el(params, text_on_info_help_page.xpath)









        # Информация - Франшиза
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_franchise.xpath)
        click(params)
        find_el(params, text_on_franchise_page.xpath)



        # Информация - Перевозчикам
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_partners.xpath)
        click(params)
        url_contain_url(params, url_auk)

        # Информация - Разработчикам
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_develop.xpath)
        click(params)
        find_el(params, text_on_develop_page.xpath)

        # Информация - Вакансии
        find_el(params, btn_header_info.xpath)
        click(params)
        find_el(params, btn_header_vacancy.xpath)
        click(params)
        find_el(params, text_on_vacancy_page.xpath)

        # География
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_header_geo.xpath)
        click(params)
        find_el(params, input_geo_page.xpath)

        """Тест №1.3"""
        description = 'Тест №1.3 - Ссылки в мини-калькуляторе'

        set_page(params, url_base_org)
        wait_page(params, url_base_org)
        price_to_load(params)

        find_el(params, delivery_time_mini_calc.xpath)
        click(params)
        find_el(params, text_on_run_schedule_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)
        price_to_load(params)

        find_el(params, btn_calculate_mini_calc.xpath)
        click(params)
        find_el(params, text_placing_an_order.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)
        price_to_load(params)

        find_el(params, inp_track_mini_calc.xpath)
        click(params)
        send_keys(params, order_mini_calc)
        find_el(params, btn_track_mini_calc.xpath)
        click(params)
        find_el(params, text_order_track.xpath)

        """Тест №1.4"""
        description = "Тест №1.4 - Ссылки в разделе 'Транспортная компания Vozovoz'"

        # ЧАСТНЫМ ЛИЦАМ
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_private_person_page.xpath)
        click(params)

        find_el(params, btn_address_delivery_main.xpath)
        click(params)
        find_el(params, text_on_address_delivery.xpath)

        # Погрузочные работы
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_private_person_page.xpath)
        click(params)

        find_el(params, btn_cargo_loading_main.xpath)
        click(params)
        find_el(params, text_on_cargo_loading.xpath)

        # Упаковка
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_private_person_page.xpath)
        click(params)

        find_el(params, btn_wrapping_main.xpath)
        click(params)
        find_el(params, icon_on_wrapping.xpath)

        # Удобные способы оплаты
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_private_person_page.xpath)
        click(params)

        find_el(params, btn_payment_methods_main.xpath)
        click(params)
        find_el(params, text_on_payment_methods_page.xpath)

        # БИЗНЕСУ
        # Доставка в торговые сети...
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_business_page.xpath)
        click(params)

        find_el(params, btn_networkshops_main.xpath)
        click(params)
        find_el(params, text_on_networkshops.xpath)

        # ЭДО
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_business_page.xpath)
        click(params)

        find_el(params, btn_edo_main.xpath)
        click(params)
        find_el(params, text_edo_edo.xpath)

        # Страхование
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_business_page.xpath)
        click(params)

        find_el(params, btn_insurance_main.xpath)
        click(params)
        find_el(params, text_on_insurance.xpath)

        # Быстрая доставка между городами
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_business_page.xpath)
        click(params)

        find_el(params, btn_fast_delivery_capital_main.xpath)
        click(params)
        find_el(params, text_on_fast_delivery_capital.xpath)

        # Коммерческое предложение
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_business_page.xpath)
        click(params)
        find_el(params, btn_commercial_offer_main.xpath)
        click(params)

        find_el(params, text_feedback_popup.xpath)

        # Интернет-магазинам
        # БГЗ
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_net_shops_main_page.xpath)
        click(params)

        find_el(params, btn_delivery_russia_main.xpath)
        click(params)
        find_el(params, text_on_delivery_russia.xpath)

        # Онлайн управление
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_net_shops_main_page.xpath)
        click(params)

        find_el(params, btn_guide_lk_main.xpath)
        click(params)
        find_el(params, text_guide_lk_main.xpath)

        # Наложенный платеж
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_net_shops_main_page.xpath)
        click(params)

        find_el(params, btn_cash_on_delivery_main.xpath)
        click(params)
        find_el(params, text_cash_on_delivery_main.xpath)

        # Бесплатное хранение
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_net_shops_main_page.xpath)
        click(params)

        find_el(params, btn_safe_custody_main.xpath)
        click(params)
        find_el(params, text_on_safe_custody.xpath)

        # Партнерам
        # Перевозчикам
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_partners_main_page.xpath)
        click(params)

        find_el(params, btn_carrier_main_page.xpath)
        click(params)
        url_contain_url(params, url_auk)

        # Франшиза
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_partners_main_page.xpath)
        click(params)

        find_el(params, btn_franchise_main.xpath)
        click(params)
        find_el(params, text_on_franchise_page.xpath)

        # Кнопка "Все услуги"
        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_all_services_main.xpath)
        click(params)
        find_el(params, text_all_services_page.xpath)

        """Тест №1.5"""
        description = "Тест №1.5 - Ссылки в разделе подвала сайта"

        find_el(params, btn_services_footer.xpath)
        click(params)
        find_el(params, text_all_services_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_tariffs_footer.xpath)
        click(params)
        find_el(params, text_on_tariffs_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_vacancy_footer.xpath)
        click(params)

        find_el(params, text_on_vacancy_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_terminals_footer.xpath)
        click(params)

        find_el(params, input_geo_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_directions_footer.xpath)
        click(params)
        find_el(params, text_on_directions.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_information_footer.xpath)
        click(params)
        find_el(params, text_on_develop_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_documents_footer.xpath)
        click(params)
        find_el(params, text_header_info_docs.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_franchise_footer.xpath)
        click(params)
        find_el(params, text_on_franchise_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_partners_footer.xpath)
        click(params)
        url_contain_url(params, url_auk)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_develop_footer.xpath)
        click(params)
        find_el(params, text_on_develop_page.xpath)

        set_page(params, url_base_org)
        wait_page(params, url_base_org)

        find_el(params, btn_contacts_footer.xpath)
        click(params)
        find_el(params, text_contacts_page.xpath)

        # Вызов функций
        # click_header_main_page()
        # click_header_services_menu()
        # click_header_cargo_transportation_menu()

        # Если доходит до сюда - значит все ок и отправляем соответствующий статус
        sending_run_status(1, main_description)

    except Exception:
        # Если какая-то ошибка - значит отправляем соответствующий статус
        send_photo_tg(params, token, chat_id, desc=description)
        sending_run_status(0, description)
        pass

    finally:
        return description, params.close(), params.quit()

