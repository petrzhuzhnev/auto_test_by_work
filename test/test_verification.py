import time
import pytest
from locators import AttributeInvest
from models import CheckData, Verification, Registration, User, Session, SingleInvestment, MainMenu

password = '123123'

TEST_CERTIFICATE_STATUS = 5
"""тестовые данные, id пакета и кошелек с которого будет списание"""
INVESTMENT_PREMIUM_25000 = [(AttributeInvest.PACKET_PREMIUM_25000, 'main')]

@pytest.mark.parametrize('investment, account', INVESTMENT_PREMIUM_25000)
def test_verification(wd, open_page, db, base_url, investment, account):
    """Регистрируем нового пользователя
    Проходим все пять шагов верификации, включая заливку сканов
    Сверяем со статусом в БД, чтобы убедиться, что тест пройден верно"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    invest = SingleInvestment(wd)
    user = User(db)
    registr.open_registration_page()
    firstname, phone, email = registr.correct_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    #registr.wait_enter_to_lk(email)
    registr.choose_inviter()
    registr.choose_citizenship()
    user.update_user_accounts(user_id)
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    menu = Verification(wd)
    menu.go_to_first_step()
    menu.first_step()
    menu.second_step()
    menu.third_step()
    menu.fourth_step()
    menu.fifth_step()
    verification_status_id = check.get_verified_status_user(user_id)
    assert [2] == [verification_status_id]
    check.update_id_status_first(user_id)
    menu.check_status_first()
    check.update_id_status_third(user_id)
    menu.check_status_third()
    check.update_id_status_second(user_id)
    menu.check_status_second()
    check.update_id_status_fifteenth(user_id)
    menu.check_status_fifteenth(base_url, wd)
    check.update_id_status_fifth(user_id)
    menu.check_status_fifth()
    mainmenu = MainMenu(wd)
    mainmenu.page_investment()
    balance = check.balance(user_id)
    invest.click_icon_hide()
    invest.coupon_10_percent()
    premium_shares_before = invest.get_premium_shares_and_in_progress()
    invest.choose_packet(investment)
    shares, dbonus_shares, coupon_shares, total_shares = invest.get_shares_from_front()
    invest.choose_chosen_instalment()
    price = invest.get_price_from_front()
    balance -= price
    invest.purchase_packet(account, price)
    time.sleep(0.5)
    cert = check.get_certificate(user_id)
    premium_shares_after = invest.get_premium_shares_and_in_progress()
    assert premium_shares_after == (
                premium_shares_before + total_shares)  # если тест падает с такой ошибкой 0 != 1800, то проверить отображение блока с премиумными долями
    assert cert[1] == 5
    print('\nTest completed: Purchase PREMIUM 25000 packet %s from accounts %s' % (investment, account))
    print('\nTest completed: User %s (%s) verified' % (user_id, email_db))


def test_verification_entity(wd, open_page, db, base_url):
    """Регистрируем нового пользователя
    Проходим три шага верификации, включая заливку сканов
    Сверяем со статусом в БД, чтобы убедиться, что тест пройден верно"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    name, phone, email = registr.first_form_entity()
    registr.sign_up_entity()
    registr.wait_confirm_first_form()
    time.sleep(1)
    name_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [name, phone, email] == [name_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.second_form_entity()
    registr.confirm_registration_entity()
    registr.wait_enter_to_lk(email)
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    registr.choose_inviter()
    registr.choose_citizenship()
    menu = Verification(wd)
    menu.go_to_first_step()
    menu.first_step_entity()
    menu.second_step_entity()
    menu.third_step_entity()
    verification_status_id = check.get_verified_status_user(user_id)
    assert [2] == [verification_status_id]
    check.update_id_status_fifth(user_id)
    menu.check_status_fifth()
    check.update_id_status_first(user_id)
    menu.check_status_first()
    check.update_id_status_third(user_id)
    menu.check_status_third()
    print('\nTest completed: User %s (%s) verified' % (user_id, email_db))


def test_verification_child(wd, open_page, db, base_url):
    """Находим пользователя, который может завести ребенка
    Проходим все четыре шага верификации, включая заливку сканов
    Сверяем со статусом в БД, чтобы убедиться, что тест пройден верно"""
    menu = Verification(wd)
    check = CheckData(db)
    session = Session(base_url, wd)
    user = User(db)
    user_id = check.get_user_for_verification_child()
    user.update_user(user_id)
    username = user.chosen_data_user(user_id)
    print(user_id, username)
    session.login(username, password)
    menu.go_to_first_step_child()
    menu.first_step_child()
    menu.second_step_child()
    menu.third_step_child()
    menu.fourth_step_child()
    time.sleep(5)
    verification_status_id, child_first_name = check.get_verified_status_child(user_id)
    print(child_first_name)
    assert [2] == [verification_status_id]
    check.update_id_status_seventeen(user_id)
    menu.check_status_seventeen()
    check.update_id_status_sixteenth(user_id)
    menu.check_status_sixteenth(child_first_name)
    print('\nTest completed: User %s verified' % user_id)
