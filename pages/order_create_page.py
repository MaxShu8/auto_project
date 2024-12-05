from site_objects import SiteObjects


"""Элементы страницы \"Расчет и оформление заказа\" """

btn_calculate_in_the_header = SiteObjects(
    "Кнопка 'Рассчитать' на странице 'Расчет и оформление заказа'",
    "(//span[text()='Рассчитать'])[1]")

txt_order_in_calculation_and_ordering_page = SiteObjects(
    "Текст 'Заказ' на странице 'Расчет и оформление заказа'",
    "//span[text()='Заказ']")

skeleton_after_push_the_btn_create_order = SiteObjects(
    "Скелетон в номере заказа после создания заказа",
    "//div[@class='w-20 mr-auto']/div[contains(@class, 'vz-skeleton vz-skeleton-animated')]")


#  Категория груза

inp_cargo_category_in_calculation_and_ordering_page = SiteObjects(
    "Поле 'Категория груза' на странице 'Расчет и оформление заказа'",
    "//input[@class='vue-treeselect__input']")

choice_sort_subcategory_toys_in_calculation_and_ordering_page = SiteObjects(
    "Подкатегория 'Игрушки' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vue-treeselect')]//span[text()='Игрушки']")

choice_sort_category_toys_in_calculation_and_ordering_page = SiteObjects(
    "Категория 'Игрушки' на странице 'Расчет и оформление заказа'",
    "(//div[@class='vue-treeselect__list']//span[text()='Игрушки'])[2]")

choice_sort_subcategory_equipment_in_calculation_and_ordering_page = SiteObjects(
    "Подкатегория 'Авто-мото-вело техника' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vue-treeselect')]//span[text()='Авто-мото-вело техника']")

choice_sort_category_equipment_in_calculation_and_ordering_page = SiteObjects(
    "Категория 'Оборудование' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vue-treeselect')]//span[text()='Автозапчасти']")

icn_rigid_packaging_icon_in_calculation_and_ordering_page = SiteObjects(
    "Иконка 'ЖУ' у категории на странице 'Расчет и оформление заказа'",
    "//span[text()='Автозапчасти']/..//div[contains(@class, 'vz-icon mdi')]")


#  Блок "Стоимость"

displaying_the_currency_tenge_in_the_cost_block = SiteObjects(
    "Отображение валюты тенге в блоке 'Стоимость'",
    "(//div[@class='vz-personal-order-total-card-item'])[1]//span[contains(text(), 'тенге')]")

displaying_the_currency_ru_in_the_cost_block = SiteObjects(
    "Отображение валюты руб. в блоке 'Стоимость'",
    "(//div[@class='vz-personal-order-total-card-item'])[1]//span[contains(text(), '₽')]")

displaying_the_currency_bel_ru_in_the_cost_block = SiteObjects(
    "Отображение валюты тенге в блоке 'Стоимость'",
    "(//div[@class='vz-personal-order-total-card-item'])[1]//span[contains(text(), 'бел. руб')]")

displaying_the_total_currency_in_the_cost_block = SiteObjects(
    "Отображение валюты в блоке 'Стоимость' в 'Итого'",
    "//div[contains(., 'Итого: ')]//span[contains(@class, 'flex-nowrap')]")

displaying_the_cost_on_the_from_address_button_in_the_cost_block = SiteObjects(
    "Отображение валюты в кнопке 'Адрес' в отправке",
    "//div[contains(text(), 'Отправка')]/../..//span[contains(text(), 'Адрес')]")

displaying_the_cost_on_the_to_address_button_in_the_cost_block = SiteObjects(
    "Отображение валюты в кнопке 'Адрес' в отправке",
    "//div[contains(text(), 'Прибытие')]/../..//span[contains(text(), 'Адрес')]")

btn_currency_change_button_in_the_cost_block = SiteObjects(
    "Кнопка смены валюты в блоке 'Стоимость' в 'Итого'",
    "(//div[contains(text(), 'Итого')]/..//div[@class='vz-select-dropdown-value'])[1]")

btn_currency_change_ru_in_the_cost_block = SiteObjects(
    "Выбор валюты 'российский рубль' в блоке 'Стоимость' в 'Итого'",
    "(//div['vz-select-dropdown-list-item']//img[@class='vz-icon-masked' and @src='/svg/vz-russia-flag.svg'])[3]")

txt_the_payer_is_on_the_order_details_page = SiteObjects(
    "Текст 'Плательщиком является' на странице детализации заказа",
    "//span[contains(text(), 'Плательщиком заказа является')]")

txt_the_text_of_total_in_the_block_the_cost_in_the_order_details = SiteObjects(
    "Текст 'Всего' в блоке 'Стоимость' в детализации заказа",
    "//div[contains(text(), 'Всего')]")


# Блок Плательщик

btn_the_sender_button_in_the_payer_block = SiteObjects(
    "Кнопка 'Отправитель' в блоке 'Плательщик'",
    "//div[contains(@class, 'vz-switcher-item')]/span[contains(text(), 'Отправитель')]")

