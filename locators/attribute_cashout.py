class AttributeCashout:

    # ВЫВОД СРЕДСТВ
    # создание нового реквизита
    BTN_CREATE_NEW_DETAIL = ('css', '.swc-btn#add-requisites')
    SELECT_PC = ('css', 'select#account-type')

    BTN_ADD_ACCOUNT = ('css', 'button#send-account-data')
    # 4 - Visa / MasterCard
    # 6 - Qiwi
    # 13 - AdvCash US$
    # 15 - Perfect Money
    # 16 - BitCoin
    # 17 - FasaPay
    # VM
    # модальное окно, данные необходимо обновить
    MODAL_NEED_TO_UPDATE_DATA = ('css', '#vmc-update-info')
    BTN_NEED_UPDATE_OK = ('css', '#vmc-update-info-btn')

    NUMBER_CARD = ('css', 'input#number')
    SURNAME_CARD = ('css', 'input#surname')
    FIRSTNAME_CARD = ('css', 'input#name')
    VALIDITY_CARD = ('css', 'input#expiry')
    CITY_CARD = ('css', 'input#city')
    # Qiwi, AdvCash, Perfect Money, FasaPay
    FIRST_NUMBER_ACCOUNT = ('css', 'input#first_number')  # BitCoin
    SECOND_NUMBER_ACCOUNT = ('css', 'input#userpaymentaccounts-second_number')
    # AdvCash, Perfect Money
    CHECKBOX_ACCOUNT = ('css', '.js-toggle-checkbox')

    INPUT_FOR_CASHOUT = ('css', 'input#summ')
    BTN_MONEY_REQUEST = ('css', '#pay1button')

    CHECKBOX_AGREE = ('css', '.swc-checkbox__label.swc-checkbox-agree')
    CHECKBOX_AGREE_BLOCKCHAIN = ('css', '.swc-checkbox__label.swc-checkbox-agree-blockchain')
    # выбор кошелька на который будет начисление
    ACCOUNTS_ACTIVATE = ('css', '.swc-elements_pay-radio-select.js-pay-active')
    SELECT_ACCOUNT = ('css', 'input[data-type-id="%s"]~.swc-elements_pay-radio-tick')

    INPUT_CODE_CASHOUT = ('css', 'input#cashoutverificationform-sms_code')
    # BTN_VERIFY_CODE = ('css', '#send-sms-code')
    BTN_VERIFY_CODE = ('css', '.swc-modal-footer #send-sms-code')
    BNT_COMPLETE_OPERATION = ('css', '.swc-btn_medium[aria-label="Close"]')
    GO_TO_CANCEL_REQUEST_SCREEN = ('css', '.js-tab-title[data-toggle="cashout-transactions"]')
    CANCEL_REQUEST = ('css', '.js-del-money-request[data-id]')
    CANCEL_REQUEST_YES = ('css', '.swc-modal-footer .js-cashout-request-cancel-btn')
    ALERT = ('css', '.alert__item-text')

    INPUT_PIN_CODE1 = ('css', '.swc-form-pin :nth-child(1).swc-input.swc-input_number.js-input-pin-number')
    INPUT_PIN_CODE2 = ('css', '.swc-form-pin :nth-child(2).swc-input.swc-input_number.js-input-pin-number')
    INPUT_PIN_CODE3 = ('css', '.swc-form-pin :nth-child(3).swc-input.swc-input_number.js-input-pin-number')
    INPUT_PIN_CODE4 = ('css', '.swc-form-pin :nth-child(4).swc-input.swc-input_number.js-input-pin-number')
    SUBMIT_TRANSACTION_PIN = ('css', '#send-sms-code.swc-btn')
    WAIT_MODAL = ('css', 'div#myModal[style="display: none;"]')
    SUBMIT_CONFIRM = ('css', 'button.swc-btn.swc-btn_medium')

    MODAL_DELETE = ('css', '.swc-btn.swc-btn_white.delete_account')
    # Ошибки валидации для btn и usdt
    BTN_ERROR = ('css', '[data-type_id="16"]')
    USDT_ERROR = ('css', '[data-type_id="18"]')
    # Ошибки валидации на форме visa/mastercard
    CARD_NUMBER_ERROR = ('css', '#number + .swc-modal-error.js-modal-error')
    SURNAME_ERROR = ('css', '#surname + .swc-modal-error.js-modal-error')
    FIRST_NAME_ERROR = ('css', '#name + .swc-modal-error.js-modal-error')
    VALIDITY_ERROR = ('css', '#expiry + .swc-modal-error.js-modal-error')
    VALIDITY_OLD_ERROR = ('css', '.swc-modal-error.js-modal-error2')
    CITY_ERROR = ('css', '#city + .swc-modal-error.js-modal-error')
