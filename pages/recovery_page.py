import allure
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Проверка видимости формы
    @allure.step('Проверка видимость формы восстановления пароля')
    def check_visible_recovery_form(self):
        return self.check_is_visible_element(RecoveryPageLocators.RECOVERY_FORM)

    # Заполнение формы
    @allure.step('Заполнение формы восстановления пароля')
    def filling_recovery_form(self, user_data):
        self.enter_text_in_element(RecoveryPageLocators.EMAIL_INPUT, user_data['email'])
        self.click_on_element(RecoveryPageLocators.SUBMIT_BUTTON)

    # Проверка запроса кода подтверждения
    @allure.step('Проверка видимости запроса ввода кода подтверждения')
    def check_visible_recovery_code(self):
        return self.check_is_visible_element(RecoveryPageLocators.INFO_ABOUT_RECOVERY)