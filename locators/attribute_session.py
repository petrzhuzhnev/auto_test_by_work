class AttributeSession:

    # Авторизация в лк
    CLOSE_MODAL = ('css', '.swc-modal-close')
    # FRAME_LOG = ('formLogin')
    NAME = ('css', '.personal-info__name')
    LOGIN_FORM_EMAIL = ('css', 'input.login__form-email')
    LOGIN_FORM_PASSWORD = ('css', 'input.login__form-control')
    LOGIN_FORM_SUBMIT = ('css', '.swc-btn.mb30#buttonLoginSubmit')
    # кнопка выхода из лк
    KEY_EXIT = ('css', 'a.header__logout')
    # ошибки при входе
    EMAIL_ERROR = ('css', '[for="email"].error')
    PASSWORD_ERROR = ('css', '[for="password"].error')
    # GA
    FIELD_FOR_GA = ('css', '.swc-input#code-input')
    BUTTON_GA = ('css', '.login__form-submit.swc-btn')
    BAN_GA = ('css', '.login__form-title')

    # ID на странице регистрации
    DISPLAYING_ID = ('css', '#signupform-partner_email')
