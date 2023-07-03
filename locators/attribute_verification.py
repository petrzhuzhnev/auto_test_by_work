class AttributeVerification:

    # Раздел Верификация
    MENU = 'li.menu-bar__li'
    MENU_LINK = 'a.menu-bar__sub-menu-link'
    SETTINGS = 'li.menu-bar__li[data-class="user/profile"]'
    # Верификация
    VERIFICATION = ('css', 'li.menu-bar__li[data-class="user/profile"] [href="/personal/list"]')
    FILL_BUTTON = ('css', '.swc-btn[href="/personal/index"]')
    FILL_BUTTON_CHILD = ('css', '.swc-btn[href="/personal/edit-underage"]')
    # Первый шаг заполнения
    LAST_NAME_RU = ('css', '.swc-input.ru_field[name="UserPersonalData[last_name]"]')
    FIRST_NAME_RU = ('css', '.swc-input.ru_field[name="UserPersonalData[first_name]"]')
    LAST_MANE_EN = ('css', '.swc-input.en_field[name="UserPersonalData[last_name_en]"]')
    FIRST_NAME_EN = ('css', '.swc-input.en_field[name="UserPersonalData[first_name_en]"]')
    GENDER = ('css', '.swc-radio.mr25')
    BD_DAY = ('css', '#userpersonaldata-birthday[name="UserPersonalData[birthDay]"]')
    BD_MONTH = ('css', '#userpersonaldata-birthmonth[name="UserPersonalData[birthMonth]"]')
    BD_YEAR = ('css', '#userpersonaldata-birthyear[name="UserPersonalData[birthYear]"]')
    COUNTRY = ('css', '#userpersonaldata-birthplace_country_id.js-userpersonaldata-birthplace_country_id.select2-hidden-accessible')
    BUTTON_1 = ('css', '.swc-btn.swc-btn_w50.btn-next[data-step="personal-data"]')
    # Второй шаг заполнения
    DOCUMENT = ('css', '.js-userpersonaldata-id_type_id.select2-hidden-accessible')
    SERIES_NUMBER = ('css', 'input#userpersonaldata-id_serial_number')
    DD_DAY = ('css', '.js-userpersonaldata-user_document_day.select2-hidden-accessible')
    DD_MONTH = ('css', '.js-userpersonaldata-user_document_month.select2-hidden-accessible')
    DD_YEAR = ('css', '.js-userpersonaldata-user_document_year.select2-hidden-accessible')
    AUTHORITY = ('css', 'input#userpersonaldata-id_who_issue')
    BUTTON_2 = ('css', '.swc-btn.swc-btn_w50.xs-w100.btn-next[data-next="address-data"]')
    # Третий шаг заполнения
    REGISTRATION_COUNTRY = ('css', '.js-userpersonaldata-reg_address_country_id.select2-hidden-accessible')
    REGION = ('css', '.js-userpersonaldata-reg_address_region_id.select2-hidden-accessible')
    SETTLEMENT = ('css', '.js-userpersonaldata-reg_address_city_type_id.select2-hidden-accessible')
    CITY = ('css', 'input#userpersonaldata-reg_address_city_name')
    BUTTON_3 = ('css', '.swc-btn.swc-btn_w50.btn-next[data-next="check-data"]')
    # Четвёртый шаг заполнения
    CONFIRM_CHECKBOX = ('css', '.swc-elements_checkbox-label.swc-elements_checkbox-label_line')
    BUTTON_4 = ('css', '.swc-btn.swc-btn_w50.xs-w100.btn-next[data-next="finish"]')
    # Пятый шаг заполнения
    UPLOAD_FILE = ('css', 'input#userpersonaldatadocuments-file')
    BUTTON_5 = ('css', '.swc-btn.swc-btn_w50')
    CONFIRM_CHECKBOX_2 = ('css', '.swc-checkbox__icon')
    SAVE_BUTTON = ('css', 'button#upload_confirm_file_save')
    MODAL_BUTTON = ('css', '.swc-btn.swc-btn_medium.btn-default')
    # Первый шаг заполнения юр. лица
    LEGAL_FORM_EN = ('css', '#userpersonaldata-legal_form_en')
    COMPANY_NAME_EN = ('css', '#userpersonaldata-company_name_en')
    LEGAL_ADDRESS_EN = ('css', '#userpersonaldata-legal_address_en')
    BUTTON_1_ENTITY = ('css', '.swc-btn.btn-next[data-next="representative-data"]')
    # Второй шаг заполнения юр. лица
    FIRST_NAME_RU_ENTITY = ('css', '.swc-input[name="UserPersonalData[first_name]"]')
    LAST_NAME_RU_ENTITY = ('css', '.swc-input[name="UserPersonalData[last_name]"]')
    LAST_MANE_EN_ENTITY = ('css', '.swc-input[name="UserPersonalData[last_name_en]"]')
    FIRST_NAME_EN_ENTITY = ('css', '.swc-input[name="UserPersonalData[first_name_en]"]')
    POSITION_RU = ('css', '#userpersonaldata-position')
    POSITION_EN = ('css', '#userpersonaldata-position_en')
    BUTTON_2_ENTITY = ('css', '.swc-btn.btn-next[data-next="finish"]')
    # Первый шаг заполнения ребенка
    COUNTRY_CHILD = ('css', '#userpersonaldata-birthplace_country_id.select2-hidden-accessible')
    BUTTON_1_CHILD = ('css', '.swc-btn.swc-btn_w50.xs-w100.btn-next[data-next="passport-data"]')
    # Второй шаг заполнения ребенка
    DOCUMENT_CHILD = ('css', '.swc-select__select.js-id_type-select.select2-hidden-accessible')
    ADDRESS_EN_CHILD = ('css', '.swc-input.en_address_field')
    DD_DAY_CHILD = ('css', '.js-user_document_day-select.select2-hidden-accessible')
    DD_MONTH_CHILD = ('css', '.js-user_document_month-select.select2-hidden-accessible')
    DD_YEAR_CHILD = ('css', '.js-user_document_year-select.select2-hidden-accessible')
    # Статусы
    STATUS_FIFTH = ('css', '.action-block__status.action-block__status_confirmed')
    STATUS_FIRST = ('css', '.action-block__status.action-block__status_need-to-upload')
    STATUS_SECOND = ('css', '.action-block__status.action-block__status_waiting')
    STATUS_THIRD = ('css', '.action-block__status.action-block__status_declined')
    STATUS_SEVENTEEN = ('css', '.color_red')
    LAST_CHILD = ('xpath', './/*[@class="swc-table"]/*/tbody/tr[last()]/td[4]')

