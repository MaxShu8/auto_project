import datetime
import time
import pytest
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from Telegram import *
from Settings import *

# фоновый режим без отрисовки UI
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#, options=chrome_options

# Прикрутим драйвер-менеджер для автообновления драйвера
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(5)
# driver.maximize_window()

# driver.get('https://vozovoz.dev/')


@pytest.fixture()
def driver_start():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://vozovoz.dev/')
    return driver


def test_check_authorization(driver):
    description = 'Проверка авторизации'

    try:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '//div[@class="flex flex-align-items-center"]//div[@class="public-header-button-personal-text text-overflow"][contains(text(),"Личный кабинет")]')))
        time.sleep(2)
        btn_personal = driver.find_element(By.XPATH, '//div[@class="flex flex-align-items-center"]//div[@class="public-header-button-personal-text text-overflow"][contains(text(),"Личный кабинет")]')
        btn_personal.click()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон или E-mail*']")))

        inp_login = driver.find_element(By.XPATH, "//input[@placeholder='Телефон или E-mail*']")
        inp_login.send_keys('79990220038')

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='vz-button primary large flex flex-center login-button']//span[@class='vz-button-title']/..")))
        btn_continue = driver.find_element(By.XPATH, "//button[@class='vz-button primary large flex flex-center login-button']//span[@class='vz-button-title']/..")
        btn_continue.click()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль*']")))
        inp_login = driver.find_element(By.XPATH, "//input[@placeholder='Пароль*']")
        inp_login.send_keys('123123')
        btn_login = driver.find_element(By.XPATH, "//button[@class='vz-button primary large']//span[@class='vz-button-title']")
        btn_login.click()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//img[contains(@src,'/svg/logo/vz-logo-white.svg')]")))

        send_message_tg(f'Тест: "{description}" - успешно пройден!\nДата: {data_event()}')

    except Exception as e:

        send_message_tg(f'Произошла ошибка в тесте\n{e}')
        print(f"Произошла ошибка в тесте: {description}\n{e}")
        pass

    finally:
        driver.close()
        driver.quit()


def check_create_order():
    description = 'Проверка создания заказа'

    try:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                        '//div[@class="flex flex-align-items-center"]//div[@class="public-header-button-personal-text text-overflow"][contains(text(),"Личный кабинет")]')))

        btn_personal = driver.find_element(By.XPATH,
                                           '//div[@class="flex flex-align-items-center"]//div[@class="public-header-button-personal-text text-overflow"][contains(text(),"Личный кабинет")]')
        btn_personal.click()

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Телефон или E-mail*']")))

        inp_login = driver.find_element(By.XPATH, "//input[@placeholder='Телефон или E-mail*']")
        inp_login.send_keys('79990220038')

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                        "//button[@class='vz-button primary large flex flex-center login-button']//span[@class='vz-button-title']/..")))
        btn_continue = driver.find_element(By.XPATH,
                                           "//button[@class='vz-button primary large flex flex-center login-button']//span[@class='vz-button-title']/..")
        btn_continue.click()

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль*']")))
        inp_login = driver.find_element(By.XPATH, "//input[@placeholder='Пароль*']")
        inp_login.send_keys('123123')

        btn_login = driver.find_element(By.XPATH,
                                        "//button[@class='vz-button primary large']//span[@class='vz-button-title']")
        btn_login.click()

        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/personal/order/create/']")))
        create_order_btn = driver.find_element(By.XPATH, "//a[@href='/personal/order/create/']")
        create_order_btn.click()

    except Exception as e:

        # send_message_tg(f'Произошла ошибка в тесте\n{e}')
        print(f"Произошла ошибка в тесте: {description}\n{e}")

    finally:
        driver.close()
        driver.quit()


test_check_authorization(driver)

