from site_objects import SiteObjects


"""Элементы страницы 'Детализация заказа'"""

data_individual_number_of_order_in_details_page = SiteObjects(
    "Данные - индивидуальный номер заказа",
    "//div[@class='vz-individual-order-header-label-wrapper']/span/span")

btn_create_based_on_in_details_page = SiteObjects(
    "Кнопка 'Создать на основе' в детализации заказа",
    "//span[contains(text(), 'Создать на основе')]")

btn_cancel_order_on_in_details_page = SiteObjects(
    "Кнопка 'Отменить заказ' в детализации заказа",
    "//span[contains(text(), 'Отменить заказ')]")


"""Блок Направление"""

# Отправка
data_dispatch_us_point_terminal_address_in_details_page = SiteObjects(
    "Данные - терминал, нас.пункт, адрес терминала",
    "(//div[contains(text(),'Отправка')]/..//div/span)[1]")

data_dispatch_date_of_order_in_details_page = SiteObjects(
    "Данные - дата заказа в детализации",
    "(//div[contains(text(),'Отправка')]/..//div/span)[2]")

data_dispatch_time_of_delivery_in_details_page = SiteObjects(
    "Данные - дата заказа в детализации",
    "(//div[contains(text(),'Отправка')]/..//div/span)[3]")

# Прибытие
data_destination_us_point_terminal_address_in_details_page = SiteObjects(
    "Данные - терминал, нас.пункт, адрес терминала",
    "(//div[contains(text(),'Прибытие')]/..//div/span)[1]")

data_destination_date_of_order_in_details_page = SiteObjects(
    "Данные - дата заказа в детализации",
    "(//div[contains(text(),'Прибытие')]/..//div/span)[2]")

data_destination_time_of_delivery_in_details_page = SiteObjects(
    "Данные - дата заказа в детализации",
    "(//div[contains(text(),'Прибытие')]/..//div/span)[3]")


"""Блок Груз"""

# Общие габариты
data_volume_in_the_total_dimensions_of_the_cargo_in_details_page = SiteObjects(
    "Данные - объем в общих габаритах груза блока груз",
    "//div[contains(text(), 'Объем')]/span[contains(@class, 'vz-cargo-view-item-value')]")

data_weight_in_the_total_dimensions_of_the_cargo_in_details_page = SiteObjects(
    "Данные - вес в общих габаритах груза блока груз",
    "(//div[contains(text(), 'Вес')]/span[contains(@class, 'vz-cargo-view-item-value')])[1]")

data_places_in_the_total_dimensions_of_the_cargo_in_details_page = SiteObjects(
    "Данные - мест в общих габаритах груза блока груз",
    "//div[contains(text(), 'Мест')]/span[contains(@class, 'vz-cargo-view-item-value')]")

# Максимальные габариты одного места
data_length_in_the_maximum_seat_dimensions_in_details_page = SiteObjects(
    "Данные - длина в максимальных габаритах места блока груз",
    "//div[contains(text(), 'Длина')]/span[contains(@class, 'vz-cargo-view-item-value')]")

data_width_in_the_maximum_seat_dimensions_in_details_page = SiteObjects(
    "Данные - ширина в максимальных габаритах места блока груз",
    "//div[contains(text(), 'Ширина')]/span[contains(@class, 'vz-cargo-view-item-value')]")

data_height_in_the_maximum_seat_dimensions_in_details_page = SiteObjects(
    "Данные - высота в максимальных габаритах места блока груз",
    "//div[contains(text(), 'Высота')]/span[contains(@class, 'vz-cargo-view-item-value')]")

data_weight_in_the_maximum_seat_dimensions_in_details_page = SiteObjects(
    "Данные - вес в максимальных габаритах места блока груз",
    "(//div[contains(text(), 'Вес')]/span[contains(@class, 'vz-cargo-view-item-value')])[2]")

# Категория груза
data_cargo_category_of_the_cargo_block_in_details_page = SiteObjects(
    "Данные - категория груза блока Груз",
    "//div[contains(text(), 'Категория груза')]/../span[contains(@class, 'vz-cargo-view-item-list')]")

# Упаковка груза
data_cargo_package_in_the_cargo_block_in_details_page = SiteObjects(
    "Данные - упаковка груза в блоке Груз",
    "//div[@class='mt-10']/div[contains(text(), 'Вид упаковки')]")

# Страхование груза
data_cargo_insurance_in_the_cargo_block_in_details_page = SiteObjects(
    "Данные - страхование груза в блоке Груз",
    "//div[contains(text(), 'Сумма')]/../span[contains(@class, 'vz-cargo-view-item-value')]")


"""Блок Доп.услуги"""

data_scan_of_the_delivery_invoice_in_details_page = SiteObjects(
    "Данные - скан накладной на выдачу в блоке доп. услуги",
    "//span[text()='Скан накладной на выдачу']")

data_accompanying_documents_in_details_page = SiteObjects(
    "Данные - сопроводительные документы в блоке доп. услуги",
    "//span[contains(text(), 'Вернуть сопроводительные документы')]")


"""Блок Участники"""

# Отправитель
data_fio_sender_in_details_page = SiteObjects(
    "Данные - ФИО отправителя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'ФИО')])[1]")

data_phone_sender_in_details_page = SiteObjects(
    "Данные - телефон отправителя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'Телефон')])[1]")

data_send_code_sender_in_details_page = SiteObjects(
    "Данные - код получения для отправителя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'Код получения')])[1]")

data_signature_of_the_payer_at_the_sender_in_details_page = SiteObjects(
    "Данные - подпись плательщика у получателя",
    "//label[contains(., 'Плательщик')]/../span")


# Получатель
data_fio_recipient_in_details_page = SiteObjects(
    "Данные - ФИО получателя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'ФИО')])[2]")

data_phone_recipient_in_details_page = SiteObjects(
    "Данные - телефон получателя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'Телефон')])[2]")

data_send_code_recipient_in_details_page = SiteObjects(
    "Данные - код получения для получателя",
    "(//div[contains(text(), 'Участники')]/..//div[@class='vz-customer-view']//span[contains(text(), 'Код получения')])[2]")













