import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driverFixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()