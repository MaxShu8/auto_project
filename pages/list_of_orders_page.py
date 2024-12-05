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



