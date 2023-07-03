from models import CheckData
from models import Registration, Session, User

import time


def test_registration_choose_real_inviter(db, wd, open_page, base_url): #дописать проверку БД трех ниже тестов
    """Проверка формы регистрации физ лица
    на сайте с указанием в ЛК пригласителя и заполнением формы."""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    registr.check_change_entity()
    firstname, phone, email = registr.correct_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    time.sleep(1)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    registr.wait_enter_to_lk(email)
    inviter, inviter_id = check.get_inviter()
    registr.choose_real_inviter(inviter)
    registr.choose_citizenship()
    #inviter_id_bd = check.search_partner(user_id)    # не делаем эту проверку так как сразу не обновляется
    # структура на сервере
    #assert inviter_id == inviter_id_bd, f'Not that inviter from {user_id}'
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    print('\nTest completed: Physical entity (%s) was registered with inviter_id = %s' % (user_id, inviter_id))


def test_registration_choose_inviter_later(db, wd, open_page, base_url):
    """Проверка формы регистрации физ лица
    на сайте с указанием в ЛК пригласителя="Указать позже" и заполнением формы."""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    # partner = registr.get_partner()
    current_email, current_phone = check.get_email_phone_for_reg()
    firstname, phone, email = registr.correct_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    time.sleep(1)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    registr.wait_enter_to_lk(email)
    registr.choose_inviter_later()
    registr.choose_citizenship()
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    inviter_id_bd = check.search_partner(user_id)
    assert inviter_id_bd == 1
    print('\nTest completed: Physical entity (%s) was registered' % user_id)


def test_registration_choose_without_inviter(db, wd, open_page, base_url):
    """Проверка формы регистрации физ лица
    на сайте с указанием в ЛК "Без пригласителя" и заполнением формы."""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    firstname, phone, email = registr.correct_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    time.sleep(1)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    registr.wait_enter_to_lk(email)
    registr.choose_without_inviter()
    registr.choose_citizenship()
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    inviter_id_bd = check.search_partner(user_id)
    assert inviter_id_bd == 1
    print('\nTest completed: Physical entity (%s) was registered' % user_id)


def test_registration(db, wd, open_page, base_url):
    """Проверка формы регистрации физ лица
    на сайте"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    # partner = registr.get_partner()
    current_email, current_phone = check.get_email_phone_for_reg()
    registr.fill_first_form_incorrect(current_email, current_phone)
    registr.open_login_page()
    registr.open_registration_page()
    firstname, phone, email = registr.fill_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    time.sleep(1)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    registr.wait_enter_to_lk(email)
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    print('\nTest completed: Physical entity (%s) was registered' % user_id)


def test_registration_entity(db, wd, open_page, base_url):
    """Проверка формы регистрации юр лица
        на сайте, негативные и положительные тесты"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    registr.open_registration_page()
    name, phone, email = registr.first_form_entity()
    registr.sign_up_entity()
    registr.wait_confirm_first_form()
    name_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [name, phone, email] == [name_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.second_form_entity()
    registr.confirm_registration_entity()
    registr.wait_enter_to_lk(email)
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    print('\nTest completed: Legal entity (%s) was registered' % user_id)


def test_registration_with_inviter(db, wd, open_page, base_url):
    """Проверка формы регистрации физ лица
    на сайте по реферальной ссылке"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    user = User(db)
    user_id_inviter = user.user_confirmed()[0]
    registr.open_registration_page_with_inviter(base_url, user_id_inviter)
    firstname, phone, email = registr.fill_form()
    registr.sign_up()
    registr.wait_enter_to_lk(email)
    time.sleep(1)
    firstname_db, phone_db, email_db, user_id, verified_code = check.get_new_user_data()
    assert [firstname, phone, email] == [firstname_db, phone_db, email_db]
    registr.to_second_form(base_url, user_id, verified_code)
    registr.fill_second_form()
    registr.confirm_registr()
    registr.wait_enter_to_lk(email)
    verified_register, verified_email = check.get_verified_register_new_user(user_id)
    assert [1, 1] == [verified_register, verified_email]
    inviter_id = check.search_partner(user_id)
    assert user_id_inviter == inviter_id
    print('\nTest completed: Physical entity (%s) with inviter (%s) was registered' % (user_id, inviter_id))


def test_registration_entity_with_inviter(db, wd, open_page, base_url):
    """Проверка формы регистрации юр лица
        на сайте, негативные и положительные тесты"""
    check = CheckData(db)
    registr = Registration(wd)
    session = Session(base_url, wd)
    user = User(db)
    user_id_inviter = user.user_confirmed()[0]
    registr.open_registration_page_with_inviter(base_url, user_id_inviter)
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
    inviter_id = check.search_partner(user_id)
    assert user_id_inviter == inviter_id
    print('\nTest completed: Legal entity (%s) with inviter (%s) was registered' % (user_id, inviter_id))

def test_registration_with_null_form(db, wd, open_page, base_url):
    """Проверка формы регистрации физ лица
    на сайте с указанием в ЛК пригласителя и заполнением формы."""
    check = CheckData(db)
    registr = Registration(wd)
    registr.open_registration_page()
    registr.delete_disabled_and_submit_for_fl()
    registr.delete_disabled_and_submit_for_yl()
    print('\nTest completed: Ok')
