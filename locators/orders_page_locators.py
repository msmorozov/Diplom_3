class OrdersPageLocators:
    # Блок заказов
    ORDER_ITEM = ('xpath', '//li[contains(@class, "OrderHistory_listItem")]')  # заказ
    ALL_ORDERS_LIST = ('xpath', '//p[contains(text(), "#")]')  # лента выполненных заказов
    ORDER_IN_WORK = ('xpath', '//ul[contains(@class, "orderListReady")]/li')  # заказ в работе

    # Блок счетчиков заказов
    ALL_ORDERS_COUNT = ('xpath', '//p[text()="Выполнено за все время:"]/following-sibling::'
                                 'p[contains(@class,"OrderFeed_number")]')  # счетчик всех заказов
    TODAY_ORDERS_COUNT = ('xpath',
                          '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "OrderFeed_number")]')  # счетчик заказов за сегодня

    # Блок модального окна
    MODAL_WINDOW = ('xpath', '//section[contains(@class, "modal_opened")]')  # модальное окно
