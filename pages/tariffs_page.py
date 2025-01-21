from site_objects import SiteObjects


"""Элементы страницы \"Тарифы\""""

txt_heading_specify_the_direction_for_calculating_tariffs_block_in_tariffs_page = SiteObjects(
    "Заголовок блока 'Укажите направление для расчета тарифов' на странице Тарифы",
    "//h2[contains(., 'Укажите направление для расчета тарифов')]")

btn_generate_in_tariffs_page = SiteObjects(
    "Кнопка \"Сформировать\" на странице Тарифы",
    "//span[contains(., 'Сформировать')]")

txt_notification_data_has_been_generated_in_tariffs_page = SiteObjects(
    "Текст уведомления 'Данные сформированы...' на странице Тарифы",
    "//span[contains(., 'Данные сформированы, загрузка началась')]")

inp_us_points_from_in_tariffs_page = SiteObjects(
    "Поле ввода нас.пунктов Откуда на странице Тарифы",
    "//label[contains(., 'Откуда')]/..//input[@placeholder='Выберите населенный пункт']")

inp_us_points_to_in_tariffs_page = SiteObjects(
    "Поле ввода нас.пунктов Куда на странице Тарифы",
    "//label[contains(., 'Куда')]/..//input[@placeholder='Выберите населенный пункт']")

btn_clear_from_field_in_tariffs_page = SiteObjects(
    "Кнопка Очистить у поля Откуда на странице Тарифы",
    "//label[contains(., 'Откуда')]/../../..//span[contains(., 'Очистить')]")

btn_clear_to_field_in_tariffs_page = SiteObjects(
    "Кнопка Очистить у поля Откуда на странице Тарифы",
    "//label[contains(., 'Куда')]/../../..//span[contains(., 'Очистить')]")

btn_close_located_at_the_dispatch_point_in_tariffs_page = SiteObjects(
    "Кнопка Закрыть у установленного нас пункта в Куда на странице Тарифы",
    "//label[contains(., 'Откуда')]/../../..//span[@class='mdi mdi-close vz-tag-close']")

btn_close_located_at_the_destination_point_in_tariffs_page = SiteObjects(
    "Кнопка Закрыть у установленного нас пункта в Куда на странице Тарифы",
    "//label[contains(., 'Куда')]/../../..//span[@class='mdi mdi-close vz-tag-close']")




