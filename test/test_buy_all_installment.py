import pytest

from models import Installment, CheckData, MainMenu, User, Session

ACCOUNTS = ['main', 'bonus']
TEST_CERTIFICATE_STATUS = 5
password = '123123'


@pytest.mark.parametrize('account', ACCOUNTS)
def test_buy_all_installment(db, wd, account, base_url):
    """
    Перейти на страницу Мои рассрочки
    Найти ордер рассрочки.
    Оплатить рассрочку. Оплата проходит по каждому счетку отдельно
    Сверить баланс до и после
    Подписать требование
    Проверка, после выплаты есть переход на страницу Мои сертификаты
    Сверить ожидаемые данные в сертификате с полученными из базы данных
    тестовые данные, кошелек для списания оплаты за платеж по рассрочке
    """
    menu = MainMenu(wd)
    invest = Installment(wd)
    check = CheckData(db)
    user = User(db)
    session = Session(base_url, wd)
    user_id = check.search_user_id_array()
    user.update_user(user_id)
    username = user.chosen_data_user(user_id)
    session.login(username, password)
    menu.page_my_instalment()
    balance_before = check.balance(user_id)
    order_id, packet_id, payments_left = check.get_order_instalment(user_id)
    price = invest.installment_payment(order_id, account, payments_left)
    balance = balance_before - price
    invest.sign_requirement()
    balance_after = check.balance(user_id)
    assert balance_after == balance
    cert = check.get_certificate(user_id)
    assert cert[1] == TEST_CERTIFICATE_STATUS
    print('\nTest completed: Payment installment %s from accounts %s ' % (packet_id, account))


account = ['main', 'bonus']


@pytest.mark.parametrize('account', account)
def test_pay(db, wd, account, base_url):
    """
    Проверить оплату со счета А и Б
    """
    menu = MainMenu(wd)
    invest = Installment(wd)
    check = CheckData(db)
    user = User(db)
    session = Session(base_url, wd)
    user_id, username = user.with_open_instalment()
    session.login(username, password)
    menu.page_my_instalment()
    balance_before = check.account_balance(user_id, account)
    order_id, packet_id, payments_left = check.get_order_instalment(user_id)
    price = invest.installment_payment_all_bill(order_id, account)
    invest.sign_requirement()
    print(balance_before, price)
    balance_after = check.account_balance(user_id, account)
    balance = int(balance_before) - int(price)
    assert balance_after == balance
    cert = check.get_certificate(user_id)
    assert cert[1] == TEST_CERTIFICATE_STATUS
    print('\nTest completed: Payment installment %s from accounts %s ' % (packet_id, account))


@pytest.mark.parametrize('account', account)
def test_pay_if_null(db, wd, account, base_url):
    """
    Списание со счета Б, если деньги на счете А и наоборот
    """
    menu = MainMenu(wd)
    invest = Installment(wd)
    check = CheckData(db)
    user = User(db)
    session = Session(base_url, wd)
    user_id, username = user.with_open_instalment()
    session.login(username, password)
    menu.page_my_instalment()
    user.update_for_only_one_account(user_id, account)
    balance_before = check.account_balance(user_id, account)
    order_id, packet_id, payments_left = check.get_order_instalment(user_id)
    revers_account = invest.reverse_account(account)  # инвертируем аккаунт для оплаты с другого счета и обратно
    price = invest.installment_payment_all_bill(order_id, revers_account)
    invest.sign_requirement()
    balance = balance_before - price
    balance_after = check.account_balance(user_id, account)
    assert balance_after == balance
    cert = check.get_certificate(user_id)
    assert cert[1] == TEST_CERTIFICATE_STATUS
    print('\nTest completed: Payment installment %s from accounts %s ' % (packet_id, account))
