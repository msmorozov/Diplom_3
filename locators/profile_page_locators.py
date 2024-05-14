class ProfilePageLocators:
    # Блок информации о профиле пользователя
    PROFILE_INFO = ('xpath', '//div[contains(@class, "Profile")]')  # информация о профиле пользователя
    ORDER_HISTORY_BTN = ('xpath', '//a[text()="История заказов"]')  # кнопка перехода в историю заказов

    # Блок управления профилем
    EXIT_BTN = ('xpath', '//button[text()="Выход"]')  # кнопка Выйти из профиля

    # Блок истории заказов
    ORDERS_HISTORY_LIST = ('xpath', '//p[contains(text(), "#")]')  # история заказов пользователя
