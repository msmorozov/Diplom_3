import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from data import EndpointURLs


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Видимость пароля
    @allure.step('Кликнуть на видимость пароля')
    def hide_or_show_password(self):
        self.click_on_element(LoginPageLocators.SHOW_PASSWORD)

    # Авторизация
    @allure.step('Авторизация')
    def login_user(self, user_data):
        self.wait_load_url(EndpointURLs.LOGIN_PAGE)
        self.enter_text_in_element(LoginPageLocators.EMAIL_INPUT, user_data['email'])
        self.enter_text_in_element(LoginPageLocators.PASSWORD_INPUT, user_data['password'])
        self.click_on_element(LoginPageLocators.SUBMIT_BUTTON)
        self.wait_load_url(EndpointURLs.MAIN_PAGE)

    # Навигация
    @allure.step('Перейти на страницу Восстановление пароля')
    def go_to_recovery_password(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD)

    # Проверка элементов
    @allure.step('Проверить активность поля')
    def check_active_password_field(self):
        if 'status_active' in self.get_attribute_from_element(LoginPageLocators.PASSWORD_CONTAIN, 'class'):
            return True
        else:
            return False

    @allure.step('Проверить видимость формы авторизации')
    def check_visible_login_form(self):
        return self.check_is_visible_element(LoginPageLocators.LOGIN_FORM)
