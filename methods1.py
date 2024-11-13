import datetime
import time

import pytest
import requests
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from Telegram import *
from various_data import *
from Business_Actions import *


def find_element(driver, Site_object, * args):
    err = ''

    try:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, Site_object)))
        find_el = driver.find_element(By.XPATH, Site_object)

    except WebDriverException as e:
        err = f"\nОшибка: указан некорректный xPath элемента\nМетод: \nЭлемент: {Site_object}"


def click_element(driver, Site_object, *args):
    err = ''
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, Site_object)))
    try:
        click_el = driver.click()

    except WebDriverException as e:
        err = f"\nОшибка: указан некорректный xPath элемента\nМетод: \nЭлемент: {Site_object}"

class Object:
    def getClass(self):
        pass

    def getEnclosingMethod(self):
        pass

    def getName(self):
        pass


def get_method_name():
    obj = Object()
    m = obj.getClass().getEnclosingMethod()
    return m.getName()







