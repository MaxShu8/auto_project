from site_objects import SiteObjects
from various_data import *


"""Элементы страницы \"Заказы\" """

input_number_of_order_on_orders_page = SiteObjects(
    "Поле 'Номер заказа' на странице 'Заказы'",
    "//input[@placeholder='Номер заказа']")

text_number_of_order_on_orders_page = SiteObjects(
    "Текст номера первого заказа на элементе 'Номер заказа' на странице 'Заказы'",
    "//label[@class='vz-tag-title']")

text_number_of_order_2_on_orders_page = SiteObjects(
    "Текст номера первого заказа на элементе 'Номер заказа' на странице 'Заказы'",
    "(//label[@class='vz-tag-title'])[2]")

btn_close_in_element_searching_number_of_order_on_orders_page = SiteObjects(
    "Кнопка 'Закрыть' в элементе поиска заказа на странице 'Заказы'",
    "//span[@class='mdi mdi-close vz-tag-close']")

btn_return_to_list_of_orders_on_orders_page = SiteObjects(
    "Кнопка 'Вернуться' в детализации заказа",
    "//span[contains(text(), 'К списку')]")

link_if_entering_an_invalid_number_of_order_on_orders_page = SiteObjects(
    "Текст при попытке ввода не того заказа в поле 'Номер заказа' на странице 'Заказы'",
    "//span[contains(text(), 'Вы пытаетесь найти заказ')]/a")

skeleton_of_order_on_orders_page = SiteObjects(
    "Скелетон на заказах на странице 'Заказы'",
    "//div[@class='vz-orders-skeleton']")

# Вкладки (Все В пути и т.д.)
tab_unpaid_in_the_list_of_orders_on_orders_page = SiteObjects(
    "Вкладка 'Неоплаченные' в списке заказов",
    "//div[contains(@class, 'vz-tabs-list-tab')]/span[contains(., 'Неоплаченные')]")

# Элементы на заказе
btn_cancel_order_button_in_the_order_list_page = SiteObjects(
    "Кнопка 'Отменить заказ' у заказа в списке заказов",
    "//div[@class='text-overflow text-body'][contains(text(), 'xxx')]/../../../..//button[@title='Отменить заказ']")

text_order_number_in_the_order_block_on_orders_page = SiteObjects(
    "Номер заказа в блоке заказа на странице 'Заказы'",
    "//div[@class='vz-order-item-meta']//div[@class='text-overflow text-body']")

text_order_number_in_the_order_block_on_orders_page_2 = SiteObjects(
    "Номер заказа в блоке заказа на странице 'Заказы' (заменяемый)",
    "//div[@class='text-overflow text-body'][contains(text(), 'xxx')]")

text_order_status_in_the_order_block_on_orders_page_x = SiteObjects(
    "Статус заказа в блоке заказа на странице 'Заказы' (заменяемый)",
    "//div[contains(., 'xxx')]/..//label[contains(., 'Отменён')]")






# btn_cancel_order_button_in_the_order_list_page = SiteObjects(
#     "Кнопка 'Отменить заказ' у заказа в списке заказов",
#     "//div[@class='text-overflow text-body'][contains(text(), 'xxx')]/../../../..//button[@title='Отменить заказ']")


# Попап "Отмена заказа"
text_cancellation_of_the_order_in_the_popup_of_the_order = SiteObjects(
    "Текст 'Отмена заказа' в попапе 'Отмена заказа'",
    "//span[contains(., 'Отмена заказа')]")

input_reason_for_cancellation_field_in_the_popup_cancellation = SiteObjects(
    "Поле 'Причина отмены' в попапе Отмена заказа",
    "//label[text()='Причина отмены']/..//textarea")

btn_send_in_the_popup_cancellation = SiteObjects(
    "Кнопка 'Отправить' в попапе Отмена заказа",
    "//span[contains(., 'Отправить')]")



