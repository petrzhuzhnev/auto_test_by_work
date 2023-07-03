class AttributeCashin:

    # ПОПОЛНЕНИЕ
    INPUT_SUM = ('css', '#cashin-sum')
    CREATE_INVOICE = ('css', 'div.pay-block__cashin button')

    # Данные биллинга
    OPERATION = 'IN'
    STATUS = 4

    # выбор раздела в пополнении
    SECTION = ('css', '[href="#psCategory-%s"]')
    SECTION_CRYPTOCURRENCY = ('css', '[href="#psCategory-1"]')
    SECTION_CARDS = ('css', '[href="#psCategory-2"]')
    SECTION_SWIFT = ('css', '[href="#psCategory-3"]')
    SECTION_AGGREGATORS = ('css', '[href="#psCategory-4"]')
    SECTION_PS = ('css', '[href="#psCategory-5"]')
    # SECTION_CASH = '[href="#psCategory-6"]'
    LIST_SECTION = [SECTION_CRYPTOCURRENCY, SECTION_CARDS, SECTION_SWIFT, SECTION_AGGREGATORS, SECTION_PS]

    # Оплата Visa / MasterCard
    BTN_COOLPAY = ('css', 'button[data-code="mera"]')
    BTN_IMPEX = ('css', 'button[data-code="impex"]')
    BTN_IKAJO = ('css', 'button[data-code="ikajo"]')
    BTN_CAPITALIST = ('css', 'button[data-code="capitalist"]')
    BTN_MERCH = ('css', 'button[data-code="merch"]')

    # Оплата криптовалютой
    BTN_BITCOIN = ('css', 'button[data-code="cryptadiumbtc"]')
    BTN_BITCOIN_CASH = ('css', 'button[data-code="bitcoin-cash"]')
    BTN_DASH = ('css', 'button[data-code="cryptadiumdash"]')
    BTN_DOGECOIN = ('css', 'button[data-code="cryptadiumdoge"]')
    BTN_LITECOIN = ('css', 'button[data-code="сryptadiumltc"]')
    BTN_MONERO = ('css', 'button[data-code="monero"]')
    BTN_ZCASH = ('css', 'button[data-code="zcash"]')
    BTN_USDT = ('css', 'button[data-code="nowpayments"]')
    BTN_BTC = ('css', 'button[data-code="nowpaymentsbtc"]')
    BTN_ETH = ('css', 'button[data-code="nowpaymentseth"]')
    BTN_LTC = ('css', 'button[data-code="nowpaymentsltc"]')
    BTN_ETHEREUM = ('css', 'button[data-code="cryptadiumeth"]')
    BTN_RIPPLE = ('css', 'button[data-code="cryptadiumxrp"]')
    BTN_USDT_OMNI = ('css', 'button[data-code="cryptadiumusdt"]')
    BTN_USDT = ('css', 'button[data-code="cryptadiumusdte"]')
    BTN = ('css', 'button[data-payid="%s"]')


    # Swift - перевод
    BTN_RBKKZSWIFT = ('css', 'button[data-payid="61"]')
    BTN_MIGOMSWIFT = ('css', 'button[data-payid="65"]')
    BTN_MIGOMSEPA = ('css', 'button[data-payid="66"]')

    # Платежные агрегаторы
    BTN_CRYPTONATOR = ('css', 'button[data-code="cryptonator"]')
    BTN_PAPACHANGE = ('css', 'button[data-code="papachange-money"]')

    # Платежные системы
    BTN_PERFECT = ('css', 'button[data-code="perfect-money"]')
    BTN_FASA = ('css', 'button[data-code="fasa"]')

    # Криптовалюты
    URL_BITCOIN = 'https://www.cryptonator.com/'
    URL_BITCOIN_CRYPTADIUM = 'https://dashboard.cryptadium.com/Payment'
    DASH = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_DASH, url=URL_BITCOIN, name='dash')
    ZCASH = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_ZCASH, url=URL_BITCOIN, name='zcash')
    MONERO = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_MONERO, url=URL_BITCOIN, name='monero')
    BITCOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_BITCOIN, url=URL_BITCOIN, name='bitcoin')
    DOGECOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_DOGECOIN, url=URL_BITCOIN, name='dogecoin')
    LITECCOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_LITECOIN, url=URL_BITCOIN, name='liteccoin')
    CRYPTONATOR = dict(section=SECTION_AGGREGATORS, btn=BTN_CRYPTONATOR, url=URL_BITCOIN, name='cryptonator')
    BITCOINCASH = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_BITCOIN_CASH, url=URL_BITCOIN, name='bitcoincash')
    LIST_CRYPTONATOR = [DASH, ZCASH, MONERO, BITCOIN, DOGECOIN, LITECCOIN, CRYPTONATOR, BITCOINCASH]
    CRYPTADIUM_DASH = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_DASH, url=URL_BITCOIN_CRYPTADIUM, name='dash')
    CRYPTADIUM_BITCOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_BITCOIN, url=URL_BITCOIN_CRYPTADIUM, name='bitcoin')
    CRYPTADIUM_DOGECOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_DOGECOIN, url=URL_BITCOIN_CRYPTADIUM, name='dogecoin')
    CRYPTADIUM_LITECCOIN = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_LITECOIN, url=URL_BITCOIN_CRYPTADIUM, name='liteccoin')
    CRYPTADIUM_ETHEREUM = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_ETHEREUM, url=URL_BITCOIN_CRYPTADIUM, name='cryptadiumeth')
    CRYPTADIUM_RIPPLE = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_RIPPLE, url=URL_BITCOIN_CRYPTADIUM, name='cryptadiumxrp')
    CRYPTADIUM_USDT_OMNI = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_USDT_OMNI, url=URL_BITCOIN_CRYPTADIUM, name='cryptadiumusdt')
    CRYPTADIUM_USDT = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_USDT, url=URL_BITCOIN_CRYPTADIUM, name='cryptadiumusdte')
    LIST_CRYPTADIUM = [CRYPTADIUM_DASH, CRYPTADIUM_BITCOIN, CRYPTADIUM_DOGECOIN, CRYPTADIUM_LITECCOIN,
                       CRYPTADIUM_ETHEREUM, CRYPTADIUM_RIPPLE, CRYPTADIUM_USDT_OMNI, CRYPTADIUM_USDT]

    # Nowpayments
    MODAL_NOWPAYMENTS = ('css', '#now-payment-msg')
    USDT = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_USDT, modal=MODAL_NOWPAYMENTS, type='Nowpayments')
    BTC = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_BTC, modal=MODAL_NOWPAYMENTS, type='Nowpaymentsbtc')
    ETH = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_ETH, modal=MODAL_NOWPAYMENTS, type='Nowpaymentseth')
    LTC = dict(section=SECTION_CRYPTOCURRENCY, btn=BTN_LTC, modal=MODAL_NOWPAYMENTS, type='Nowpaymentsltc')
    LIST_NOWPAYMENTS = [USDT, BTC, ETH, LTC]

    # Impex
    URL_IMPEX = 'https://devcab.trading-impex.com'
    IMPEX_AGREE_ELEMENT = ('css', '#impex-alert')
    IMPEX_AGREE_MC = 'span.swc-checkbox__icon'
    BUT_IMPEX__MC = ('css', '#impex-success')
    MASTERCARD = dict(section=SECTION_CARDS, btn=BTN_IMPEX, url=URL_IMPEX, name='mastercard', type='Impex')

    # Ikajo
    URL_IKAJO = 'https://secure.cryptopaymentservices.com/payment/processing'
    IKAJO = dict(section=SECTION_CARDS, btn=BTN_IKAJO, url=URL_IKAJO, name='Ikajo', type='Ikajo')

    # Capitalist
    URL_CAPITALIST = 'https://capitalist.net/merchant/order'
    CAPITALIST = dict(section=SECTION_CARDS, btn=BTN_CAPITALIST, url=URL_CAPITALIST, name='Capitalist',
                      type='Capitalist', id = 63)
    # Perfect money
    URL_PERFECT = 'https://perfectmoney.is/api/step1.asp'
    PERFECTMONEY = dict(section=SECTION_PS, btn=BTN_PERFECT, url=URL_PERFECT, name='perfectmoney',
                        type='PerfectMoney', id = 6)
    # FasaPay
    URL_FASAPAY = 'https://sandbox.fasapay.com/sci/'
    FASAPAY = dict(section=SECTION_PS, btn=BTN_FASA, url=URL_FASAPAY, name='fasapay', type='Fasa', id = 46)

    # AdvCash - papa-change
    URL_ADVCASH = 'https://papa-change.com/merchant_pay'
    ADVCASH = dict(section=SECTION_AGGREGATORS, btn=BTN_PAPACHANGE, url=URL_ADVCASH, name='adv', type='Papachange',
                   id = 67 )

    # Swift
    RBKKZSWIFT = dict(section=SECTION_SWIFT, btn=BTN_RBKKZSWIFT, type='RBKKZSwift', url='swift')
    MIGOMSWIFT = dict(section=SECTION_SWIFT, btn=BTN_MIGOMSWIFT, type='MigomSwift', url='swift')
    MIGOMSEPA = dict(section=SECTION_SWIFT, btn=BTN_MIGOMSEPA, type='MigomSepa', url='swift')
    CONTINUE_SEPA = ('css', '.swc-btn#sepa-link')

    # Заполнение инвойса
    CURRENCY = ('css', 'div[data-val="%s"]')
    LOAD_DATA = ('css', '#fill-from-vd')

    SWIFT_LAST_NAME_EN = ('css', '#swiftagreement-last_name_en')
    SWIFT_FIRST_NAME_EN = ('css', '#swiftagreement-first_name_en')
    SWIFT_CITY_EN = ('css', '#swiftagreement-city_en')
    SWIFT_STREET_EN = ('css', '#swiftagreement-street_en')
    SWIFT_HOUSE = ('css', '#swiftagreement-house')
    # подтверждение создания инвойса
    CHECKBOX_ICON = ('css', '#agree')
    SWC_BTN_NEXT = ('css', '.swc-form-group button.swc-btn')

    COOLPAY_PS = 12
    MERCH = 91
    CRYPTADIUMBTC = 74
    CRYPTADIUMLTC = 75
    CRYPTADIUMETC = 76
    CRYPTADIUMDASH = 77
    CRYPTADIUMDOGE = 78
    CRYPTADIUMXRP = 79
    CRYPTADIUMUSDT = 80
    PERFECT_MONEY = 6
    FASAPAY_PS = 46
    CAPITALIST_PS = 63
    LIST_PS_ALL = [COOLPAY_PS, MERCH, CRYPTADIUMBTC, CRYPTADIUMLTC, CRYPTADIUMETC, CRYPTADIUMDASH, CRYPTADIUMDOGE,
                   CRYPTADIUMXRP, CRYPTADIUMUSDT, PERFECT_MONEY, FASAPAY_PS, CAPITALIST_PS]

    # Параметра ПС в лк
    COMMISSION_PS = ('css', '[data-payid="%s"] .paying__panel-item-text-comission strong')
    SUM_COMMISSION_PS = ('css', '[data-payid="%s"] .paying__panel-item-text-comission')
    FIXED_COMMISSION_PS = ('css', '[data-payid="%s"] .paying__panel-item-text-comission span strong')
    MIN_LIMIT_PS = ('css', '[data-payid="%s"] .paying__panel-item-text :nth-child(4) strong span')
    MAX_LIMIT_PS = ('css', '[data-payid="%s"] .paying__panel-item-text :nth-child(4) strong span:nth-child(2)')

    # merch
    URL_MERCH = 'https://themerch.money/'
    MERCH_PS = dict(section=SECTION_CARDS, btn=BTN_MERCH, url=URL_MERCH, name='Merch', type='Merch', id=MERCH)
    MERCH_SUM_OUT = ('css', '.col-sm-6.col-md-8 .d-flex')

    # мера
    URL_MERA = 'https://lk.cool-pay.com/'
    COOLPAY = dict(section=SECTION_CARDS, btn=BTN_COOLPAY, url=URL_MERA, name='coolpay', type='Mera', id=COOLPAY_PS)
    MASTERCARD_RUS = ('css', '.wrapper [href]')
    MASTERCARD_SUM = ('css', '.whole.unit:nth-of-type(1) .grid.no-stacking-on-mobiles:nth-of-type(2) strong')

    # Проставление чек-боксов
    WARNING_CHECK = ('css', 'input#crypto-checkbox-accept-warning')
    BINANCE_CHECK = ('css', 'input#crypto-checkbox-accept-binance')
    BUTTON_CONFIRM = ('css', 'button#confirm-crypto-warning')
