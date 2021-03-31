from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
    # Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)  # Влад впиши потом нужный сайт.

# Теперь нажмем на кнопку "Найти"
@then("click on href with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.LINK_TEXT, text))
    )
    context.browser.find_element_by_link_text(text).click()

@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='{}']".format(text)))
    ).click()
    #context.browser.find_element_by_xpath("//button[text()='{}']".format(text)).click()

# Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
    context.browser.quit()