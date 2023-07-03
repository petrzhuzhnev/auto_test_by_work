import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import AttributeInvest, AttributeConference
from models import Application, CheckData
from moduls import random_data


class Investment(Application):

    # ПОКУПКА ПАКЕТОВ
    def choose_packet(self, packet):
        """нажимает на кнопку 'оформить' для указанного пакета"""
        if packet['id'] in (783, 784, 785):
            element = self.add_id(AttributeInvest.CHOOSE_KIDS_INSTALMENT, packet['id'])
        elif packet['id'] in range(100, 530):
            element = self.add_id(AttributeInvest.CHOOSE_INSTALMENT, packet['id'])
        elif packet['id'] in range(771, 775):
            element = self.add_id(AttributeInvest.CHOOSE_INSTALMENT, packet['id'])
        elif packet['id'] in range(749, 764):
            element = self.add_id(AttributeInvest.CHOOSE_SIMPLE_PACKET, packet['id'])
        else:
            element = self.add_id(AttributeInvest.CHOOSE_PACKET, packet['id'])
        print(element)
        self._wait_click(element)

    def choose_simple_packet(self, investment):
        element = self.add_id(AttributeInvest.CHOOSE_SIMPLE_PACKET, investment['id'])
        self._wait_click(element)

    # возвращает кол-во долей и стоимость пакета
    def get_price_from_front(self):
        price = self._wait_element(AttributeInvest.PACKET_PRICE).text
        price = random_data.extract_nbr(price)
        return int(price)

    def get_shares_from_front(self):
        shares = self._element(AttributeInvest.SHARES_IN_PACKAGE)
        shares = shares.text
        shares = random_data.extract_nbr(shares)
        dbonus_shares = 0
        coupon_shares = 0
        try:
            dbonus_shares = self._element(AttributeInvest.SHARES_FOR_DOUBLE).text
            dbonus_shares = random_data.extract_nbr(dbonus_shares)
            if dbonus_shares == 0:
                dbonus_shares = self._element(AttributeInvest.SHARES_FOR_DOUBLE2).text
                dbonus_shares = random_data.extract_nbr(dbonus_shares)
        except:
            pass
        try:
            coupon_shares = self._element(AttributeInvest.SHARES_FOR_COUPON).text
            coupon_shares = random_data.extract_nbr(coupon_shares)
        except:
            pass
        total_shares = int(shares) + int(dbonus_shares) + int(coupon_shares)
        return int(shares), int(dbonus_shares), int(coupon_shares), int(total_shares)

    def get_overdue_installment_shares(self, order_id, equality):
        coupon_bonus, double_bonus = 0, 0
        if equality == '<':
            coupon_bonus = self.add_id(AttributeInvest.INSTALLMENT_COUPON_BONUS_LOST, order_id)
        else:
            coupon_bonus = self.add_id(AttributeInvest.INSTALLMENT_COUPON_BONUS, order_id)
        double_bonus_ = self.add_id(AttributeInvest.INSTALLMENT_DOUBLE_BONUS, order_id)
        page = 1
        while self.is_element_present(coupon_bonus) is False:    # листает, если не находит на странице элемент
            pages = self.add_id(AttributeInvest.PAGE, page)
            self._click(pages)
            page += 1
        coupon_bonus = self._element(coupon_bonus).text
        coupon_bonus = random_data.extract_nbr(coupon_bonus)
        if self.is_element_present(double_bonus_):
            double_bonus = self._element(double_bonus_).text
            double_bonus = random_data.extract_nbr(double_bonus)
        return int(coupon_bonus), int(double_bonus)

    # возвращает максимальное количество долей из пакета Быстрый старт
    def get_shares_from_investments_screen(self):
        shares_screen = self._element(AttributeInvest.SHARES_IN_PACKAGE_INVESTMENTS_SCREEN)
        shares_screen = shares_screen.text
        shares_screen = random_data.extract_nbr(shares_screen)
        return int(shares_screen)

    def get_shares_from_packet(self, packet):
        try:
            shares = packet['prem']
            return shares
        except:
            shares = 0
            return shares
        return shares

    def issue_premium_shares(self):
        self._click(AttributeInvest.ISSUE_SHARES)


    def click_icon_hide(self):
        if self.is_element_present(AttributeInvest.ICON_HIDEN):
            self._wait_click(AttributeInvest.ICON_HIDEN)

    def coupon_10_percent(self):
        self._wait_implicitly(AttributeInvest.COUPON_ACTIVATED)

    def get_premium_shares_and_in_progress(self):
        self.click_icon_hide()
        try:
            premium_shares = self._wait_element(AttributeInvest.PREMIUM_SHARES)
            premium_shares = premium_shares.text
            premium_shares = random_data.extract_nbr(premium_shares)
            in_process = self._wait_element(AttributeInvest.IN_PROCESS)
            in_process = in_process.text
            in_process = random_data.extract_nbr(in_process)
        except NoSuchElementException:
            premium_shares = 0
            try:
                in_process = self._wait_element(AttributeInvest.IN_PROCESS_WITHOUT_PREMIUM)
                in_process = in_process.text
                in_process = random_data.extract_nbr(in_process)
            except:
                in_process = 0
        return int(premium_shares)+int(in_process)

    def get_discount_from_front(self):
        discount = self._element(AttributeInvest.DISCOUNT)
        discount = discount.text
        return int(discount)

    def get_discount_from_innotrans(self):
        discount = self._element(AttributeInvest.INNOTRANS_DISCOUNT).text
        return int(discount)

    def get_packets_data(self):
        discount = self.get_discount_from_front()
        shares, dbonus_shares, coupon_shares, total_shares = self.get_shares_from_front()
        price = self.get_price_from_front()
        return discount, shares, price

    # разбиваем цену пакета на две части, и вводит в два поля
    def input_sum_for_two(self, input_first, input_second, price):
        self._wait_input(input_first, price // 2)
        self._wait_input(input_second, price - price // 2)

    # разбиваем цену пакета на три части, и вводит в три поля
    def input_sum_for_three(self, input_first, input_second, input_third, price):
        self._wait_input(input_first, price // 3)
        self._wait_input(input_second, price // 3)
        self._wait_input(input_third, price - price // 3 * 2)

    def accounts_for_pay(self, account, price):
        input_a = AttributeInvest.PAY_INPUT_A
        input_b = AttributeInvest.PAY_INPUT_B
        input_c = AttributeInvest.PAY_INPUT_C
        if account == 'main':
            self._wait_input(input_a, price)
            #self._element(AttributeInvest.PAY_INPUT_A).send_keys(Keys.TAB)
        elif account == 'bonus':
            self._wait_input(input_b, price)
            self._element(AttributeInvest.PAY_INPUT_B).send_keys(Keys.TAB)
        elif account == 'share':
            try:
                self._wait_input(input_c, price)
                self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
            except:
                self._wait_input(input_a, price)
                self._element(AttributeInvest.PAY_INPUT_A).send_keys(Keys.TAB)
        elif account == 'main_and_bonus':
            self.input_sum_for_two(input_a, input_b, price)
            self._element(AttributeInvest.PAY_INPUT_B).send_keys(Keys.TAB)
        elif account == 'main_and_share':
            try:
                self.input_sum_for_two(input_a, input_c, price)
                self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
            except:
                self.input_sum_for_two(input_a, input_b, price)
                self._element(AttributeInvest.PAY_INPUT_B).send_keys(Keys.TAB)
        elif account == 'bonus_and_share':
            try:
                self.input_sum_for_two(input_b, input_c, price)
                self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
            except:
                self.input_sum_for_two(input_a, input_b, price)
                self._element(AttributeInvest.PAY_INPUT_B).send_keys(Keys.TAB)
        elif account == 'main_and_bonus_and_share':
            try:
                self.input_sum_for_three(input_a, input_b, input_c, price)
                self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
            except:
                self.input_sum_for_two(input_a, input_b, price)
                self._element(AttributeInvest.PAY_INPUT_B).send_keys(Keys.TAB)
        else:
            print('Error choosing account')

    def accounts_for_pay_conference(self, account, price):
        input_a = AttributeConference.INPUT_A
        input_b = AttributeConference.INPUT_B
        input_c = AttributeInvest.PAY_INPUT_C
        if account == 'main':
            self._wait_input(input_a, price)
            self._element(AttributeConference.INPUT_A).send_keys(Keys.TAB)
        elif account == 'bonus':
            self._wait_input(input_b, price)
            self._element(AttributeConference.INPUT_B).send_keys(Keys.TAB)
        elif account == 'share':
            self._wait_input(input_c, price)
            self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
        elif account == 'main_and_bonus':
            self.input_sum_for_two(input_a, input_b, price)
            self._element(AttributeConference.INPUT_B).send_keys(Keys.TAB)
        elif account == 'main_and_share':
            self.input_sum_for_two(input_a, input_c, price)
            self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
        elif account == 'bonus_and_share':
            self.input_sum_for_two(input_b, input_c, price)
            self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
        elif account == 'main_and_bonus_and_share':
            self.input_sum_for_three(input_a, input_b, input_c, price)
            self._element(AttributeInvest.PAY_INPUT_C).send_keys(Keys.TAB)
        else:
            print('Error choosing account')

    def click_pay(self):
        self._wait_click(AttributeInvest.BTN_PAY_PACKAGE)

    # отмечает чекбокс согласен с условиями дкз, подтверждает инвестицию
    def investment_confirmation(self):
        try:
            self._wait_click(AttributeInvest.CHECKBOX_ICON)
        except:
            self.wd.refresh
            self._wait_click(AttributeInvest.CHECKBOX_ICON)
        finally:
            self._click(AttributeInvest.BTN_FOR_INVESTMENT_CONFIRMATION)

    # подписание требования
    def sign_requirement(self):
        time.sleep(2)
        if self.is_element_present(AttributeInvest.REQUIREMENT_OPEN) is False:
            self.wd.refresh()
            self._wait_element(AttributeInvest.REQUIREMENT_OPEN)
        self._wait_click(AttributeInvest.BTN_SIGN_REQUIREMENT)
        self._wait_element(AttributeInvest.TITLE_CERT)

    # отложить подписание требования
    def postpone_requirement(self):
        self._wait_element(AttributeInvest.REQUIREMENT_OPEN)
        self.remove_element(AttributeInvest.TEST)
        self._click(AttributeInvest.BTN_POSTPONE_REQUIREMENT)
        try:
            self._click(AttributeInvest.MODAL_REGISTER_ALL_REQUIREMENTS)
        except NoSuchElementException:
            return False

    # найти Id сертификата, затем найти отложенное требование и подписать его
    def sign_postpone_requirements(self, db, user_id):
        check = CheckData(db)
        certificate_id = check.postpone_certificate(user_id)
        url_sign = self.wd.find_element(By.CSS_SELECTOR, f'[href="/investment/requirement-sign?id={certificate_id}"]')
        self._click(url_sign)
        self.sign_requirement()

    # Оставляем заявку на голограмму
    def hologram(self):
        try:
            self._click(AttributeInvest.REQUEST_HOLOGRAM)
            return True
        except TimeoutException:
            assert self._element(AttributeInvest.REQUEST_HOLOGRAM_SUCCESS), 'Button did not changed'
        self. _click(AttributeInvest.HOLOGRAM_PACKET_LINK)
        assert self._wait_element(AttributeInvest.REQUEST_HOLOGRAM_SUCCESS), 'Button did not change for Packet page'

    def click_D_reg(self):
        try:
            self._click(AttributeInvest.D)
        except:
            return False
        self._click(AttributeInvest.D_REG)
        self.sign_requirement()

    def check_сert(self, cert_id):
        cert = self.add_id(AttributeInvest.CERT, cert_id)
        self._element(cert)
        cert_status = self.add_id(AttributeInvest.CERT_STATUS, cert_id)
        cert_status = self._element(cert_status).text
        assert cert_status == 'Оформлен' or 'Registered', f'Статус сертификата {cert_status}. Не верный!'

    def check_tizer(self, result):
        if self.is_element_present(AttributeInvest.TIZER) is result:
            return True
        else:
            return False

    def activate_coupon(self):
        self._wait_click(AttributeInvest.COUPON_ACTIVATED)
        activated = self._wait_element(AttributeInvest.COUPON_ACTIVATED)
        activated = activated.text
        assert activated == 'Activated' or 'Активирован', f'Купон {activated}'
        """try:
            self._wait_element(AttributeInvest.TIZERNONE)
            self._click(AttributeInvest.COUPON)
        except:
            return"""
