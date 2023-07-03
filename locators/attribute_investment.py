class AttributeInvest:


    # Премиальный счет
    D = ('css', '[data-t="premium-acc"] .personal-info__item-name_action')
    D_REG = ('css', '#premium-account-btns button')

    #Серт
    CERT = ('css', '[href="/investment/get-agreement?format=pdf&id=%s"]')
    CERT_STATUS = ('xpath', '//*[@href="/investment/get-agreement?format=pdf&id=%s"]/ancestor::*[2]/td/b')

    #Тизер купона
    TIZER = ('css', '#couponBillet[style="display: block"]')

    #Купон
    COUPON = ('css', '.coupon__item-status .swc-btn')

    # ПОКУПКА
    TITLE_PAGE_INVEST = ('css', '.swc-page-title__between h1')
    # модалки
    # модальное окно для рассрочек
    MODAL_ELEMENT = ('css', '#universal-modal')
    MODAL_ALREADY_OPEN_INSTALLMENT = ('css', '#universal-modal button[data-dismiss="modal"]')
    # подтверждаете инвестицию
    MODAL_FOR_INSTALMENT = ('css', '#progressStart')
    MODAL_FOR_SIMPLE = ('css', 'button.buttonYes')
    # выбрать ребенка
    MENU_SELECT_UNDERAGE = ('css', '#select-underage')
    # стоимость пакета
    PACKET_PRICE = ('css', '#total_price')
    # модальное окно с дисконтом 1:100
    MODAL_DISCOUNT = ('css', '#stepup-modal .swc-modal-dialog .swc-modal-content')
    MODAL_CHOOSENT_DISCOUNT = '#stepup-modal .swc-modal-dialog .swc-modal-content ' \
                              'button.swc-btn.swc-btn_transparent.js-go-to-check'

    # количесвто долей в пакете innotrans
    PACKET_ELEMENT = ('css', '#divStep2')
    SHARES_IN_PACKAGE_INNOTRANS = 'table.innotrans-table.active > tbody > tr:nth-child(3) > td:nth-child(2)'
    # количесвто долей в пакете
    FORM_INFO = ('css', '.chosen-packet__info')
    FORM_PAY = ('css', 'div.chosen-packet__bottom')
    SHARES_IN_PACKAGE = ('css', '[data-type="actions_qnt"]')
    SHARES_FOR_DOUBLE = ('css', '[data-type="siblingBonus"]')
    SHARES_FOR_DOUBLE2 = ('css', '[data-type="simpleBonuses_bonus1"]')
    SHARES_FOR_COUPON = ('css', '[data-type="coupons_qnt"]')
    INSTALLMENT_COUPON_BONUS = ('css', '[data-id="%s"] .executable .my-instalment-bonus__text')
    INSTALLMENT_COUPON_BONUS_LOST = ('css', '[data-id="%s"] .lost .my-instalment-bonus__text')
    INSTALLMENT_DOUBLE_BONUS = ('css', '[data-id="%s"] .taken .my-instalment-bonus__text')
    DISCOUNT = ('css', '.chosen-packet__table-td[data-type="discount"]')
    INNOTRANS_DISCOUNT = ('css', '.chosen-packet__table .innotrans-table.active td:nth-child(2)')
    PREMIUM_SHARES = ('css', '[data-t="premium-acc"] .personal-info__item-val')
    IN_PROCESS = ('css', '.personal-info__items :nth-child(4) [data-show="swcShares"]')
    IN_PROCESS_WITHOUT_PREMIUM = ('css', '.personal-info__items :nth-child(3) [data-show="swcShares"]')
    ICON_HIDEN = ('css', '.personal-info__shares.js-personal-info .personal-info__title_show-icon_hidden')
    ICON_HIDE = ('css', '.personal-info__shares.js-personal-info .personal-info__title_show-icon.js-show-icon')
    COUPON_10_PERCENT = ('css', '.coupon__item-status .swc-btn[onclick]')
    COUPON_ACTIVATED = ('css', '.coupon__billet-block')

    COUPON_DEACTIVATE = ('css', '[onclick="couponDeactivate()"]')

    # Кнопка Продолжить, если не хватает денег для покупки
    NO_MONEY_BUTTON = ('css', '#insufficient-amount .swc-btn.swc-btn_transparent')

    # Кнопка отмены действующего купона
    CANCEL_COUPON = ('css', '[onclick="couponDeactivate()"]')

    #Кнопка подарить
    DONATE_COUPON = ('css', '[onclick="couponModalGift(%s)"]')
    COUPON_IS_NOT_USE = ('xpath', '//*[@id="coupon-id-%s"]/../../following-sibling::*[1]/div/div')
    #COUPON_USED = ('xpath', '//*[@onclick="couponHide(%s)"]/../../div')
    COUPON_USED = ('xpath', './/*[@id="coupon-id-%s"]/../../../../div[3]/div[4]/div/div')
    COUPON_EXPIRED = ('xpath', '//*[@onclick="couponHide(%s)"]/../../div')

    COUPONS_BLOCK = ('xpath', '//*[@id="coupon-id-%s"]/../../../../h3')

    # Активировать
    ACTIVATED_COUPON = ('css', '#coupon-id-%s')

    # Подарок от
    PRESENT_FROM = ('css', '#coupon-id-%s~div b')

    #Плейсхолдер получателя
    DONATE_USER = ('css', '#gift-input')
    DONATE_ERROR = ('css', '.swc-modal-input_error-msg')
    SEND = ('css', '#coupon-modal__gift-ok') # Отправить
    MODAL_TEXT = ('css', '#myModalLabel')
    OK = ('css', 'button[onclick="location.reload()"]') # ОК в модалке

    # поля для ввода суммы для покупки
    MY_CERTIFICATES = ('css', '.swc-table')
    DOUBLE_PAYMENT = ('css', '.chosen-packet__bonus .swc-checkbox-slider__icon')
    PAY_INPUT_A = ('css', 'input#accounta')
    PAY_INPUT_B = ('css', 'input#accountb')
    PAY_INPUT_C = ('css', 'input#accountc')
    BTN_PAY_PACKAGE = ('css', 'input.swc-btn.do-pay-button')
    TO_BOOK = ('css', '[data-type="book_installment"] .swc-btn')
    MODAL_BOOK = ('css', '.swc-btn.js-book-installment.js-book-installment2')
    # подтверждение договора
    BTN_FOR_INVESTMENT_CONFIRMATION = ('css', '.swc-btn.js-toggle-btn')
    REQUIREMENT_OPEN = ('css', '#swc-canvas')
    BTN_SIGN_REQUIREMENT = ('css', 'button#agreement-submit-agree')
    TITLE_CERT = ('css', '.swc-page-title')
    TEST = 'agreement-submit-agree'
    TEST1 = 'button'
    TEST3 = '.swc-elements_btn-box'
    BTN_POSTPONE_REQUIREMENT = ('css', '[name="delay"]')
    REQUIREMENT_DOCUMENT = ('css', '#swc-canvas[height][width]')
    MODAL_REGISTER_ALL_REQUIREMENTS = ('css', '.swc-modal-close.js-chat-rules__no')

    # Заявка на голограмму
    REQUEST_HOLOGRAM = ('css', '.invest-again.invest-again--nagative-mt '
                               '.hologram__button.invest-again__btn.js-invest-again-request-btn')
    REQUEST_HOLOGRAM_SUCCESS = ('css', '.invest-again.invest-again--nagative-mt '
                                       '.hologram__buttoninvest-again__btn.hologram__button_success'
                                       '.js-invest-again-requested-btn')
    HOLOGRAM_PACKET_LINK = ('css', '.hologram__menu-link.js-section-target[data-section-target="packet"]')

    # простые пакеты
    COUPON = ('css', '#coupon-id-%s')
    # выбрать пакет
    PACKAGES = ('css', '#divStep1')
    CHOOSE_SIMPLE_PACKET = ('css', '#investment_programs_button_%s_plus')
    CHOOSE_PACKET = ('css', '[href="/investment/programs?packet=%s"]')
    CHOOSE_INNOTRANCE = ('css', '.package [href="/investment/programs?packet=%s"]')
    CHOOSE_INSTALMENT_WITH_DOUBLE = ('css', '[href="/investment/instalment?packet=%s"]')
    #CHOOSE_INSTALMENT = ('css', '#divStep1 [data-id="%s"] .swc-btn')
    CHOOSE_INSTALMENT = ('css', '[href="/investment/instalment?packet=%s"]')
    # CHOOSE_KIDS_INSTALMENT = ('css', '[href="/investment/instalment?packet=%s"]')
    # CHOOSE_DISABLED_INSTALMENT = ('css', '[data-id="%s"] .swc-btn.disabled')
    SELECT_DOUBLE_ELEMENT = ('css', 'div.packet-line.js_anniversary_inner.packet-line_instal-bonus'
                                    '[data-sibling-id="%s"]')
    SELECT_DOUBLE = 'span.swc-checkbox-slider__icon'
    MONTHS = '[data-type="packetRadio-month"]'
    MONTHS_ON_DETAILS = ('css', '[data-type="month"]')

    # выбор простых пакетов
    PLUS_SIMPLE_PACKET = ('css', '#investment_programs_button_%s_plus')
    PLUS_SIMPLE_PACKET_DISABLED = ('css', '#investment_programs_button_%s_plus.disabled')
    MINUS_SIMPLE_PACKET = ('css', '#investment_programs_button_%s_minus')
    GET_SHARES_ELEMENT = ('css', '#simple-packets-info')
    GET_SHARES_FOR_SIMPLE = 'span[data-type="actions_qnt"]'
    BTN_PAY_PACKAGE_SIMPLE = ('css', '#goToPayStep')
    # ID пакетов
    FIRST_INNOTRANS = dict(id=900, disc=25, price=1000, icon = 'kid', coup=50)
    SECOND_INNOTRANS = dict(id=901, disc=29, price=1000)
    THIRD_INNOTRANS = dict(id=902, disc=39, price=1000)
    PACKET_PREMIUM_25000 = dict(id=896, disc=40, price=25000, icon = 'prem', coup=50, coup1=50, coup2=20)
    PACKET_PREMIUM_50000 = dict(id=897, disc=42, price=50000, icon = 'prem', coup=50, coup1=50, coup2=50)
    PACKET_PREMIUM_100000 = dict(id=898, disc=45, price=100000, icon = 'prem', coup=50, coup1=50, coup2=50)
    PACKET_PREMIUM_150000 = dict(id=899, disc=47, price=150000, icon = 'prem', coup=50, coup1=50, coup2=50)
    PACKET_BONUS_250 = dict(id=903, disc=23, price=250, icon = 'bonus', coup=20)
    PACKET_BONUS_400 = dict(id=904, disc=26, price=400, icon = 'bonus', coup=20)
    PACKET_BONUS_1000 = dict(id=905, disc=31, price=1000, icon = 'bonus', coup=50)
    PACKET_BONUS_1800 = dict(id=906, disc=40, price=1800, icon = 'bonus', coup=50)
    PACKET_STEPUP_600 = dict(id=700, disc=000, price=600)  # степап недействующие пакеты
    PACKET_STEPUP_1200 = dict(id=702, disc=000, price=1200) # степап недействующие пакеты

    PACKET_50 = dict(id=885, disc=14, price=50)
    PACKET_100 = dict(id=886, disc=18, price=100)
    PACKET_200 = dict(id=887, disc=19, price=200, icon = 'simple', coup=20)
    PACKET_350 = dict(id=888, disc=21, price=350, icon = 'simple', coup=20)
    PACKET_500 = dict(id=889, disc=23, price=500, icon = 'simple', coup=20)
    PACKET_1000 = dict(id=890, disc=25, price=1000, icon = 'simple', coup=50)
    PACKET_2000 = dict(id=891, disc=26, price=2000, icon = 'simple', coup=50)
    PACKET_2500 = dict(id=892, disc=27, price=2500, icon = 'simple', coup=50)
    PACKET_3500 = dict(id=893, disc=30, price=3500, icon = 'simple', coup=50)
    PACKET_5000 = dict(id=894, disc=31, price=5000, icon = 'simple', coup=20, coup1=50)
    PACKET_10000 = dict(id=895, disc=37, price=10000, icon = 'simple', coup=20, coup1=50)
    PACKET_25000 = dict(id=896, disc=40, price=25000, icon = 'simple', coup=20, coup1=50, coup2=50)
    PACKET_50000 = dict(id=897, disc=42, price=50000, icon = 'simple', coup=50, coup1=50, coup2=50)
    PACKET_100000 = dict(id=898, disc=45, price=100000, icon = 'simple', coup=50, coup1=50, coup2=50)
    PACKET_150000 = dict(id=899, disc=47, price=150000, icon = 'simple', coup=50, coup1=50, coup2=50)
    SIMPLE_PACKETS = [PACKET_50, PACKET_100, PACKET_200, PACKET_350, PACKET_500, PACKET_1000, PACKET_2000, PACKET_2500,
                      PACKET_3500, PACKET_5000, PACKET_10000, PACKET_25000, PACKET_50000, PACKET_100000, PACKET_150000]
    SIMPLE_PACKETS_WITH_COUPONS = [PACKET_200, PACKET_350, PACKET_500, PACKET_1000, PACKET_2000, PACKET_2500,
                      PACKET_3500, PACKET_5000, PACKET_10000, PACKET_25000, PACKET_50000, PACKET_100000, PACKET_150000]

    # рассрочки
    PACKET_START = dict(id=921, disc=21, price=600, prem=1200, icon = 'kid', coup=20)
    PACKET_KID = dict(id=919, disc=22, price=585, prem=585, icon = 'kid', coup=20)
    PACKET_STUDENT = dict(id=920, disc=24, price=1350, prem=2700, icon = 'kid', coup=50)
    INSTALLMENT_5000 = dict(id=907, disc=29, price=5000,  icon = 'inst', coup=20, coup1=50)
    INSTALLMENT_10000 = dict(id=908, disc=35, price=10000,  icon = 'inst', coup=20, coup1=50)
    INSTALLMENT_25000 = dict(id=909, disc=39, price=25000,  icon = 'inst', coup=20, coup1=50, coup2=50)
    INSTALLMENT_50000 = dict(id=910, disc=40, price=50000,  icon = 'inst', coup=20, coup1=50, coup2=50)

    START_250 = dict(id=911, disc=17, price=250, prem=250, coup=20)
    SENOR_500 = dict(id=912, disc=21, price=500, prem=500, coup=20)
    STABLE_1000 = dict(id=913, disc=23, price=1000, prem=1000, coup=50)
    BUSINESS_2000 = dict(id=914, disc=24, price=2000, prem=2000, coup=50)
    """Рассрочки с двойным платежом"""
    START_250PLUS = dict(id=915, disc=18, price=250, prem=250)
    SENOR_500PLUS = dict(id=916, disc=22, price=500, prem=500)
    STABLE_1000PLUS = dict(id=917, disc=24, price=1000, prem=1000)
    BUSINESS_2000PLUS = dict(id=918, disc=25, price=2000, prem=2000)

    STEPUP_50 = 701
    STEPUP_100 = 703

    """Пакеты Юницкого"""
    UNI_STEP_1_500 = dict(id=870, disc=74, price=500)
    UNI_STEP_1_1000 = dict(id=871, disc=74, price=1000)
    UNI_STEP_1_3000 = dict(id=872, disc=74, price=5000)
    UNI_STEP_1_5000 = dict(id=879, disc=74, price=5000)
    UNI_STEP_1_10000 = dict(id=880, disc=74, price=5000)

    UNI_STEP_2_500 = dict(id=873, disc=74, price=5000)
    UNI_STEP_2_1000 = dict(id=874, disc=77, price=1000)
    UNI_STEP_2_3000 = dict(id=875, disc=77, price=5000)
    UNI_STEP_2_5000 = dict(id=881, disc=77, price=5000)
    UNI_STEP_2_10000 = dict(id=882, disc=77, price=5000)

    UNI_STEP_3_500 = dict(id=876, disc=74, price=5000)
    UNI_STEP_3_1000 = dict(id=877, disc=77, price=1000)
    UNI_STEP_3_3000 = dict(id=878, disc=77, price=5000)
    UNI_STEP_3_5000 = dict(id=883, disc=77, price=5000)
    UNI_STEP_3_10000 = dict(id=884, disc=77, price=5000)



    # оплата рассрочек
    PAY_BTN = ('css', 'button[type="submit"]')
    BTN_TO_SELECT = ('css', 'select.instalment-payment-qty[data-id="%s"]')
    PAGE = ('css', 'a[data-page="%s"]')
    BTN_LAST_DATE = ('css', 'select.instalment-payment-qty[data-id="%s"] :last-child')
    FULL_PAYMENT = ('css', 'select.instalment-payment-qty[data-id="%s"] option')
    BTN_SELECT_ACCOUNT = ('css', '#pay-select%s')
    BTN_TO_PAY = ('css', 'button[data-id="%s"]')
    DOUBLE_PAY = ('css', '.myinstalment_description-link.js-make_double.make_double')
    DOUBLE_CONFIRM = ('css', '.swc-btn.swc-btn_white.buttonYes')
    AUTOPAYMENT_CHECKBOX = ('css', '.options-block-wrap.js-autopayment.js-autopayment_modal '
                                   '.swc-checkbox.js-toggle-label .swc-checkbox__icon')
    AUTOPAYMENT_BUTTON = ('css', '.swc-btn.xs-w100.js-autopayment-submit.js-toggle-btn')
    AUTOPAYMENT_CANCEL = ('css', '.swc-btn-link.js-recurrent-cancel')
    PAY_INSTALMENT = ('css', '.myinstalment__bot .swc-btn.swc-btn_transparent')

    # подписание требования
    CHECKBOX_ICON = ('css', '.swc-checkbox.mb30 span.swc-checkbox__icon')
    WAIT_MY_INSTALMENT = ('css', 'div.swc-page-title.swc-page-title__row')

    # Кол-во простых пакетов
    COUNT_PACKETS = ('css', '[data-id-count="%s"]')

    # Тултипы
    TOOLTIP = ('css', '.tooltipster-base #tooltip_content%s-%s%s')
    KIDS_ICON = ('css', '.package [data-tooltip-content="#tooltip_content%s-%s"]%s')
    DETAILED = ('css', '.tooltipster-base #tooltip_content%s-%s a%s')
    BONUS_ICON = ('css', '.packet-line.js_anniversary_inner [data-tooltip-content="#tooltip_content%s-%s"]%s')
    SIMPLE_ICON = ('css', '[data-tooltip-content="#tooltip_content%s-%s"]%s')
    PREMIUM_ICON = ('css', '.packet-line__scale-top [data-tooltip-content="#tooltip_content%s-%s"]%s')

    # Дисконт 1:600
    DIS600_150000 = dict(id=100, disc=26, price=600, prem=1200)
    DIS600_300000 = dict(id=101, disc=26, price=600, prem=1200)
    DIS600_600000 = dict(id=102, disc=26, price=600, prem=1200)
    DIS600_1500000 = dict(id=103, disc=26, price=600, prem=1200)
    DIS600_3000000 = dict(id=409, disc=26, price=600, prem=1200)
    DIS600_6000000 = dict(id=454, disc=26, price=600, prem=1200)
    DIS600_30000000 = dict(id=455, disc=26, price=600, prem=1200)

    # Дисконт 1:550
    DIS550_137500 = dict(id=521, disc=26, price=600, prem=1200)
    DIS550_275000 = dict(id=159, disc=26, price=600, prem=1200)
    DIS550_550000 = dict(id=160, disc=26, price=600, prem=1200)
    DIS550_1375000 = dict(id=161, disc=26, price=600, prem=1200)
    DIS550_2750000 = dict(id=522, disc=26, price=600, prem=1200)
    DIS550_5500000 = dict(id=460, disc=26, price=600, prem=1200)
    DIS550_27500000 = dict(id=523, disc=26, price=600, prem=1200)

    # Дисконт 1:500
    DIS500_125000 = dict(id=162, disc=26, price=600, prem=1200)
    DIS500_250000 = dict(id=163, disc=26, price=600, prem=1200)
    DIS500_500000 = dict(id=164, disc=26, price=600, prem=1200)
    DIS500_1250000 = dict(id=165, disc=26, price=600, prem=1200)
    DIS500_2500000 = dict(id=519, disc=26, price=600, prem=1200)
    DIS500_5000000 = dict(id=259, disc=26, price=600, prem=1200)
    DIS500_25000000 = dict(id=520, disc=26, price=600, prem=1200)

    # Дисконт 1:450
    DIS450_112500 = dict(id=170, disc=26, price=600, prem=1200)
    DIS450_225000 = dict(id=171, disc=26, price=600, prem=1200)
    DIS450_450000 = dict(id=172, disc=26, price=600, prem=1200)
    DIS450_1125000 = dict(id=173, disc=26, price=600, prem=1200)
    DIS450_2250000 = dict(id=258, disc=26, price=600, prem=1200)
    DIS450_4500000 = dict(id=517, disc=26, price=600, prem=1200)
    DIS450_11250000 = dict(id=518, disc=26, price=600, prem=1200)

    # Дискон 1:400
    DIS400_100000 = dict(id=178, disc=26, price=600, prem=1200)
    DIS400_200000 = dict(id=179, disc=26, price=600, prem=1200)
    DIS400_400000 = dict(id=180, disc=26, price=600, prem=1200)
    DIS400_1000000 = dict(id=181, disc=26, price=600, prem=1200)
    DIS400_2000000 = dict(id=361, disc=26, price=600, prem=1200)
    DIS400_4000000 = dict(id=515, disc=26, price=600, prem=1200)
    DIS400_20000000 = dict(id=516, disc=26, price=600, prem=1200)

    # Дисконт 1:350
    DIS350_87500 = dict(id=186, disc=26, price=600, prem=1200)
    DIS350_175000 = dict(id=187, disc=26, price=600, prem=1200)
    DIS350_350000 = dict(id=188, disc=26, price=600, prem=1200)
    DIS350_875000 = dict(id=189, disc=26, price=600, prem=1200)
    DIS350_1750000 = dict(id=512, disc=26, price=600, prem=1200)
    DIS350_3500000 = dict(id=513, disc=26, price=600, prem=1200)
    DIS350_17500000 = dict(id=514, disc=26, price=600, prem=1200)

    # Дисконт 1:300
    DIS300_75000 = dict(id=194, disc=26, price=600, prem=1200)
    DIS300_150000 = dict(id=195, disc=26, price=600, prem=1200)
    DIS300_300000 = dict(id=196, disc=26, price=600, prem=1200)
    DIS300_750000 = dict(id=197, disc=26, price=600, prem=1200)
    DIS300_1500000 = dict(id=509, disc=26, price=600, prem=1200)
    DIS300_3000000 = dict(id=510, disc=26, price=600, prem=1200)
    DIS300_15000000 = dict(id=511, disc=26, price=600, prem=1200)

    # Дисконт 1:250
    DIS250_62500 = dict(id=202, disc=26, price=600, prem=1200)
    DIS250_125000 = dict(id=203, disc=26, price=600, prem=1200)
    DIS250_250000 = dict(id=204, disc=26, price=600, prem=1200)
    DIS250_625000 = dict(id=205, disc=26, price=600, prem=1200)
    DIS250_1250000 = dict(id=506, disc=26, price=600, prem=1200)
    DIS250_2500000 = dict(id=507, disc=26, price=600, prem=1200)
    DIS250_12500000 = dict(id=508, disc=26, price=600, prem=1200)

    SHARES_IN_PACKAGE_INVESTMENTS_SCREEN = ('css', f'.package [data-id="{PACKET_START["id"]}"] tr:nth-child(1) '
                                                   '.package__item-td.package__item-td_numb')
    SHARES_IN_PACKAGE_PREMIUM_25000 = ('css', f'[data-id="{PACKET_PREMIUM_25000["id"]}"] .packet-line__shares')
    INSTALLMENT_SHARES = ('css', '.executable .my-instalment-bonus__text')
    INSTALLMENT_SHARES2 = ('css', '.lost .my-instalment-bonus__text')

    ISSUE_SHARES = ('css', '#w0 .swc-btn.swc-btn_medium.w100')
