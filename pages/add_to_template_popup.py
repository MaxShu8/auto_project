from site_objects import SiteObjects


"""Элементы попапа формы \"Добавить в шаблон\""""

txt_add_to_template_on_the_add_to_template_popup = SiteObjects(
    "Заголовок Добавить в шаблоны в попапе шаблона",
    "//span[@class='vz-dialog-card-header-title']")

inp_enter_the_name_in_template_popup = SiteObjects(
    "Поле 'Введите название' в попапе добавления в шаблон",
    "//input[@placeholder='Введите название']")

btn_select_all_in_template_popup = SiteObjects(
    "Кнопка 'Выделить всё' в попапе добавления в шаблон",
    "//a[text()='Выделить всё']")

btn_add_and_go_to_template_in_template_popup = SiteObjects(
    "Кнопка 'Добавить и перейти к шаблону' в попапе добавления в шаблон",
    "//button[@class='vz-button primary outline big']")




