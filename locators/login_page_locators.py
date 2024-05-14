class LoginPageLocators:
    # Блок авторизации
    LOGIN_FORM = ('xpath', '//h2[text()="Вход"]')  # бланк авторизации
    EMAIL_INPUT = ('xpath', '//label[text()="Email"]/../input')  # поле ввода электронной почты
    PASSWORD_INPUT = ('xpath', '//label[text()="Пароль"]/../input')  # поле ввода пароля

    # Блок кнопок и действий
    SUBMIT_BUTTON = ('xpath', '//form//button')  # кнопка Войти
    RECOVERY_PASSWORD = ('xpath', '//a[text()="Восстановить пароль"]')  # кнопка Восстановить пароль
    SHOW_PASSWORD = ('xpath', '//div[contains(@class, "input__icon-action")]')  # кнопка Показать/скрыть пароль

    # Блок отображения активности поля пароля
    PASSWORD_CONTAIN = ('xpath', '//label[text()="Пароль"]/..')  # отображение активности поля
