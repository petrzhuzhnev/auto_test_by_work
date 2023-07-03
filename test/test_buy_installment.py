import pytest
import time

from locators import AttributeInvest
from models import CheckData, Installment, MainMenu, User, Session

TEST_URL = 'myinstalment-not-paid'
TEST_ORDER_STATUS = 1
TEST_ORDER_STATUS2 = 3
TEST_CERTIFICATE_STATUS = 5
password = '123123'

SET_INSTALLMENT = [(AttributeInvest.INSTALLMENT_5000, 'bonus'),
                   (AttributeInvest.INSTALLMENT_10000, 'main_and_bonus'),
                   (AttributeInvest.INSTALLMENT_25000, 'main'),
                   (AttributeInvest.INSTALLMENT_50000, 'bonus'),
                   (AttributeInvest.START_250, 'main_and_bonus'),
                   (AttributeInvest.SENOR_500, 'main'),
                   (AttributeInvest.STABLE_1000, 'bonus'),
                   (AttributeInvest.BUSINESS_2000, 'main_and_bonus')]

@pytest.mark.parametrize('packet, account', SET_INSTALLMENT)
def test_buy_installment(db, wd, base_url, packet, account):
    """
    Проверить отображение требования для подписания, если есть, подписать
    Открыть страницу инвестировать
    Сохранить баланс до покупки
    Выбрать пакет
    Оформить пакет, сохранить стоимость и доли
    Проверка, после оформления есть переход на страницу Мои рассрочки
    Вычесть из баланса до стоимость пакета
    Сравнить ожидаемый баланс и баланс после покупки
    Найти ордер рассрочки. Сравнить ожидаемые данные с полученными из базы данных
    тестовые данные, id пакета и кошелек с которого будет списание
    """
    menu = MainMenu(wd)
    invest = Installment(wd)
    check = CheckData(db)
    user = User(db)
    session = Session(base_url, wd)
    user_id, username = user.with_open_instalment()
    session.login(username, password)
    menu.page_investment()
    balance = check.balance(user_id)
    print(balance, user_id)
    invest.choose_packet(packet)
    #invest.choose_chosen_instalment()
    discount = invest.get_discount_from_front()
    assert discount == packet['disc'], "Дисконты не равны"
    invest.modal_already_open_installment()
    price, shares, dbonus_shares, coupon_shares, total_shares = invest.purchase_installment_packet(account)
    balance -= price
    balance_after = check.balance(user_id)
    assert balance_after == balance
    order_shares, status, order = check.get_order(user_id)
    assert [order_shares, status] == [shares, TEST_ORDER_STATUS]
    print('\nTest completed: Registration installments %s from accounts %s ' % (packet, account))
