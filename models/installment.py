from selenium.common.exceptions import TimeoutException, NoSuchElementException, JavascriptException

from locators import AttributeInvest
from models import Investment, CheckData, Application

import time


class Installment(Investment, CheckData):

    # ПОКУПКА ПАКЕТОВ
    def choose_packet(self, packet):
        """нажимает на кнопку 'оформить' для указанного пакета"""
        element = self.add_id(AttributeInvest.CHOOSE_INSTALMENT, packet['id'])
        self._wait_click(element)

    def choose_disabled_packet(self, packet):
        """нажимает на кнопку 'оформить со свойством дизайблед' для указанного пакета"""
        # element = self._in_element(AttributeInvest.PACKAGES, AttributeInvest.CHOOSE_DISABLED_INSTALMENT % packet['id'])
        print(packet['id'], AttributeInvest.CHOOSE_DISABLED_INSTALMENT)
        element = self.add_id(AttributeInvest.CHOOSE_DISABLED_INSTALMENT, packet['id'])
        print(element)
        # self._wait_element(element)
        assert self.is_element_present(element), f'Not true {element}'

    # выбрать пакет (для рассрочек с двойным платежом)
    def choose_instalment_double(self, packet):
        element = self.add_id(AttributeInvest.SELECT_DOUBLE_ELEMENT, packet['id'])
        months = self._in_element(element, AttributeInvest.MONTHS).text
        radiobtn = self._in_element(element, AttributeInvest.SELECT_DOUBLE)
        self._click(radiobtn)
        months2 = self._in_element(element, AttributeInvest.MONTHS).text
        assert int(months) - int(months2) == 1, f'{months2} не уменьшилось на 1'
        self.choose_packet(packet)
        monts_d = self._wait_element(AttributeInvest.MONTHS_ON_DETAILS).text
        assert int(months2) == int(monts_d), f'Months {months2} != {monts_d} on detail page'

    # выбор в акционной модалке нашего предложения
    def choose_chosen_instalment(self):
        self._wait_implicitly(AttributeInvest.MODAL_DISCOUNT)
        try:
            self._click(AttributeInvest.MODAL_CHOOSENT_DISCOUNT)
            return True
        except JavascriptException:
            return False

    def coupon_deactivate(self):
        try:
            self.is_element_present(AttributeInvest.COUPON_DEACTIVATE)
            self._click(AttributeInvest.COUPON_DEACTIVATE)
        except:
            return

    # модальное окно уведомляющее о том,
    # что рассрочка уже открыта. нажимает продолжить
    def modal_already_open_installment(self):
        self._wait_implicitly(AttributeInvest.MODAL_ELEMENT)
        try:
            self._click(AttributeInvest.MODAL_ALREADY_OPEN_INSTALLMENT)
            return True
        except NoSuchElementException:
            return False

    # метод для детских пакетов для выбора ребенка
    def select_underage(self):
        self._wait_element(AttributeInvest.MENU_SELECT_UNDERAGE)
        self.menu_select_by_index(AttributeInvest.MENU_SELECT_UNDERAGE, 1)

    # метод для детских пакетов, если нет ребйнка, должен осуществдяться переход к экрану добавления ребёнка
    def select_underage_without_kids(self, base_url, wd):
        self._wait_element(AttributeInvest.MENU_SELECT_UNDERAGE)
        self.menu_select_by_index(AttributeInvest.MENU_SELECT_UNDERAGE, 1)
        url_invoice = f'{base_url}/personal/edit-underage'
        new_url = url_invoice.replace("q:w@", "")
        assert wd.current_url == new_url

    # модальное окно, которое просит подтвердить инвестицию для рассрочек, нажимает да
    def standard_modal_window_for_installment(self):
        self._click(AttributeInvest.MODAL_FOR_INSTALMENT)

    # общий метод для покупки рассрочки
    def purchase_installment_packet(self, account):
        price = self.get_price_from_front()
        shares, dbonus_shares, coupon_shares, total_shares = self.get_shares_from_front()
        self.accounts_for_pay(account, price)
        self.click_pay()
        self.standard_modal_window_for_installment()
        self.investment_confirmation()
        self._wait_element(AttributeInvest.WAIT_MY_INSTALMENT)
        print(f'Price: {price}, shares: {shares}, dbonus_shares: {dbonus_shares}, coupon_shares: {coupon_shares}, '
              f'total_shares: {total_shares}')
        return price, shares, dbonus_shares, coupon_shares, total_shares

    def book_installment_packet(self, packet):
        price = self.get_price_from_front()
        print(packet['id'])
        if packet['id'] in (775, 776, 777, 778):
            self._wait_click(AttributeInvest.DOUBLE_PAYMENT)
        else:
            pass
        self._wait_click(AttributeInvest.TO_BOOK)
        self._wait_click(AttributeInvest.MODAL_BOOK)
        self.investment_confirmation()
        self._element(AttributeInvest.WAIT_MY_INSTALMENT)

    # ОПЛАТА РАССРОЧКИ

    # выбрать кошелек для оплаты
    # A - основной счет - Main account
    # B - бонусный счет - Bonus account
    def select_account_to_pay(self, btn_select_account, account):
        if account == 'main':
            account = 'A'
        else:
            account = 'B'
        self.menu_select(btn_select_account, account)

    def reverse_account(self, account):
        if account == 'main':
            account = 'B'
            return account
        elif account == 'bonus':
            account = 'A'
            return account

    def installment_payment_all_bill(self, order_id, account, value=None):
        select_periods = self.add_id(AttributeInvest.BTN_TO_SELECT, order_id)
        price_for_one = self._element(select_periods)
        price_for_one = price_for_one.get_attribute("data-one-payment")
        periods = self.add_id(AttributeInvest.FULL_PAYMENT, order_id)
        value = len(self._elements(periods))
        re_value = '{}'.format(value)
        price = int(price_for_one) * int(value)
        self.menu_select(select_periods, re_value)
        btn_select_account = self.add_id(AttributeInvest.BTN_SELECT_ACCOUNT, order_id)
        self.select_account_to_pay(btn_select_account, account)
        btn_to_pay = self.add_id(AttributeInvest.BTN_TO_PAY, order_id)
        self._click(btn_to_pay)
        print('Оплата прошла со счета {}'.format(account))
        time.sleep(60)
        return price

    # выбор счета для оплаты по рассрочке, выбирает первый
    def installment_payment(self, order_id, account, payments_left):
        print(order_id)
        btn_to_select = self.add_id(AttributeInvest.BTN_TO_SELECT, order_id)
        btn_select_account = self.add_id(AttributeInvest.BTN_SELECT_ACCOUNT, order_id)
        btn_to_pay = self.add_id(AttributeInvest.BTN_TO_PAY, order_id)
        price = 0
        while payments_left > 0:
            # '1' - селектор для выбора первого счета
            try:
                self._wait_element(btn_to_select)
            except:
                self._click(AttributeInvest.PAGE2)  # можно добавить пролистывание при необходимости
                self._wait_element(btn_to_select)
            self.menu_select(btn_to_select, '1')
            price_for_one = self._element(btn_to_select)
            price_for_one = price_for_one.get_attribute("data-one-payment")
            self.select_account_to_pay(btn_select_account, account)
            self._wait_element(btn_to_select)
            price += int(price_for_one)
            self._click(btn_to_pay)
            payments_left -= 1
            try:
                self.wait_staleness_of(btn_to_pay)
            except:
                self.wd.refresh()
        return price

    def all_installment_payment(self, order_id, account, payments_left):
        btn_to_select = self.add_id(AttributeInvest.BTN_TO_SELECT, order_id)
        btn_select_account = self.add_id(AttributeInvest.BTN_SELECT_ACCOUNT, order_id)
        btn_to_pay = self.add_id(AttributeInvest.BTN_TO_PAY, order_id)
        self.menu_select(btn_to_select, f'{payments_left}')
        self.select_account_to_pay(btn_select_account, account)
        self._click(btn_to_pay)
        time.sleep(15)  # чтоб не упало из-за того что сервер не успел обработать запрос

    # ищем пользователя по ордеру и обновляем ордер по колонке paid
    def search_user_use_order(self, order_id):
        self.search_order()
        self.update_order(order_id)
        self.search_user(order_id)

    def double_pay(self):
        self._click(AttributeInvest.DOUBLE_PAY)
        self._wait_implicitly(AttributeInvest.PAY_INSTALMENT)
        self._click(AttributeInvest.PAY_INSTALMENT)
        self._wait_click(AttributeInvest.DOUBLE_CONFIRM)
        self._wait_implicitly(AttributeInvest.PAY_INSTALMENT)
        self._click(AttributeInvest.PAY_INSTALMENT)

    def autopayment_letters(self):
        self._click(AttributeInvest.AUTOPAYMENT_CHECKBOX)
        self._wait_click(AttributeInvest.AUTOPAYMENT_BUTTON)
        self.wd.back()
        self._wait_click(AttributeInvest.AUTOPAYMENT_CANCEL)

    def cancel_coupon(self):
        try:
            self._wait_implicitly(AttributeInvest.CANCEL_COUPON)
            button = self._element(AttributeInvest.CANCEL_COUPON)
            self._click(button)
            return True
        except NoSuchElementException:
            return False

    def check_tooltips(self, packet):
        locator = None
        if packet['icon'] == 'kid':
            locator = AttributeInvest.KIDS_ICON
        if packet['icon'] == 'bonus':
            locator = AttributeInvest.BONUS_ICON
        if packet['icon'] == 'prem':
            locator = AttributeInvest.PREMIUM_ICON
        if packet['icon'] == 'simple':
            locator = AttributeInvest.SIMPLE_ICON
        icon = self.add_id(locator, packet['id'], packet['coup'])
        print(icon)
        self._click(icon)
        detail = self.add_id(AttributeInvest.DETAILED, packet['id'], packet['coup'])
        self._wait_click(detail)
        window = self.wd.current_window_handle
        windows = self.wd.window_handles
        self.wd.switch_to_window(windows[-1])
        time.sleep(1)
        self.wd.close()
        self.wd.switch_to_window(window)
        if 'coup1' in packet:
            if packet['coup1'] != packet['coup']:
                icon = self.add_id(locator, packet['id'], packet['coup1'], place='')
            else:
                icon = self.add_id(locator, packet['id'], packet['coup1'], place=':nth-of-type(2n)')
            self._click(icon)
            detail = self.add_id(AttributeInvest.DETAILED, packet['id'], packet['coup1'])
            self._click(detail)
            window = self.wd.current_window_handle
            windows = self.wd.window_handles
            self.wd.switch_to_window(windows[-1])
            self.wd.close()
            self.wd.switch_to_window(window)
            if 'coup2' in packet:
                if packet['coup2'] != packet['coup']:
                    icon = self.add_id(locator, packet['id'], packet['coup2'], place='')
                else:
                    icon = self.add_id(locator, packet['id'], packet['coup2'], place=':nth-of-type(2n)')
                print(icon)
                self._click(icon)
                detail = self.add_id(AttributeInvest.DETAILED, packet['id'], packet['coup2'])
                print(detail)
                try:
                    self._click(detail)
                except:
                    self._click(icon) # 2 клика потому-что остается открытой прошлая иконка, что бы закрыть иконку
                    self._click(detail)
                window = self.wd.current_window_handle
                windows = self.wd.window_handles
                self.wd.switch_to_window(windows[-1])
                self.wd.close()
                self.wd.switch_to_window(window)
