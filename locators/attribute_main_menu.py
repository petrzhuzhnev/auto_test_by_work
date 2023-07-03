class AttributeMainMenu:

    # Мои инвестиции раздел
    # Мои инвестиции
    MENU = 'li.menu-bar__li'
    MENU_LINK = 'a.menu-bar__sub-menu-link'
    MY_INVESTMENT = ('css', MENU + '[data-class="investment/portfolio"] span')
    # Инвестировать
    MY_CERTIFICATES = ('css', MENU_LINK + '[href="/investment/portfolio"]')
    MY_COUPONS = ('css', MENU_LINK + '[href="/investment/coupons"]')
    INVESTMENT_PAGE = ('css', MENU_LINK + '[href="/investment/programs"]')
    PAGE_INVESTMENT_URL = ('css', '/investment/programs')
    DISCOUNT_PAGE = ('css', '.swc-btn.swc-btn_transparent-white.desktop')
    # Мои рассрочки
    INVESTMENT = ('css', 'li.menu-bar__li[data-class="investment/portfolio"]')
    MY_INSTALMENT = ('css', MENU_LINK + '[href="/investment/myinstalment-not-paid"]')
    # Голограммы
    HOLOGRAM = ('css', MENU_LINK + '[href="/investment/hologram"]')

    # Банкинг
    MENU_BANKING = ('css', MENU + '[data-class="account/index"] span')
    # Транзакции
    BANKING_TRANSACTIONS = ('css', MENU_LINK + '[href="/account/index"]')
    # Пополнение
    BANKING_CASHING = ('css', MENU_LINK + '[href="/account/cashin"]')
    # Swift-инвойс
    BANKING_SWIFT = ('css', MENU_LINK + '[href="/swift"]')
    # Перевод средств
    BANKING_TRANSFER = ('css', MENU_LINK + '[href="/account/money-transfer"]')
    BANKING_CASHOUT = ('css', MENU_LINK + '[href="/account/cashout"]')
    # Страница создания реквизитов
    BANKING_DETAILS = ('css', MENU_LINK + '[href="/account/settings"]')

    # Настройки
    PROFILE = ('css', 'li.menu-bar__li[data-class="user/profile"]')
    SECURITY = ('css', '[href="/user/security"]')
    # Инструменты пользователя
    TOOLS = ('css', MENU_LINK + '[href="/tools/ref-link"]')
    # План вознаграждений
    REWARDS_PLAN = ('css', MENU_LINK + '[href="/tools/marketing-plan"]')
    # Магазин
    SHOP = ('css', MENU_LINK + '[href="/shop"]')
    # Статистика
    STATISTICS = ('css', MENU_LINK + '[href="/stat/statistics"]')
