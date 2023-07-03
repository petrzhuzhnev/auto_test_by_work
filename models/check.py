import random

from moduls import random_data
import time
from decimal import Decimal

class CheckData:

    def __init__(self, db):
        self.db = db

    def delete_hidden_name(self, user_id):
        request = "DELETE from user_properties where user_id = %s and name = 'hidden_name'; " % user_id
        self.db.select_data_from_db(request)
        time.sleep(1)
        request = "SELECT *from user_properties where user_id = %s and name = 'hidden_name'; " % user_id
        check_hidden_name = self.db.select_data_from_db(request)
        assert check_hidden_name is None, print('Удаление отображения ID не сработало')
        return

    def get_inviter(self):
        request = "SELECT email m, id from user " \
                      "where verified_notification = 1 order by id desc limit 1; "
        inviter, inviter_id = self.db.select_data_from_db(request)
        return inviter, inviter_id

    def get_overdraft_agreement(self, user_id):
        time.sleep(1)
        request = "SELECT value from user_properties " \
                  "WHERE  user_id = %s and name = 'overdraft_agreement_signed'; " % user_id
        _value = self.db.select_data_from_db(request)
        return _value[0]

    def delete_agreement(self, user_id):
        request = "DELETE FROM user_properties " \
                  "where user_id = %s and name = 'overdraft_agreement_signed'; " % user_id
        self.db.select_data_from_db(request)
        request = 'INSERT INTO user_alert_notices (user_id, `type`) VALUES (%s, 8);' % user_id
        self.db.select_data_from_db(request)
        return

    def ga_on(self, user_id):
        request = "INSERT Into google_authenticator (user_id, code, active, created_at, updated_at, `type`)" \
                      "values(%s, 11, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0); " % user_id
        self.db.select_data_from_db(request)
        return

    def ga_off_email_off(self, user_id):
        request = "Delete from google_authenticator user_id = %s; " % user_id
        request1 = "DELETE from user_properties where user_id = %s and name = 'verify_method'; " % user_id
        self.db.select_data_from_db(request)
        self.db.select_data_from_db(request1)
        return

    # Получаем ид последнего авторизованного пользователя
    def get_user_id(self):
        request = "Select user_id From sessions " \
                  "Order by id desc limit 1; "
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_login_history(self, user_id):
        request = "Select DATE_FORMAT( `timestamp`, TIMESTAMP) From login_history where user_id = %s order by id desc limit 1;" % user_id
        timestamp = self.db.select_data_from_db(request)
        return timestamp[0]

    def get_user_id_for_cash_swift(self):
        request = "SELECT user_id, email " \
                  "FROM user_personal_data upd " \
                  "WHERE upd.citizenship_country_id = 1 " \
                  "and verification_status_id = 5"
        user_id, username = self.db.select_data_from_db(request)
        return user_id, username

    def get_user_id_for_cash_paysystem(self, ps):
        request = f"SELECT user_id, email FROM user_personal_data upd " \
                  "join payment_systems_available_countries psac on upd.reg_address_country_id = psac.country_id " \
                  f"where psac.payment_system_id = {ps} and upd.verification_status_id = 5 " \
                  "order by upd.id desc;"
        user_id, username, = self.db.select_data_from_db(request)
        return user_id, username,

    def change_block_status(self, user_id):
        request = "UPDATE user_properties SET value = 0 " \
                  "WHERE user_id = %s " \
                  "and name in ('block_transfer', 'block_account_a', 'block_account_b', " \
                  "'block_account_c', 'block_account_out', 'block_withdrawal', 'block_cashin');" % user_id
        self.db.select_data_from_db(request)
        return

    # Получаем баланс пользователя - сумма с трех кошельков
    def balance(self, user_id):
        time.sleep(4)
        request = "Select SUM(sum) From accounts Where user_id = %s and type in ('A', 'B', 'C');" % user_id
        balance = self.db.select_data_from_db(request)
        return balance[0]

    def ps_list(self):
        request = "SELECT id FROM user_payment_accounts_types upat  where enable_for_request = 1;"
        ps_list = self.db.select_a_lot_of_data_from_db(request)
        return ps_list

    def account_balance(self, user_id, account):
        if account == 'main':
            account = 'A'
        elif account == 'bonus':
            account = 'B'
        request = "Select sum From accounts " \
                  "Where user_id = %s " \
                  "and type in ('%s') " \
                  "Order by id; " % (user_id, account)
        time.sleep(1)
        account = self.db.select_data_from_db(request)
        return int(account[0])

    # Ищем последний сертификат пользователя
    def get_certificate(self, user_id):
        request = "SELECT actions_qnt, status " \
                  "FROM certificates " \
                  "Where user_id = (%s) " \
                  "Order by id desc limit 1;" % user_id
        actions_qnt, status = self.db.select_data_from_db(request)
        return actions_qnt, status

    # Поиск последнего ордера (может быть уже оплачен)
    def get_order_new(self, user_id):
        request = "SELECT actions_qnt, status, id " \
                  "FROM orders " \
                  "Where id_user = (%s) " \
                  "Order by id desc limit 1;" % user_id
        actions_qnt, status, order_id = self.db.select_data_from_db(request)
        return actions_qnt, status, order_id

    # Поиск последнего созданного ордера
    def get_order(self, user_id):
        request = "SELECT actions_qnt, status, id " \
                  "FROM orders " \
                  "Where id_user = (%s) " \
                  "Order by id desc limit 1;" % user_id
        (actions_qnt, status, order_id) = self.db.select_data_from_db(request)
        return actions_qnt, status, order_id

    def get_shares_for_double_payment(self, user_id, coupon=1):
        request = "SELECT actions_qnt, status " \
                  "FROM orders " \
                  "Where id_user = %s " \
                  "Order by id desc limit 1;" % user_id
        actions_qnt, status = self.db.select_data_from_db(request)
        if coupon > 1:
            request = "SELECT CONVERT(SUM(t.sum), INT) FROM `transaction` t Join accounts a on a.id = t.account_id " \
                  "WHERE a.user_id = %s and a.`type` = 'D' order by t.id desc limit %s;" % (user_id, coupon)
        else:
            request = "SELECT t.sum FROM `transaction` t Join accounts a on a.id = t.account_id " \
                  "WHERE a.user_id = %s and a.`type` = 'D' order by t.id desc limit %s;" % (user_id, coupon)
        sum = self.db.select_a_lot_of_data_from_db(request)
        total_shares = int(actions_qnt) + int(sum[0][0])
        return total_shares, status

    # Поиск последнего купона
    def get_last_coupon(self, user_id):
        time.sleep(2)
        _format = ('"%d.%m.%Y"')
        time_request = "SELECT DATE_FORMAT(SYSDATE(),%s);" % _format
        _time = self.db.select_data_from_db(time_request)
        request = "SELECT DATE_FORMAT(created_at, %s), created_for_order_id, status, activated " \
                  "FROM coupons " \
                  "Where user_id = (%s) " \
                  "and activation_date is NULL " \
                  "Order by id desc;" % (_format, user_id)
        date, order_id, status, activated = self.db.select_data_from_db(request)
        assert date == _time[0], 'Не тот купон'
        return order_id, status, activated

    def get_order_instalment(self, user_id):
        request = "SELECT o.id, od.packet_id, payments_left " \
                  "FROM orders o  join orders_detail od on o.id = od.orders_id " \
                  "Where id_user = (%s) " \
                  "and o.status = 1  " \
                  "and o.instalment = 1  " \
                  "Order by o.id desc limit 1;" % user_id
        order_id, packet_id, payments_left = self.db.select_data_from_db(request)
        return order_id, packet_id, payments_left

    def get_payments_left(self, order_id):
        request = f"SELECT payments_left FROM orders od where id ={order_id};"
        payments_left = self.db.select_data_from_db(request)
        return payments_left[0]

    def late_payment(self, order_id):
        request = "SELECT o.id, od.packet_id, payments_left " \
                  "FROM orders o  join orders_detail od on o.id = od.orders_id " \
                  "Where id_user = (%s) " \
                  "and o.status = 1  " \
                  "and o.instalment = 1  " \
                  "Order by o.id desc limit 1;" % order_id
        order_id, packet_id, payments_left = self.db.select_data_from_db(request)
        return order_id, packet_id, payments_left

    # Поиск swift
    def check_swift_agreement(self, user_id):
        request = "Select b.operation, b.paysystem_type, b.status, b.amount_2, sa.actions_qnt " \
                  "From billing b join swift_agreement sa on b.id = sa.bill_id " \
                  "Where b.user_id = %s " \
                  "Order by b.id desc limit 1;" % user_id
        operation, paysystem_type, status, price, shares = self.db.select_data_from_db(request)
        return operation, paysystem_type, status, float(price), shares

    # Получить код подтверждения перевода
    def get_verify_code_transfer(self, user_id):
        request = "Select sms_code " \
                  "From money_transfer " \
                  "Where user_id_from = %s " \
                  "Order by id desc limit 1;" % user_id
        value = self.db.select_data_from_db(request)
        return value

    # Ищет верифицированного пользователя для перевода
    def select_user_for_transfer(self):
        request = "Select user_id, email " \
                  "From user_personal_data " \
                  "Where verification_status_id = 5 " \
                  "Order by id limit 1;"
        user_id, email = self.db.select_data_from_db(request)
        return user_id, email

    # Ищет неверифицированного пользователя для перевода
    def select_unverified_user_for_transfer(self):
        request = "select username " \
                  "from user " \
                  "where verified_register = 0 " \
                  "Order by username desc limit 1;"
        email = self.db.select_data_from_db(request)
        return email[0]

    # Проверяет создан ли уже платежный реквизит по заданной платежной системе
    def check_accounts(self, value, user_id):
        request = "Select count(id) " \
                  "From user_payment_accounts " \
                  "Where user_id = %s " \
                  "and type_id = %s " \
                  "and hidden = 0; " % (user_id, value)
        value = self.db.select_data_from_db(request)
        return value

    def get_verify_code_cashout(self, user_id):
        request = "Select id " \
                  "From money_request " \
                  "Where user_id = %s " \
                  "Order by id desc limit 1 ;" % user_id
        mr_id = self.db.select_data_from_db(request)
        return mr_id[0]

    # Получает статус запроса для вывода
    def select_status_request(self, mr_id):
        request = "Select status " \
                  "From money_request " \
                  "Where id = %s; " % mr_id
        status = self.db.select_data_from_db(request)
        return status[0]

    # Получает статус запроса для вывода
    def select_time_stamp_request(self, mr_id):
        time.sleep(3)
        request = "Select cancel_after " \
                  "From money_request " \
                  "Where id = %s; " % mr_id
        cancel_after = self.db.select_data_from_db(request)
        return cancel_after[0]

    # def select_money_request_for_cancel(self, user_id):
    #     select_id = "Select max(id) " \
    #                 "from  money_request " \
    #                 "Where user_id = %s " \
    #                 "and (cancel_after is not Null or status = 1);" % user_id
    #     mr_id = self.db.select_data_from_db(select_id)
    #     return mr_id

    """Удаляем старый метод подтверждения и создаём новый"""

    def create_transaction_confirmation_for_user(self, user_id):
        delete_old_verify_method = "delete FROM user_properties " \
                                   "WHERE user_id = %s AND name = 'verify_method';" % user_id
        delete_old_pincode = "delete FROM user_properties " \
                             "WHERE user_id = %s AND name = 'pincode';" % user_id
        create_new_verify_method = "INSERT INTO user_properties (user_id, name, value) " \
                                   "VALUES (%s, 'verify_method', 'pin');" % user_id
        create_new_pincode = "INSERT INTO user_properties (user_id, name, value) " \
                             "VALUES (%s, 'pincode', \
                             '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');" % user_id
        self.db.select_data_from_db(delete_old_verify_method)
        self.db.select_data_from_db(delete_old_pincode)
        self.db.select_data_from_db(create_new_verify_method)
        self.db.select_data_from_db(create_new_pincode)
        return

    def delete_old_verify_method(self, user_id):
        delete_old_verify_method = "delete FROM user_properties " \
                                   "WHERE user_id = %s AND name = 'verify_method';" % user_id
        delete_old_pincode = "delete FROM user_properties " \
                             "WHERE user_id = %s AND name = 'pincode';" % user_id
        self.db.select_data_from_db(delete_old_verify_method)
        self.db.select_data_from_db(delete_old_pincode)
        return

    """Обновляем метод подтверждения транзакции, делаем подтверждение пинкодом
    Устанавливаем пинкод - 1234"""

    def update_transaction_confirmation_for_user(self, user_id):
        update_confirmation = "UPDATE user_properties " \
                              "SET value = 'pin' " \
                              "WHERE user_id = %s " \
                              "and name='verify_method'" % user_id
        update_pincode = "UPDATE user_properties " \
                         "SET value = '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4' " \
                         "WHERE user_id = %s " \
                         "and name = 'pincode'" % user_id
        self.db.update_data(update_confirmation)
        self.db.update_data(update_pincode)
        return

    """Проверяем, что установлен метод подтверждения
    по пинкоду"""

    def check_verify_method(self, user_id):
        request = "SELECT value from user_properties up " \
                  "where user_id = %s and name = 'verify_method';" % user_id
        result = self.db.select_data_from_db(request)
        return result[0]

    def update_money_request_cancel(self, mr_id, user_id):
        update_status = "Update money_request " \
                        "Set status = 3 " \
                        "Where id = %s ;" % mr_id
        update_time_stamp = "Update money_request  " \
                            "Set cancel_after = Null " \
                            "Where id = %s ;" % mr_id
        self.db.update_data(update_status)
        self.db.update_data(update_time_stamp)
        return

    def update_money_request(self, mr_id, user_id):
        update_status = "Update money_request " \
                        "Set status = 2 " \
                        "Where id = %s " \
                        "and user_id = %s ;" % (mr_id, user_id)
        self.db.update_data(update_status)
        return

    # def update_money_request_cancel(self, user_id):
    #     mr_id = self.select_money_request_for_cancel(user_id)
    #     self.update_money_request(mr_id, user_id)

    # Ищет тип платежной системы, которая указана в заявке на вывод
    def payment_account_type(self, mr_id, user_id):
        request = "Select name " \
                  "From money_request mr " \
                  "join user_payment_accounts upa on mr.payment_account_id = upa.id " \
                  "join user_payment_accounts_types upat on upa.type_id = upat.id " \
                  "Where mr.id = '%s' and mr.user_id = '%s' ;" % (mr_id, user_id)
        type_ps = self.db.select_data_from_db(request)
        return type_ps

    # Ищет последний биллинг по пользователю
    def get_billing(self, user_id):
        time.sleep(1)
        request = "Select operation, status, paysystem_type, amount_2, id " \
                  "From billing " \
                  "Where user_id = %s " \
                  "Order by id desc limit 1;" % user_id
        operation, status, paysystem_type, amount, bill_id = self.db.select_data_from_db(request)
        return operation, status, paysystem_type, int(amount), bill_id

    # Ищет последний биллинг по пользователю для swift
    def get_swift(self, user_id, bill_id):
        request = "Select currency_id " \
                  "From swift_agreement " \
                  "Where user_id = %s " \
                  "and bill_id = %s " \
                  "Order by id desc limit 1;" % (user_id, bill_id)
        currency_id = self.db.select_data_from_db(request)
        return currency_id[0]

    # Исправляем статусы сертификата на 8 и ордер заказа у пользователя, нужно для заказа
    def update_meta_cert(self, user_id):
        time.sleep(4)
        update_status = "UPDATE meta_certificates set status = 8 " \
                        "WHERE user_id = %s;" % user_id
        update_order_id = "UPDATE meta_certificates set cert_delivery_order_id = NULL " \
                          "WHERE user_id = %s;" % user_id
        self.db.select_data_from_db(update_status)
        time.sleep(2)
        self.db.select_data_from_db(update_order_id)
        time.sleep(1)
        return

    # Ищет метасертификат пользователя со статусом 8
    def get_user_id_meta_cert(self):
        request = "Select user_id, id From meta_certificates mc " \
                  "Where mc.status = 8 " \
                  "and mc.cert_delivery_order_id is Null " \
                  "and n_first_name is Null " \
                  "and created_at LIKE '2018_______________' " \
                  "Order by id desc limit 1 offset 1;"
        user_id, cert_id = self.db.select_data_from_db(request)
        return user_id, cert_id

    def change_status_meta_cert(self):
        request = "Select user_id ,id from meta_certificates mc " \
                  "where user_id = 259 " \
                  "Order by id desc limit 1 offset 1;"
        request_change_status = "UPDATE meta_certificates " \
                                "set status = 8 where user_id = 259;"
        self.db.select_data_from_db(request_change_status)
        user_id, cert_id = self.db.select_data_from_db(request)
        return user_id, cert_id

    def get_id_meta_cert(self, user_id):
        request = "Select id From meta_certificates mc " \
                  "Where mc.status = 8 and mc.cert_delivery_order_id is Null " \
                  "and n_first_name is Null and created_at LIKE '2018_______________' " \
                  "and user_id = %s Order by id desc limit 1 offset 1;" % user_id
        cert_id = self.db.select_data_from_db(request)
        return cert_id[0]

    # Ищет кол-во метасертфикатов у пользователя, которые еще не были заказаны
    def select_meta_cetrs(self, user_id):
        request = "Select count(id) From meta_certificates mc " \
                  "Where mc.status = 8 " \
                  "and mc.cert_delivery_order_id is Null " \
                  "and n_first_name is Null " \
                  "and user_id = %s; " % user_id
        value = self.db.select_data_from_db(request)
        return value[0]

    def meta_certs(self):
        request = "Select id, user_id, union_cert_number From meta_certificates mc " \
                  "Where mc.status = 8 " \
                  "and mc.cert_delivery_order_id is Null and mc.user_id != 140742 " \
                  "and n_first_name is Null and union_cert_number is not NULL " \
                  "GROUP by union_cert_number HAVING COUNT(union_cert_number)>1 order by id desc limit 1;"
        id, user_id, union_cert = self.db.select_data_from_db(request)
        return id, user_id, union_cert

    def get_certificate_statuses(self, user_id):
        request = "Select mc.status, d.status, d.fio " \
                  "From meta_certificates mc " \
                  "join certificate_delivery_order d on mc.id = d.meta_certificate_id " \
                  "Where mc.user_id = %s " \
                  "Order by mc.id desc limit 1;" % user_id
        mc_status, d_status, fio = self.db.select_data_from_db(request)
        return mc_status, d_status

    # Выводит статусы метасертификата
    def select_certificate_status(self, user_id, cert_id, union_cert):
        request = "Select mc.status, d.status, d.fio " \
                  "From meta_certificates mc " \
                  "join certificate_delivery_order d on mc.id = d.meta_certificate_id " \
                  "Where mc.user_id = %s " \
                  "Order by mc.id desc limit 1;" % user_id
        mc_status, d_status, fio = self.db.select_data_from_db(request)
        request2 = "Select mc.status " \
                  "From meta_certificates mc " \
                  "Where mc.user_id = %s and id != %s and union_cert_number = '%s' " \
                  "Order by mc.id desc;" % (user_id, cert_id, union_cert)
        print(request2)
        status2 = self.db.select_data_from_db(request2)
        print(status2[0])
        return mc_status, d_status, fio, status2[0]

    def get_count_innotrans(self, datetime, user_id):
        request = "Select count(o.id) From orders o join orders_detail od on o.id = od.orders_id " \
                  "Where date > '%s' " \
                  "and packet_id in (764,765,766) " \
                  "and status = 3 " \
                  "and id_user = %s" % (datetime, user_id)
        count_innotrans = self.db.select_data_from_db(request)
        return int(count_innotrans[0])

    def get_new_user_data(self):
        request = "Select firstname, phone, username, id, verified_register_code " \
                  "From user " \
                  "Order by id desc limit 1; "
        firstname, phone, email, user_id, verified_code = self.db.select_data_from_db(request)
        return firstname, phone, email, int(user_id), verified_code

    def get_verified_register_new_user(self, user_id):
        request = "Select verified_register, verified_email " \
                  "From user " \
                  "Where id = %s; " % user_id
        verified_register, verified_email = self.db.select_data_from_db(request)
        return verified_register, verified_email

    """Ищем последний реквизит у пользователя"""

    def get_last_id_money_request(self, user_id):
        request = "Select id " \
                  "From user_payment_accounts " \
                  "Where user_id = '%s' " \
                  "Order by id desc limit 1;" % user_id
        pa_id = self.db.select_data_from_db(request)
        return pa_id[0]

    def create_new_pa(self, user_id, pa_id):
        request = "INSERT into money_request (user_id, payment_account_id, status, sms_verified) " \
                  "values ('%s', '%s', '2', '1')" % (user_id, pa_id)
        self.db.select_data_from_db(request)
        self.db.select_data_from_db(request)
        self.db.select_data_from_db(request)
        return

    def get_verified_status_user(self, user_id):
        time.sleep(3)
        request = "Select verification_status_id " \
                  "From user_personal_data " \
                  "Where user_id = %s; " % user_id
        verification_status_id = self.db.select_data_from_db(request)
        return verification_status_id[0]

    def autopayment_off(self, orders_id):
        update_enabled = "UPDATE instalment_autopayment " \
                         "SET enabled = 0 where order_id = %s;" % orders_id
        update_recurrent = "UPDATE instalment_autopayment " \
                           "SET recurrent = 0 where order_id = %s;" % orders_id
        self.db.select_data_from_db(update_enabled)
        self.db.select_data_from_db(update_recurrent)
        return

    def search_user(self, orders_id):
        request = "SELECT id_user FROM instalment_schedule i " \
                  "join orders o on i.order_id = o.id " \
                  "where o.id = %s;" % orders_id
        id_user = self.db.select_data_from_db(request)
        request1 = "UPDATE user_personal_data set verification_status_id = 5 WHERE user_id = %s;" % id_user
        self.db.select_data_from_db(request1)
        return id_user[0]

    # Ищем и запоминаем страну у пользователя. Меняем на Латвию. Затем возвращаем исходную.
    # Нужно для Мигомсепа, так как он дружит только с выбранными странами
    def search_user_for_migomsepa(self, user_id):
        request = "SELECT reg_address_country_id " \
                  "FROM user_personal_data " \
                  "WHERE user_id = %s;" % user_id
        user_personal_data = self.db.select_data_from_db(request)
        return user_personal_data[0]

    def chosen_latvia(self, user_id):
        request = "UPDATE user_personal_data " \
                  "SET citizenship_country_id = 12 " \
                  "WHERE user_id = %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def return_country(self, user_id, user_personal_data):
        request = "UPDATE user_personal_data " \
                  "SET reg_address_country_id = %s " \
                  "WHERE user_id = %s;" % (user_personal_data, user_id)
        self.db.select_data_from_db(request)
        return

    # Ищем id юзеров в последних купленных рассрочках, затем выбираем того, кто прошёл верификацию
    def search_user_id_array(self):
        request = "SELECT id_user " \
                  "FROM instalment_schedule i join orders o on i.order_id = o.id " \
                  "where o.status not in (7,3,6) " \
                  "and o.deleted_by = 0 " \
                  "ORDER BY id_user DESC limit 2000;"
        id_user_tuple = self.db.select_a_lot_of_data_from_db(request)
        table = str.maketrans("", "", "()")
        id_user = ''.join(map(str, id_user_tuple))
        id_user = id_user.translate(table)
        request_next = "SELECT id_user FROM instalment_schedule i join orders o on i.order_id = o.id " \
                       "where order_id like '______' " \
                       "and id_user in (%s%s);" % (id_user, 0)
        user_id_tuple = self.db.select_a_lot_of_data_from_db(request_next)
        table = str.maketrans("", "", "()")
        id_user = ''.join(map(str, user_id_tuple))
        id_user = id_user.translate(table)
        request_new = "SELECT user_id " \
                      "from user_personal_data upd " \
                      "where user_id in (%s%s) and verification_status_id = 5;" % (id_user, 0)
        user_id = self.db.select_data_from_db(request_new)
        return user_id[0]

    # Ищем пользователя без 10-ти процентного бонуса к долям
    def search_user_without_bonus(self):
        request = "SELECT user_id FROM user_personal_data upd " \
                  "WHERE verification_status_id = 5 " \
                  "order by user_id desc limit 1 offset 2000;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def search_reset_token(self, username):
        request = "SELECT password_reset_token from user " \
                  "WHERE username = '%s'" % username
        password_reset_token = self.db.select_data_from_db(request)
        return password_reset_token[0]

    def name_of_user(self, username):
        request = "SELECT first_name_en, last_name_en from user_personal_data where email = '%s';" % username
        first_name_en, last_name_en = self.db.select_data_from_db(request)
        return first_name_en, last_name_en

    def search_user_for_old_installment(self, packet):
        """Найти пользователя, которому доступна оплата дисконта"""
        request = "SELECT od.orders_id " \
                  "FROM orders_detail od join instalment_schedule i on od.orders_id = i.order_id " \
                  "WHERE od.packet_id in (%s) and i.paid = 0 " \
                  "ORDER BY orders_id DESC limit 1;" % packet
        orders_id = self.db.select_data_from_db(request)
        if orders_id == None:
            user_id = None
            return user_id, orders_id
        self.autopayment_off(orders_id)
        user_id = self.search_user(orders_id[0])
        return user_id, orders_id[0]

    def search_user_for_old_disabled_installment(self, packet, multi):
        """Найти пользователя, которому доступна оплата дисконта"""
        request = f"SELECT od.orders_id FROM orders_detail od " \
                  "join instalment_schedule i on od.orders_id = i.order_id " \
                  f"WHERE od.packet_id in ({packet}) and i.paid = 1 and " \
                  "orders_id in (SELECT o.id from orders o join coupons c on o.id_user = c.user_id where " \
                  f"c.multiplier = {multi} and c.valid_until >= SYSDATE() order by c.valid_until desc) " \
                  "ORDER BY orders_id DESC limit 1;"
        orders_id = self.db.select_data_from_db(request)
        if orders_id == None:
            user_id = None
            return user_id
        self.autopayment_off(orders_id)
        user_id = self.search_user(orders_id)
        return user_id

    def search_partner(self, user_id):
        request = "SELECT partner_id from user where id = %s;" % user_id
        partner_id = self.db.select_data_from_db(request)
        return partner_id[0]

    def check_partnership_agreement(self, user_id):
        request = "SELECT agreement_signed from user where id = %s" % user_id
        agreement = self.db.select_data_from_db(request)
        return agreement[0]

    def get_user_id_successor(self):
        request = "Select id From user u " \
                  "Where id NOT IN (SELECT user_id FROM user_successor) " \
                  "and u.verified_email = 1 " \
                  "and u.allow_info_support = 0 " \
                  "and u.verified_phone = 0 " \
                  "and u.agreement_signed = 1 " \
                  "and u.mark_delete = 0 " \
                  " limit 1;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_new_successor(self):
        request = "Select fullname, email " \
                  "From user_successor " \
                  "Order by id desc limit 1; "
        fullname, email = self.db.select_data_from_db(request)
        return fullname, email

    def get_info(self, user_id):
        request = "Select allow_info_support " \
                  "From user " \
                  "Where id = %s " \
                  "Order by id desc limit 1;" % user_id
        allow_info_support = self.db.select_data_from_db(request)
        return allow_info_support[0]

    def get_contacts(self, user_id):
        request = "Select skype, phone_2 " \
                  "From user " \
                  "Where id = %s ;" % user_id
        skype_db, phone_2_db = self.db.select_data_from_db(request)
        return skype_db, phone_2_db

    def get_user_for_transactions_sms(self):
        request = "Select user_id From user_properties " \
                  "Where value = 'sms' " \
                  "Order by id desc limit 1;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_user_for_transactions_tg(self):
        request = "select id from user where exists(select user_id from user_properties " \
                  "where user.id = user_id and user_properties.name = 'pincode' " \
                  "and user_properties.value = '0') and exists(select user_id " \
                  "from user_properties where user.id = user_id and user_properties.name = 'verify_method' " \
                  "and user_properties.value = 'telegram') ORDER BY id desc limit 1;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_user_for_transactions_email(self):
        request = "select id from user where exists(select user_id from user_properties " \
                  "where user.id = user_id and user_properties.name = 'pincode' " \
                  "and user_properties.value = '0') and exists(select user_id " \
                  "from user_properties where user.id = user_id and user_properties.name = 'verify_method' " \
                  "and user_properties.value = 'email') ORDER BY id desc limit 1;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_user_for_transactions_ga(self):
        request = "select id from user where exists(select user_id from user_properties " \
                  "where user.id = user_id and user_properties.name = 'pincode' " \
                  "and user_properties.value = '0') and exists(select user_id " \
                  "from user_properties where user.id = user_id and user_properties.name = 'verify_method' " \
                  "and user_properties.value = 'ga') ORDER BY id desc limit 1;"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_user_id_notification_email(self):
        request = "Select id, email, phone From user u " \
                  "Where u.notification_email is null " \
                  "and u.verified_email = 1 " \
                  "and u.allow_info_support = 0 " \
                  "Order by id desc limit 1;"
        user_id, current_email, current_phone = self.db.select_data_from_db(request)
        return user_id, current_email, current_phone

    def get_user_for_transactions_pin(self):
        request = "select id from user where exists(select user_id from user_properties " \
                  "where user.id = user_id and user_properties.name = 'pincode' " \
                  "and user_properties.created_at is null)" \
                  "and user.verified_register = 1 " \
                  "and exists(select user_id " \
                  "from user_properties where user.id = user_id and user_properties.name = 'verify_method' " \
                  "and user_properties.value = 'pin') ORDER BY id desc limit 1"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    # Ищем перевод денег, затем получаем номера транзакций для этого перевода, из них выбираем исходящую
    def search_money_transfer(self, user_id_from, user_id_to):
        time.sleep(2)
        request = "SELECT id FROM money_transfer mt " \
                  "WHERE user_id_from = %s and user_id_to = %s " \
                  "Order by id desc limit 1;" % (user_id_from, user_id_to)
        money_transfer_id = self.db.select_data_from_db(request)
        return money_transfer_id[0]

    def search_transactions_id(self, money_transfer_id):
        request = "SELECT transaction_id FROM money_transfer_transaction mtt " \
                  "WHERE money_transfer_id = %s;" % money_transfer_id
        print(request)
        transaction_id = self.db.select_a_lot_of_data_from_db(request)
        print(transaction_id)
        return transaction_id[0][0], transaction_id[1][0]

    def choose_transaction_from(self, transaction_id_from, transaction_id_to):
        request = "SELECT id FROM `transaction` t " \
                  "where id = %s or id = %s and " \
                  "initiator_user_id = NULL;" % (transaction_id_from, transaction_id_to)
        transaction_id = self.db.select_data_from_db(request)
        return transaction_id[0]

    def user_for_swift_invoice(self):
        request = "SELECT id, user_id, email FROM swift_agreement " \
                  "Order by id desc limit 1;"
        operation_id, user_id, email = self.db.select_data_from_db(request)
        request1 = f"UPDATE swift_agreement set status=0 WHERE id={operation_id};"
        self.db.update_data(request1)
        return operation_id, user_id, email

    def get_user_for_verification_child(self):
        request = "select user_id from user_personal_data " \
                  "where underage = 1 " \
                  "and verification_status_id = 5 and citizenship_country_id = 20 " \
                  "ORDER BY id desc limit 1"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_verified_status_child(self, user_id):
        request = "Select verification_status_id, first_name_en " \
                  "From user_personal_data " \
                  "Where user_id = %s ORDER BY id desc limit 1 " % user_id
        verification_status_id, first_name = self.db.select_data_from_db(request)
        return verification_status_id, first_name

    def change_month_instalment(self, order_id):
        request = "UPDATE instalment_schedule " \
                  "set real_date = date_add(real_date, INTERVAL -1 MONTH) " \
                  "where order_id = %s and paid = 1; " % order_id
        self.db.select_data_from_db(request)
        return

    def postpone_certificate(self, user_id):
        request = "SELECT id from certificates c2 where exists " \
                  "(SELECT id from orders o where id_user = %s and " \
                  "o.id = c2.order_id Order by id desc limit 1) " \
                  "Order by id desc limit 1;" % user_id
        certificate_id = self.db.select_data_from_db(request)
        return certificate_id[0]

    def get_user_for_display_id(self):
        request = "SELECT u_s.partner_id, u_s.user_id FROM user_structure u_s Join user u ON u.id = u_s.partner_id " \
                  "join user_personal_data upd ON upd.user_id = u_s.user_id " \
                  "join user_properties up ON up.user_id=u_s.partner_id " \
                  "WHERE u_s.lvl = 1 and u.mark_delete != 1 and upd.verification_status_id =5 and " \
                  "u.verified_register = 1 and up.name ='verify_method' and u_s.user_id not IN " \
                  "(Select up2.user_id from user_properties up2 where up2.name = 'hidden_name') " \
                  "order by u_s.partner_id desc;"
        partner_id, user_id = self.db.select_data_from_db(request)
        request2 = f"INSERT INTO user_properties (user_id, name, value ) values ({partner_id}, 'hidden_name', 1);"
        self.db.select_data_from_db(request2)
        return partner_id, user_id

    def update_id_status_fifth(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 5 " \
                  "where t.user_id =  %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def update_id_status_first(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 1 " \
                  "where t.user_id =  %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def update_id_status_third(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 3 " \
                  "where t.user_id =  %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def update_id_status_seventeen(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 17 " \
                  "where t.underage = 1 and t.verification_status_id = 2 and t.user_id =  %s ORDER BY id desc limit 1;" % user_id
        self.db.select_data_from_db(request)
        return

    def create_curator(self, random_numbers, user_id):
        request = "INSERT curators(id, descr, comment) " \
                  "VALUES (%s, 'testForCurators', DEFAULT); " % random_numbers
        request_2 = "INSERT curator_to_user(curator_id, user_id, status, sign_date) " \
                    "VALUES (%s, %s, DEFAULT, DEFAULT); " % (random_numbers, user_id)
        request_3 = "INSERT curator_to_countries(curator_id, country_id) " \
                    "VALUES (%s,20);" % random_numbers
        self.db.select_data_from_db(request)
        self.db.select_data_from_db(request_2)
        self.db.select_data_from_db(request_3)
        return

    def create_conference(self, ):
        data_reg = '["self_registered","self_verified","partner_registered","partner_verified","guest"]'
        lang = '["ru", "en"]'
        price = 777
        request_time = "SELECT SYSDATE(), UNIX_TIMESTAMP(), DATE_FORMAT(SYSDATE(),'%Y-%m-%d');"
        curtime, unix_time, start_date = self.db.select_data_from_db(request_time)
        request_date = "SELECT DATE_ADD('%s', INTERVAL 1 DAY)" % start_date
        end_date = self.db.select_data_from_db(request_date)
        request = "INSERT into event_list " \
            "(title, creator_id, created_at, start_date, end_date, " \
            "use_default_form, is_active, tickets_available, register_end_date, is_free) " \
            "values ('New_test_rega', 91, %s, '%s',  '%s', 1, 1, 1, '%s', 0);" % (unix_time, start_date, end_date[0], end_date[0])
        self.db.select_data_from_db(request)
        time.sleep(3)
        request_1 = "SELECT id from event_list el order by id desc limit 1;"
        id = self.db.select_data_from_db(request_1)
        request_2 = "INSERT into event_list_text " \
            "(news_id, language, title , text_short, text_long, is_public, town, cost, spicker_list, address, rasp) " \
            "values " \
            "(%s, 'ru', 'FOR TEST', '<p>TEST</p>',  '<p>TEST</p>', 1, 'TEST', 333, '<p>TEST</p>', '<p>TEST</p>','<p>TEST</p>');" % id[0]
        self.db.select_data_from_db(request_2)
        request_3 = "INSERT into event_enrollment_type " \
            "(event_id, source_message_id, available_user_types, name, amount, deleted, " \
            "created_by, updated_by, created_at, updated_at, active, activated_by, available_lang_codes) " \
            "values (%s, 32397, '%s', " \
            "'Конференция', %s,  0, 91, 91, '%s', '%s', 1, 91, '%s');" % (id[0], data_reg, price, curtime, curtime, lang)
        self.db.select_data_from_db(request_3)
        return id[0], price

    def get_code_for_phone(self, user_id):
        request = "select verified_phone_code from user u " \
                  "where u.id =  %s;" % user_id
        code_phone = self.db.select_data_from_db(request)
        return code_phone[0]

    def update_id_status_second(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 2 " \
                  "where t.user_id =  %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def update_id_status_fifteenth(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 15 " \
                  "where t.user_id =  %s;" % user_id
        self.db.select_data_from_db(request)
        return

    def update_id_status_sixteenth(self, user_id):
        request = "update user_personal_data t " \
                  "set t.verification_status_id = 16 " \
                  "where t.verification_status_id = 17 and t.user_id =  %s ORDER BY t.last_update desc limit 1;" % user_id
        self.db.select_data_from_db(request)
        return

    def get_email_phone_for_reg(self):
        request = "Select email, phone From user u " \
                  "Where u.notification_email is null " \
                  "and u.verified_email = 1 " \
                  "and phone like '%7' " \
                  "Order by id desc limit 1;"
        current_email, current_phone = self.db.select_data_from_db(request)
        return current_email, current_phone

    def search_user_with_structure(self):
        request = "SELECT us.partner_id from user_structure us " \
                  "where us.user_id is not NULL and partner_id not in (1);"
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def search_structure(self, partners_id):
        request = "SELECT user_id FROM user_structure us " \
                  "where partner_id = %s;" % partners_id
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_ps_list(self):
        request = "SELECT id, type " \
                  "from payment_systems ps " \
                  "where lk_enabled = 1 and type != 3;"
        ps_list = self.db.select_a_lot_of_data_from_db(request)
        return ps_list

    def get_settings_ps(self, paysystem):
        request = "SELECT lk_commission, min_sum, max_sum " \
                  "from payment_systems ps " \
                  "where id = %s" % paysystem
        lk_commission, min_sum, max_sum = self.db.select_data_from_db(request)
        return float(lk_commission), int(min_sum), int(max_sum)

    def get_fixed_commission_ps(self, paysystem):
        request = "SELECT fixed_commission " \
                  "from payment_systems ps " \
                  "where id = %s" % paysystem
        fixed_commission = self.db.select_data_from_db(request)
        return float(fixed_commission[0])

    def update_settings_ps(self, commission, fixed_commission, min_sum, max_sum, paysystem):
        update_commission = "UPDATE payment_systems " \
                            "Set lk_commission = %s where id = %s" % (commission, paysystem)
        update_min_sum = "UPDATE payment_systems " \
                         "Set min_sum = %s where id = %s" % (min_sum, paysystem)
        update_max_sum = "UPDATE payment_systems " \
                         "Set max_sum = %s where id = %s" % (max_sum, paysystem)
        update_fixed_commission = "UPDATE payment_systems " \
                                  "Set fixed_commission = %s where id = %s" % (fixed_commission, paysystem)
        self.db.select_data_from_db(update_commission)
        self.db.select_data_from_db(update_min_sum)
        self.db.select_data_from_db(update_max_sum)
        self.db.select_data_from_db(update_fixed_commission)
        return

    # получаем курс доллара
    def rate_usd(self):
        request = "SELECT value FROM currency c where code = 'USD';"
        rate_usd = self.db.select_data_from_db(request)
        return float(rate_usd[0])

    def get_user_for_display_id_ref(self, user_id_ref):
        request = "SELECT user_id FROM user_structure us " \
                  "where us.lvl = 1 and us.partner_id = %s and " \
                  "us.user_id not IN (Select user_id from user_properties up where name = 'hidden_name') " \
                  "ORDER BY id desc limit 1;" % user_id_ref
        user_id = self.db.select_data_from_db(request)
        return user_id[0]

    def get_date_of_transaction(self, aD, aC, aB, aA):
        _format = ('"%d.%m.%Y"')
        request = f"SELECT DATE_FORMAT(date, {_format})  from `transaction` t where account_id IN{aD, aC, aB, aA} " \
                  f"order by id desc limit 1;"
        date = self.db.select_data_from_db(request)
        return date[0]

    def get_types_of_transaction(self, aD, aC, aB, aA):
        request = f"SELECT DISTINCT account_type  from `transaction` t " \
              f"where account_id IN{aD, aC, aB, aA} order by id desc;"
        types = self.db.select_a_lot_of_data_from_db(request)
        print(types)
        return types

    def select_user_for_transfer_id(self, user_id_ref):
        request = "select username " \
                  "from user " \
                  "where id = %s " \
                  "Order by username desc limit 1;" % user_id_ref
        email = self.db.select_data_from_db(request)
        return email[0]

    def select_user_for_overdraft(self):
        request = "SELECT DISTINCT u.id, u.username from user u " \
                  "WHERE u.id IN (SELECT uan.user_id from user_alert_notices uan where uan.`type` = 8) " \
                  "order by u.id desc limit 1;"
        user_id, username = self.db.select_data_from_db(request)
        print(user_id)
        request = "DELETE from user_properties " \
                  "where name = 'overdraft_agreement_signed' and user_id = %s;" % user_id
        self.db.select_data_from_db(request)
        return user_id, username

    def check_donate(self, user_id, multi):
        _format = ("'%d.%m.%Y'")
        time_request = "SELECT DATE_FORMAT(SYSDATE(),%s);" % _format
        date_now = self.db.select_data_from_db(time_request)
        request = f"SELECT c.id, DATE_FORMAT(c.created_at, {_format}) from coupons c " \
                  f"WHERE c.user_id = {user_id} and c.type = 5 and c.multiplier = {multi} " \
                  f"order by c.id limit 1;"
        coupon_id, date = self.db.select_data_from_db(request)
        assert date_now[0] == date, f'Дата {date_now[0]} не равны {date}'
        request = "SELECT c.id from coupons c " \
                  "WHERE c.user_id = %s " \
                  "order by c.id desc limit 1;" % user_id
        last_coupon_id = self.db.select_data_from_db(request)
        assert coupon_id == last_coupon_id[0], f'Купоны {coupon_id} не равны {last_coupon_id[0]}'
        return coupon_id

    def coupons_date_for_donate(self, coupon_id):
        validity = (['>', 7], ['<', 3]) # изменения по срокам купонов после 2021-04-12 23:10:45.000
        for n in validity:
            try:
                request = f"SELECT DATEDIFF(c.valid_until, c.created_at) from coupons c " \
                          f"WHERE c.id = {coupon_id} and created_at {n[0]} '2021-04-12 23:10:45.000';"
                datediff = self.db.select_data_from_db(request)
                print(datediff[0])
                assert datediff[0] == n[1], f'Срок действия купона = {datediff} не равен {n[1]}'
            except:
                continue

    def change_coupon_valid_date(self, coupon_id):
        request = f"UPDATE coupons c SET c.valid_until = SYSDATE() where c.id = {coupon_id};"
        datediff = self.db.update_data(request)
        time.sleep(0.5)

    def expired_coupon(self):
        request = "SELECT c.id, c.user_id, u.username  FROM coupons c join user u on c.user_id = u.id " \
                  "WHERE c.type = 5 and c.status = 6 and c.valid_until < SYSDATE() and u.mark_delete = 0 " \
                  "order by c.id desc limit 1;"
        coupon_id, user_id, username = self.db.select_data_from_db(request)
        return coupon_id, user_id, username

    def deactivate_coupon(self,user_id):
        request = f"UPDATE coupons SET activated = 0 WHERE activated = 1 and user_id = {user_id};"
        self.db.select_data_from_db(request)
        time.sleep(2.5)

    def donating_coupons_date(self, coupon_id):
        request = f"SELECT DATEDIFF(c.valid_until, c.created_at) from coupons c WHERE c.id = {coupon_id};"
        datediff = self.db.select_data_from_db(request)
        assert datediff[0] == 7, f'Срок действия купона = {datediff} не равен 7'

    def set_copons_type(self, coupon_id, type):
        request = f"UPDATE coupons c set c.type = {type} WHERE c.id = {coupon_id};"
        self.db.select_data_from_db(request)

    def get_paysystems(self, currency):
        request =f"SELECT id FROM payment_systems ps where lk_enabled=1 and name_printed_en = '{currency}'"
        paysystems = self.db.select_a_lot_of_data_from_db(request)
        paysystems = list(x[0] for x in paysystems)
        return paysystems

    def get_last_cert_id(self, user_id):
        request = f"SELECT id from certificates c WHERE user_id ={user_id}  order by id desc;"
        cert_id = self.db.select_data_from_db(request)
        return cert_id[0]

