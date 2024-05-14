class RecoveryPageLocators:
    # Блок формы восстановления пароля
    RECOVERY_FORM = ('xpath', '//h2[text()="Восстановление пароля"]')  # форма восстановления пароля
    EMAIL_INPUT = ('xpath', '//label[text()="Email"]/../input')  # поле ввода электронной почты

    # Блок кнопки и сообщения
    SUBMIT_BUTTON = ('xpath', '//form//button')  # кнопка Восстановить
    INFO_ABOUT_RECOVERY = ('xpath', '//label[text()="Введите код из письма"]')  # сообщение о восстановлении
