import pytest
from selenium import webdriver
import helpers
import requests
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import EndpointURLs


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(EndpointURLs.MAIN_PAGE)
    yield driver
    driver.quit()

"""
@pytest.fixture()
def login_user(driver, user_data):
    MainPage(driver).enter_in_account()
    LoginPage(driver).login_user(user_data)
"""

"""
@pytest.fixture()
def user_data():
    user_data = helpers.create_user_data()
    response = requests.post(EndpointURLs.REGISTER_USER, user_data)
    yield user_data
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(EndpointURLs.DELETE_USER, headers=headers)"""

@pytest.fixture
def login_user(driver, registered_user):
    MainPage(driver).enter_in_account()
    LoginPage(driver).login_user(registered_user)

@pytest.fixture
def user_data():
    user_data = helpers.create_user_data()
    yield user_data

@pytest.fixture
def registered_user(user_data):
    response = requests.post(EndpointURLs.REGISTER_USER, json=user_data)
    yield user_data  # Возвращаем user_data для использования в login_user
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(EndpointURLs.DELETE_USER, headers=headers)