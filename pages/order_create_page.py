from site_objects import SiteObjects


"""Элементы страницы \"Расчет и оформление заказа\""""

btn_calculate_in_the_header = SiteObjects(
    "Кнопка 'Рассчитать' на странице 'Расчет и оформление заказа'",
    "(//span[text()='Рассчитать'])[1]")

txt_order_in_calculation_and_ordering_page = SiteObjects(
    "Текст 'Заказ' на странице 'Расчет и оформление заказа'",
    "//span[text()='Заказ']")

skeleton_after_push_the_btn_create_order = SiteObjects(
    "Скелетон в номере заказа после создания заказа",
    "//div[@class='w-20 mr-auto']/div[contains(@class, 'vz-skeleton vz-skeleton-animated')]")


"""Блок Направление"""
# Отправка
input_from_terminal_in_create_order_page = SiteObjects(
    "Инпут с адресом терминала (от) в создании заказа",
    "(//div[contains(text(), 'Отправка')]/../..//label[contains(text(), 'Терминал')]/..//span)[1]")

input_to_terminal_in_create_order_page = SiteObjects(
    "Инпут с адресом терминала (до) в создании заказа",
    "(//div[contains(text(), 'Прибытие')]/../..//label[contains(text(), 'Терминал')]/..//span)[1]")

btn_dispatch_address = SiteObjects(
    "Кнопка 'Адрес' в отправке в создании заказа",
    "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]/..")

btn_dispatch_terminal = SiteObjects(
    "Кнопка 'Терминал' в отправке в создании заказа",
    "//div[contains(text(),'Отправка')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]/..")

active_btn_dispatch_terminal_or_address = SiteObjects(
    "Кнопка 'Терминал' в отправке в создании заказа",
    "//div[contains(text(),'Отправка')]/../..//div[contains(@class, 'vz-switcher-item')]")

btn_calendar_in_dispatch_block = SiteObjects(
    "Кнопка 'Календарь' в отправке в создании заказа",
    "//div[text()='Отправка']/../..//span[text()='Календарь']")

text_in_calendar_in_dispatch_block = SiteObjects(
    "Текст Пн в календаре в отправке в создании заказа",
    "//div[text()='Отправка']/../..//span[text()='пн']")

btn_in_calendar_day_selected_dispatch_block = SiteObjects(
    "Кнопка текущей/выбранной даты в календаре в отправке в создании заказа",
    "//div[text()='Отправка']/../..//div[contains(@class, 'day selected')]/span")

btn_in_calendar_day_to_choice_dispatch_block = SiteObjects(
    "Кнопка следующей активной даты в календаре в отправке в создании заказа",
    "//div[text()='Отправка']/../..//div[@class='day']/span")

# Дата
choice_the_another_date_in_the_dispatch_calendar_in_create_order_page_x = SiteObjects(
    "Дата в календаре в Отправка (заменяемый)",
    "//div[text()='Отправка']/../../..//div[@class='day']/span[contains(text(), 'xxx')]")

choice_the_active_date_in_the_sending_feed_in_create_order_page = SiteObjects(
    "Активная дата в ленте в Отправка",
    "//div[text()='Отправка']/../../..//div[contains(@class, 'vz-direction-calendar-calendar-slider-day active')]/div[1]/..")

choice_the_another_date_in_the_sending_feed_in_create_order_page = SiteObjects(
    "Другая дата в ленте в Отправка",
    "//div[@class='vz-direction-calendar-calendar-slider-day']/div[1]")

choice_the_another_date_in_the_sending_feed_in_create_order_page_x = SiteObjects(
    "Неактивная дата в ленте в Отправка (заменяемый)",
    "//div[text()='Отправка']/../../..//div[contains(@class, 'vz-direction-calendar-calendar-slider-day') and @data-text='xxx']")

choice_us_item_from_drop_down_list_in_dispatch_in_create_order_page = SiteObjects(
    "Выбор нас.пункта из выпадающего списка в Отправка (заменяемый)",
    "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll vz-new-autocomplete-list')]//div[contains(@class, 'vz-new-autocomplete-list-item')]//div[contains(text(), 'xxx')]/..")

# Время
input_time_from_dispatch_terminal_in_create_order_page = SiteObjects(
    "Время в 'Прибытие' в поле Время при отправке с терминала",
    "//div[text()='Отправка']/../..//div[contains(text(), 'Время')]/..//span[text()='до']/..//div[contains(@class, 'vz-select-dropdown-value')]/span")

input_time_from_dispatch_in_create_order_page = SiteObjects(
    "Инпут с выбором времени 'с' в отправке в создании заказа",
    "//div[text()='Отправка']/../..//div[contains(text(), 'Время')]/../..//span[text()='с']/..//div[contains(@class, 'vz-select-dropdown-value')]/span")

input_time_to_dispatch_in_create_order_page = SiteObjects(
    "Инпут с выбором времени 'до' в отправке в создании заказа",
    "(//div[text()='Отправка']/../..//div[contains(text(), 'Время')]/../..//span[text()='до']/..//div[contains(@class, 'vz-select-dropdown-value')]/span)[2]")

btn_choice_morning_time_in_dropdown_dispatch = SiteObjects(
    "Утреннее время в 'Отправка' (первое)",
    "//img[@class='vz-icon-masked'][@src='/svg/morning.svg']/../../span")

btn_choice_last_morning_time_in_dropdown_dispatch = SiteObjects(
    "Утреннее время в 'Отправка' (последнее)",
    "(//img[@class='vz-icon-masked'][@src='/svg/morning.svg']/../../span)[last()]")

btn_choice_evening_time_in_dropdown_dispatch = SiteObjects(
    "Вечернее время в 'Отправка' (последний элемент)",
    "(//img[@class='vz-icon-masked'][@src='/svg/evening.svg']/../../span)[last()]")

btn_choice_default_time_in_dropdown_dispatch = SiteObjects(
    "Дефолтное время в 'Отправка'",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]//span")

btn_choice_default_time_in_dropdown_dispatch_x = SiteObjects(
    "Дефолтное время в 'Отправка' (заменяемый)",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]//span[contains(text(), 'xxx')]")


"""Прибытие"""

input_timing_from_destination_in_create_order_page = SiteObjects(
    "Инпут с выбором времени 'с' в прибытии в создании заказа",
    "(//span[text()='с']/..//span[contains(@class, 'vz-select-dropdown-value-title')])[3]")

input_timing_to_destination_in_create_order_page = SiteObjects(
    "Инпут с выбором времени 'с' в прибытии в создании заказа",
    "(//span[text()='с']/..//span[contains(@class, 'vz-select-dropdown-value-title')])[4]")

choice_pvz_point_in_destination_in_create_order_page = SiteObjects(
    "Выбор пункта ПВЗ в прибытии в создании заказа (заменяемый)",
    "//div[text()='xxx']")

choice_us_item_from_drop_down_list_in_destination_in_create_order_page = SiteObjects(
    "Выбор нас.пункта из выпадающего списка в Отправка (заменяемый)",
    "//div[contains(@class, 'vz-new-autocomplete-list vz-scroll vz-new-autocomplete-list')]//div[contains(@class, 'vz-new-autocomplete-list-item')]//div[contains(text(), 'xxx')]/..")

active_btn_destination_terminal_or_address = SiteObjects(
    "Кнопка 'Терминал' в прибытии в создании заказа",
    "//div[contains(text(),'Прибытие')]/../..//div[contains(@class, 'vz-switcher-item')]")

btn_destination_address = SiteObjects(
    "Кнопка 'Адрес' в прибытии в создании заказа",
    "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Адрес')]/..")

btn_destination_terminal = SiteObjects(
    "Кнопка 'Терминал' в прибытии в создании заказа",
    "//div[contains(text(),'Прибытие')]/ancestor::div[@class='vz-direction-card']//span[contains(text(),'Терминал')]/..")

btn_calendar_in_destination_block = SiteObjects(
    "Кнопка 'Календарь' в прибытии в создании заказа",
    "//div[text()='Прибытие']/../../..//span[text()='Календарь']")

text_in_calendar_in_destination_block = SiteObjects(
    "Текст Пн в календаре в прибытии в создании заказа",
    "//div[text()='Прибытие']/../../..//span[text()='пн']")

btn_in_calendar_day_selected_destination_block = SiteObjects(
    "Кнопка текущей/выбранной даты в календаре в прибытии в создании заказа",
    "//div[text()='Прибытие']/../../..//div[contains(@class, 'day selected')]/span")

btn_in_calendar_day_to_choice_destination_block = SiteObjects(
    "Кнопка следующей активной даты в календаре в прибытии в создании заказа",
    "//div[text()='Прибытие']/../../..//div[@class='day']/span")

btn_in_calendar_day_to_choice_with_status_destination_block = SiteObjects(
    "Кнопка следующей активной даты (со статусом) в календаре в прибытии в создании заказа",
    "//div[text()='Прибытие']/../../..//div[@class='day discount']/span")


# Дата
choice_the_another_date_in_the_destination_calendar_in_create_order_page_x = SiteObjects(
    "Дата в календаре в Отправка (заменяемый)",
    "//div[text()='Прибытие']/../../..//div[@class='day']/span[contains(text(), 'xxx')]")

btn_active_date_in_the_send_in_the_calendar = SiteObjects(
    "Активная дата в 'Отправка' в календаре",
    "(//div[contains(@class, 'vz-direction-calendar-calendar-slider')]/div[contains(@class, 'active')])[1]")

btn_active_date_in_the_arrival_in_the_calendar = SiteObjects(
    "Активная дата в 'Прибытие' в календаре",
    "(//div[contains(@class, 'vz-direction-calendar-calendar-slider')]/div[contains(@class, 'active')])[2]")


# Время
input_time_from_destination_in_create_order_page = SiteObjects(
    "Активное время в 'Прибытие' в поле Время",
    "(//div[text()='Прибытие']/../../..//div[contains(text(), 'Время')]/..//span[text()='с']/..//div[contains(@class, 'vz-select-dropdown-value')]/span)[1]")

input_time_destination_in_create_order_page = SiteObjects(
    "Активное время в 'Прибытие' в поле Время",
    "(//div[text()='Прибытие']/../../..//div[contains(text(), 'Время')]/..//span[text()='с']/..//div[contains(@class, 'vz-select-dropdown-value')]/span)[2]")

btn_choice_morning_time_in_dropdown_destination = SiteObjects(
    "Утреннее время в 'Прибытие'",
    "//img[@class='vz-icon-masked'][@src='/svg/morning.svg']/../../span")

checkbox_fixed_time_dispatch_in_create_order_page = SiteObjects(
    "Чек-бокс 'Фиксированное время' в отправке при создании заказа",
    "(//div[contains(text(), 'Фиксированное')]/../div)[1]")

checkbox_fixed_time_destination_in_create_order_page = SiteObjects(
    "Чек-бокс 'Фиксированное время' в прибытии при создании заказа",
    "//div[text()='Прибытие']/../../..//div[contains(text(), 'Фиксированное')]/../div")


# Выбор времени ожидания
input_waiting_time_dispatch_in_create_order_page = SiteObjects(
    "Инпут с выбором времени ожидания в отправке в создании заказа",
    "(//div[text()='Время ожидания']/../..//span[contains(@class, 'vz-select-dropdown-value-title')])[1]")

input_waiting_time_destination_in_create_order_page = SiteObjects(
    "Инпут с выбором времени ожидания в отправке в создании заказа",
    "(//div[text()='Время ожидания']/../..//span[contains(@class, 'vz-select-dropdown-value-title')])[2]")

btn_waiting_time_dispatch_2_hours = SiteObjects(
    "Кнопка '2 часа' в списке времени ожидания в создании заказа",
    "//div[@class='vz-select-dropdown-list vz-scroll open']//span[contains(text(), '2 часа')]")


# Выбор даты (Лента/Календарь)
choice_the_active_date_in_the_arrival_feed_in_create_order_page = SiteObjects(
    "Активная дата в ленте в прибытии",
    "//div[text()='Прибытие']/../../..//div[contains(@class, 'vz-direction-calendar-calendar-slider-day active')]/div[1]")

choice_the_another_date_in_the_arrival_feed_in_create_order_page = SiteObjects(
    "Другая дата (без статуса) в ленте в прибытии",
    "//div[text()='Прибытие']/../../..//div[@class='vz-direction-calendar-calendar-slider-day']/div[1]")

choice_the_another_date_with_status_in_the_arrival_feed_in_create_order_page = SiteObjects(
    "Другая дата (со статусом) в ленте в прибытии",
    "//div[text()='Прибытие']/../../..//div[@class='vz-direction-calendar-calendar-slider-day discount']/div[1]")

choice_the_another_date_disabled_in_the_arrival_feed_in_create_order_page = SiteObjects(
    "Неактивная дата в ленте в прибытии",
    "//div[text()='Прибытие']/../../..//div[@class='vz-direction-calendar-calendar-slider-day disabled']/div[1]")

choice_the_another_date_in_the_arrival_feed_in_create_order_page_x = SiteObjects(
    "Неактивная дата в ленте в прибытии (заменяемый)",
    "//div[text()='Прибытие']/../../..//div[contains(@class, 'vz-direction-calendar-calendar-slider-day') and @data-text='xxx']")


"""Блок Груз"""
# Максимальные габариты одного груза
inp_length_field_in_the_maximum_dimensions_of_one_place_create_order_page = SiteObjects(
    "Поле 'Длина' в Максимальные габариты одного места на странице 'Расчет и оформление заказа'",
    "//label[text()='Длина']/..//input")

inp_width_field_in_the_maximum_dimensions_of_one_place_create_order_page = SiteObjects(
    "Поле 'Ширина' в Максимальные габариты одного места на странице 'Расчет и оформление заказа'",
    "//label[text()='Ширина']/..//input")

inp_height_field_in_the_maximum_dimensions_of_one_place_create_order_page = SiteObjects(
    "Поле 'Высота' в Максимальные габариты одного места на странице 'Расчет и оформление заказа'",
    "//span[text()='Высота']/..//input")

inp_weight_field_in_the_maximum_dimensions_of_one_place_create_order_page = SiteObjects(
    "Поле 'Вес' в Максимальные габариты одного места на странице 'Расчет и оформление заказа'",
    "(//span[text()='Вес']/..//input)[2]")

inp_insurance_create_order_page = SiteObjects(
    "Поле 'Страхование' на странице 'Расчет и оформление заказа'",
    "//label[contains(text(), 'Страхование')]/../div[@class='vz-select-dropdown-value big']")

choice_without_the_declared_insurance_cost_create_order_page = SiteObjects(
    "Страхование 'Без объявленной стоимости' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]/span[contains(text(), 'Без объявленной стоимости')]")

text_without_the_declared_insurance_cost_create_order_page = SiteObjects(
    "Вид указанного страхования 'Без объявленной стоимости' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]/span[contains(text(), 'Без объявленной стоимости')]/..")

choice_without_insurance_create_order_page = SiteObjects(
    "Страхование 'Без страхования' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]/span[contains(text(), 'Без страхования')]")

choice_with_insurance_create_order_page = SiteObjects(
    "Страхование 'Страхование груза' на странице 'Расчет и оформление заказа'",
    "//div[contains(@class, 'vz-select-dropdown-list-item')]/span[contains(text(), 'Страхование груза')]")

inp_amount_for_specifying_the_insurance_amount_create_order_page = SiteObjects(
    "Поле 'Сумма' для указания суммы страхования на странице 'Расчет и оформление заказа'",
    "//label[contains(text(), 'Сумма')]/..//input")

txt_type_of_insurance_create_order_page = SiteObjects(
    "Вид страхования на странице 'Расчет и оформление заказа'",
    "//label[contains(text(), 'Страхование')]/../div[contains(@class, 'vz-select-dropdown-value')]/..//span")


# Категория груза
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


# Упаковка
btn_add_button_packaging_create_order_page = SiteObjects(
    "Кнопка 'Добавить' (упаковку) при оформлении заказа",
    "//div[contains(text(), 'Упаковка')]/..//span")

checkbox_pallet_board_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Паллетный борт' в модалке Вид упаковки",
    "//span[text()='Паллетный борт']")

checkbox_protective_rigid_packaging_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Защитная жёсткая упаковка' в модалке Вид упаковки",
    "//span[text()='Защитная жёсткая упаковка']")

checkbox_protective_rigid_packaging_photo_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Защитная жёсткая упаковка' в модалке Вид упаковки",
    "//span[text()='Защитная жёсткая упаковка (+ фото)']")

checkbox_palletizing_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Паллетирование' в модалке Вид упаковки",
    "//span[text()='Паллетирование']")

checkbox_palletizing_at_the_pick_up_terminal_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Паллетирование на терминале выдачи' в модалке Вид упаковки",
    "//span[text()='Паллетирование на терминале выдачи']")


# Доп. упаковка
checkbox_additional_packaging_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Дополнительная упаковка' в модалке Вид упаковки",
    "//span[text()='Дополнительная упаковка']")

radiobtn_transparent_film_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Радиокнопка 'Прозрачная пленка' в модалке Вид упаковки",
    "//span[text()='Дополнительная упаковка']/../../..//span[text()='Прозрачная плёнка']")

radiobtn_black_film_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Радиокнопка 'Черная пленка' в модалке Вид упаковки",
    "//span[text()='Дополнительная упаковка']/../../..//span[text()='Чёрная плёнка']")

radiobtn_air_bubble_film_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Радиокнопка 'Воздушно-пузырьковая пленка' в модалке Вид упаковки",
    "//span[text()='Дополнительная упаковка']/../../..//span[text()='Воздушно-пузырьковая пленка']")

radiobtn_paperboard_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Радиокнопка 'Картон' в модалке Вид упаковки",
    "//span[text()='Дополнительная упаковка']/../../..//span[text()='Картон']")


# Коробки
checkbox_boxes_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Коробки' в модалке Вид упаковки",
    "//span[text()='Коробки']")

input_choice_of_boxes_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Инпут 'Коробка ...' в модалке Вид упаковки",
    "//span[@class='vz-select-dropdown-value-title'][contains(., 'Коробка')]")

choice_of_box_60_40_40_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Выбор коробки 'Коробка 60х40х40' в модалке Вид упаковки",
    "//span[@class='vz-select-dropdown-list-item-title'][contains(., 'Коробка 60×40×40')]")


# Мешки
checkbox_bags_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Мешки' в модалке Вид упаковки",
    "//span[text()='Мешки']")


# Сейф-пакет
checkbox_safe_package_in_the_modal_type_of_packaging_create_order_page = SiteObjects(
    "Чек-бокс 'Сейф-пакет' в модалке Вид упаковки",
    "//span[text()='Упаковка в сейф-пакет']")

btn_apply_in_the_package_view_modal_create_order_page = SiteObjects(
    "Кнопка 'Применить' в модалке Вид упаковки при оформлении заказа",
    "//button[@class='vz-button primary big flex-center']//span[contains(., 'Применить')]")

list_block_with_packaging_elements_in_create_order_page = SiteObjects(
    "Блок с элементами упаковок при оформлении заказа",
    "//label[contains(text(), 'Вид упаковки')]/../div[@class='vz-input-wrapper']/input")


# Страхование груза
btn_insurance_field_in_the_create_order_form = SiteObjects(
    "Поле 'Страхование' в оформлении заказа",
    "//label[contains(text(), 'Страхование')]/../div[@class='vz-select-dropdown-value big']/span")

btn_choosing_cargo_insurance_in_insurance_block_in_create_order_form = SiteObjects(
    "Выбор 'Страхование груза' в Страховании при оформлении заказа",
    "//div[@class='vz-select-dropdown-list-item big']/span[contains(text(), 'Страхование груза')]")

inp_amount_field_in_the_insurance_in_create_order_form = SiteObjects(
    "Поле 'Сумма' в Страховании при оформлении заказа",
    "//label[contains(text(), 'Сумма')]/..//input[contains(@class, 'vz-input-control big')]")


# Номер перевозки
inp_field_is_your_transportation_number_in_create_order_form = SiteObjects(
    "Поле 'Ваш номер перевозки' при оформлении заказа",
    "//textarea[@placeholder='Номер перевозки']")


"""Блок Доп.услуги"""
checkbox_scan_of_the_delivery_invoice_in_the_add_on_block_services_create_order_page = SiteObjects(
    "Чек-бокс 'Скан накладной на выдачу' в блоке доп.услуги",
    "//span[contains(text(), 'Скан накладной на выдачу')]")

checkbox_return_the_accompanying_documents_in_the_add_on_block_services_create_order_page = SiteObjects(
    "Чек-бокс 'Вернуть сопроводительные документы' в блоке доп.услуги",
    "//span[contains(text(), 'Вернуть сопроводительные документы')]")

checkbox_disassembly_of_packaging_upon_delivery_to_the_address_on_block_services_create_order_page = SiteObjects(
    "Чек-бокс 'Разбор упаковки при доставке до адреса' в блоке доп.услуги",
    "//span[contains(text(), 'Разбор упаковки при доставке до адреса')]")

btn_terminal_in_the_additional_services_section_in_create_order_form = SiteObjects(
    "Кнопка 'Терминал' в блоке Доп.услуги при оформлении заказа",
    "//span[contains(text(), 'Вернуть сопроводительные документы')]/../../../..//span[contains(text(), 'Терминал')]")


"""Блок Плательщик"""
btn_the_sender_button_in_the_payer_block = SiteObjects(
    "Кнопка 'Отправитель' в блоке 'Плательщик'",
    "//div[contains(@class, 'vz-switcher-item')]/span[contains(text(), 'Отправитель')]")

btn_recipient_in_the_payer_block_in_create_order_form = SiteObjects(
    "Кнопка 'Получатель' в блоке Плательщик при оформлении заказа",
    "//div[contains(@class, 'vz-switcher-item')]/span[contains(text(), 'Получатель')]")


"""Блок Участники"""
# Отправитель физ. лицо
btn_type_ind_sender = SiteObjects(
    "Кнопка 'Физ.лицо' у отправителя",
    "//span[text()='Отправитель']/../..//span[contains(text(),'Физическое лицо')]/..")

input_fio_ind_sender = SiteObjects(
    "Поле ФИО у отправителя физ.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'ФИО')]/..//input")

input_phone_ind_sender = SiteObjects(
    "Поле Телефон у отправителя физ.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")

input_add_phone_ind_sender = SiteObjects(
    "Кнопка доп. телефон у отправителя физ.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'+ Доп. номер')]")

input_email_ind_sender = SiteObjects(
    "Поле email у отправителя физ.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Email')]/..//input")

checkbox_send_code_ind_sender = SiteObjects(
    "Поле email у отправителя физ.лицо",
    "//span[text()='Отправитель']/../..//span[contains(text(),'Отправить код получения')]/preceding-sibling::div")

list_fio_ka_sender = SiteObjects(
    "Список всех КА",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")

choice_name_ka_in_drop_down_list_of_companies_create_order_page = SiteObjects(
    "Выбор по имени физ.лица в выпадающем списке компаний",
    "//div[@class='vz-new-autocomplete-list-item-title'][contains(text(), 'xxx')]")


# Получатель физ. лицо
btn_type_ind_recipient = SiteObjects(
    "Кнопка 'Физ.лицо' у получателя",
    "//span[text()='Получатель']/../..//span[contains(text(),'Физическое лицо')]/..")

input_fio_ind_recipient = SiteObjects(
    "Поле ФИО у получателя физ.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'ФИО')]/..//input")

input_phone_ind_recipient = SiteObjects(
    "Поле Телефон у получателя физ.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'Телефон')]/..//input")

input_add_phone_ind_recipient = SiteObjects(
    "Кнопка доп. телефон у отправителя физ.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'+ Доп. номер')]")

input_email_ind_recipient = SiteObjects(
    "Поле email у отправителя физ.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'Email')]/..//input")

checkbox_send_code_ind_recipient = SiteObjects(
    "Поле email у отправителя физ.лицо",
    "//span[text()='Получатель']/../..//span[contains(text(),'Отправить код получения')]/preceding-sibling::div")


# Отправитель юр. лицо
btn_type_corp_sender = SiteObjects(
    "Кнопка 'Юр.лицо' у отправителя",
    "//span[text()='Отправитель']/../..//span[contains(text(),'Юридическое лицо')]/..")

input_name_corp_sender = SiteObjects(
    "Инпут 'Наименование компании' у отправителя юр.лица",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Наименование компании')]/..//input")

input_phone_corp_sender = SiteObjects(
    "Поле Телефон у отправителя юр.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Телефон')]/..//input")

input_additional_phone_corp_sender = SiteObjects(
    "Кнопка доп. телефон у отправителя юр.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'+ Доп. номер')]")

input_email_corp_sender = SiteObjects(
    "Поле ФИО у получателя юр.лицо",
    "//span[text()='Отправитель']/../..//label[contains(text(),'Email')]/..//input")

choice_company_in_drop_down_list_of_companies_create_order_page = SiteObjects(
    "Выбор по ИНН компании в выпадающем списке компаний",
    "//div[@class='vz-new-autocomplete-list-item-description'][contains(text(), 'xxx')]")


# Получатель юр. лицо
btn_country_selection_flag_corp_recipient = SiteObjects(
    "Кнопка выбора страны (флаг) у 'Юр.лицо' у получателя",
    "//span[contains(., 'Получатель')]/..//span[@class='vz-select-dropdown-value-title']/..")

btn_country_selection_flag_ru_corp_recipient = SiteObjects(
    "Кнопка выбора страны Россия (флаг) у 'Юр.лицо' у получателя",
    "//img[@src='/svg/vz-russia-flag.svg']/../ancestor::div[contains(@class, 'vz-select-dropdown-list-item')]")

input_fio_corp_recipient = SiteObjects(
    "Поле ФИО у получателя юр.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'ФИО')]/..//input")

input_phone_corp_recipient = SiteObjects(
    "Поле Телефон у получателя юр.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'Телефон')]/..//input")

input_email_corp_recipient = SiteObjects(
    "Поле ФИО у получателя юр.лицо",
    "//span[text()='Получатель']/../..//label[contains(text(),'Email')]/..//input")


"""Блок Стоимость"""
# Услуги
text_morning_pick_up_service_in_the_cost_block = SiteObjects(
    "Услуга Утренний забор в блоке Стоимость",
    "//div[contains(@class, 'vz-order-total-price')]//span[contains(@title, 'Утренний забор')]")

text_evening_pick_up_service_in_the_cost_block = SiteObjects(
    "Услуга Вечерний забор в блоке Стоимость",
    "//div[contains(@class, 'vz-order-total-price')]//span[contains(@title, 'Вечерний забор')]")

text_fixed_time_service_from_in_the_cost_block = SiteObjects(
    "Услуга Фиксированное время забора в блоке Стоимость",
    "//div[contains(@class, 'vz-order-total-price')]//span[contains(@title, 'Фиксированное время забора')]")

text_fixed_time_service_to_in_the_cost_block = SiteObjects(
    "Услуга Фиксированное время отвоза в блоке Стоимость",
    "//div[contains(@class, 'vz-order-total-price')]//span[contains(@title, 'Фиксированное время доставки')]")


# Валюты
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
    "//div[@class='vz-select-dropdown-list vz-scroll open vz-order-total-price-cost-country-list']/div[contains(@class, 'vz-select-dropdown-list-item')]//img[@class='vz-icon-masked' and @src='/svg/vz-russia-flag.svg']")

txt_the_payer_is_on_the_order_details_page = SiteObjects(
    "Текст 'Плательщиком является' на странице детализации заказа",
    "//span[contains(text(), 'Плательщиком заказа является')]")

txt_the_text_of_total_in_the_block_the_cost_in_the_order_details = SiteObjects(
    "Текст 'Всего' в блоке 'Стоимость' в детализации заказа",
    "//div[contains(text(), 'Всего')]")

txt_currency_confirmation_header_in_the_currency_confirmation_popup = SiteObjects(
    "Заголовок 'Подтверждение валюты' в попапе 'Подтверждение валюты'",
    "//span[@title='Подтверждение валюты']")

btn_confirm_in_the_currency_confirmation_popup = SiteObjects(
    "Кнопка 'Подтвердить' в попапе 'Подтверждение валюты'",
    "//button[text()='Подтвердить']")




