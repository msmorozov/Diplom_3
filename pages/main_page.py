import allure
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from data import EndpointURLs


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Ингредиенты
    @allure.step("Получить количество добавлений ингредиента")
    def get_ingredient_count(self):
        return self.get_value_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Кликнуть на ингредиент")
    def view_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step("Закрыть окно с деталями об ингредиенте")
    def close_ingredient_detail_windows(self):
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW)

    @allure.step('Окно деталей ингредиента не отображается')
    def check_display_ingredient_details_popup(self):
        return self.check_is_visible_element(MainPageLocators.MODAL_WINDOW)

    @allure.step("Проверить открытие окна с деталями ингредиента")
    def check_visible_ingredient_detail_windows(self):
        return self.check_is_visible_element(MainPageLocators.MODAL_WINDOW)

    # Навигация
    @allure.step('Перейти на страницу Лента заказов')
    def go_to_orders_feed_page(self):
        self.click_on_element(HeaderLocators.ORDERS_FEED_BTN)
        self.wait_load_url(EndpointURLs.FEED)

    @allure.step('Перейти на страницу Личный кабинет')
    def go_to_profile(self):
        self.click_on_element(MainPageLocators.PROFILE_BTN)
        self.wait_load_url(EndpointURLs.PROFILE_PAGE)

    @allure.step('Перейти на страницу авторизации')
    def go_to_login(self):
        self.click_on_element(MainPageLocators.PROFILE_BTN)
        self.wait_load_url(EndpointURLs.LOGIN_PAGE)

    # Заказы
    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_in_basket(self):
        element = self.get_element(MainPageLocators.INGREDIENT)
        target = self.get_element(MainPageLocators.BASKET_AREA)
        self.drag_and_drop(element, target)

    @allure.step('Создать заказ')
    def create_order(self):
        self.add_ingredient_in_basket()
        self.click_on_element(MainPageLocators.CREATE_ORDER)
        self.wait_hide_text_in_element(MainPageLocators.ORDER_NUMBER, "9999")
        order = self.get_value_from_element(MainPageLocators.ORDER_NUMBER)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW)
        return order

    # Авторизация
    @allure.step('Нажать кнопку Войти в аккаунт')
    def enter_in_account(self):
        self.click_on_element(MainPageLocators.ENTER_IN_ACCOUNT)
