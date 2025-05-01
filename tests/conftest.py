import pytest
from selene import browser

from selenium import webdriver

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # Задаем базовый урл
    browser.config.base_url = 'https://demoqa.com'
    # Задаем размер окна браузера
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    driver_options = webdriver.ChromeOptions()
    # Selenium WebDriver будет ожидать, пока не будет возвращен запуск события DOMContentLoaded
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
