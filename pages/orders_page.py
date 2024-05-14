import allure
from locators.header_locators import HeaderLocators
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage
from data import EndpointURLs


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Навигация
    @allure.step('Перейти на главную страницу')
    def go_to_main_page(self):
        self.click_on_element(HeaderLocators.CONSTRUCTOR_BTN)
        self.wait_load_url(EndpointURLs.MAIN_PAGE)

    # Управление заказами
    @allure.step('Открыть заказ')
    def open_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_ITEM)

    # Получение информации о заказах
    @allure.step('Получить список заказов')
    def get_history_orders(self):
        self.wait_element(OrdersPageLocators.ALL_ORDERS_LIST)
        orders = [element.text.lstrip('#0') for element in self.get_elements(OrdersPageLocators.ALL_ORDERS_LIST)]
        return orders

    @allure.step('Получить количество заказов за все время')
    def get_all_orders_count(self):
        return self.get_value_from_element(OrdersPageLocators.ALL_ORDERS_COUNT)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_count(self):
        return self.get_value_from_element(OrdersPageLocators.TODAY_ORDERS_COUNT)

    # Проверка состояния заказа
    @allure.step('Проверить, что заказ в работе')
    def check_order_in_work(self, order):
        return self.wait_show_text_in_element(OrdersPageLocators.ORDER_IN_WORK, order)

    # Проверка видимости окна с деталями заказа
    @allure.step('Проверить появление окна с деталями заказа')
    def check_visible_order_window(self):
        return self.check_is_visible_element(OrdersPageLocators.MODAL_WINDOW)
