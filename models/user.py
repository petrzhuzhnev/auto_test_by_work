import time

TEST_ACCOUNT_SUM = 300000


class User:

    def __init__(self, db):
        self.db = db

    def select_user(self, sql_request):
        user = self.db.select_data_from_db(sql_request)
        user_id, username = user
        username = username.replace("'", "")
        return user_id, username

    def update_new_user(self, user_id):
        update_accounts = "UPDATE user_personal_data " \
                          "SET user_id = %s " \
                          "WHERE verification_status_id=5 " \
                          "Order by id desc limit 1;" % user_id
        self.db.update_data(update_accounts)

    def update_user_password(self, user_id):
        auth_key = 'hHh_hpSzRKqfL-KXn7yC3l6omOns3i9Z'
        password_hash = '$2y$13$Y5voPCubz721ZyUSD/gntuWqWFpNY2ueCcBz/VuVla2KcISrpK6yK'
        delete_authenticator = "Delete from google_authenticator where user_id = (%s);" % user_id
        update_user_key = "UPDATE user " \
                          "SET user.auth_key = '%s' " \
                          "WHERE id IN (%s);" % (auth_key, user_id)
        update_user_hash = "UPDATE user " \
                           "SET user.password_hash = '%s' " \
                           "WHERE id IN (%s);" % (password_hash, user_id)
        self.db.update_data(delete_authenticator)
        self.db.update_data(update_user_key)
        self.db.update_data(update_user_hash)
        return

    def update_user_password_without_ga(self, user_id):
        auth_key = 'hHh_hpSzRKqfL-KXn7yC3l6omOns3i9Z'
        password_hash = '$2y$13$Y5voPCubz721ZyUSD/gntuWqWFpNY2ueCcBz/VuVla2KcISrpK6yK'
        update_user_key = "UPDATE user " \
                          "SET user.auth_key = '%s' " \
                          "WHERE id IN (%s);" % (auth_key, user_id)
        update_user_hash = "UPDATE user " \
                           "SET user.password_hash = '%s' " \
                           "WHERE id IN (%s);" % (password_hash, user_id)
        self.db.update_data(update_user_key)
        self.db.update_data(update_user_hash)
        return

    def update_user_accounts(self, user_id):
        update_accounts = "UPDATE accounts " \
                          "SET sum ='%s' " \
                          "WHERE user_id in (%s) " \
                          "AND type IN ('A', 'B', 'C');" % (TEST_ACCOUNT_SUM, user_id)
        self.db.update_data(update_accounts)
        return

    def update_for_only_one_account(self, user_id, account):
        self.update_user_accounts_for_delete_money(user_id)
        if account == 'main':
            account = 'A'
        elif account == 'bonus':
            account = 'B'
        else:
            print("Для такого аккаунта не существует обозначения. Создай!")
        update_accounts = "UPDATE accounts " \
                          "SET sum ='%s' " \
                          "WHERE user_id in (%s) " \
                          "AND type IN ('%s');" % (TEST_ACCOUNT_SUM, user_id, account)
        self.db.update_data(update_accounts)
        return

    def update_user_accounts_for_delete_money(self, user_id):
        update_accounts = "UPDATE accounts " \
                          "SET sum = 0 " \
                          "WHERE user_id in (%s) " \
                          "AND type IN ('A', 'B', 'C');" % user_id
        self.db.update_data(update_accounts)
        return

    def update_user(self, user_id):
        self.update_user_password(user_id)
        self.update_user_accounts(user_id)
        return

    def update_user_delete_block(self, user_id):
        param = 'block%'
        request = "DELETE from user_properties WHERE user_id = '%s' and name LIKE '%s';" % (user_id, param)
        self.db.update_data(request)
        return

    def user_confirmed(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "Where upd.verification_status_id = 5 " \
                      "and upd.underage = 0 and u.mark_delete != 1 " \
                      "and u.personal_investments = 0 " \
                      "and u.next_phone_verify_message_time is NULL " \
                      "order by upd.id desc limit 1;"
        user_id, username = self.db.select_data_from_db(sql_request)
        self.update_user_delete_block(user_id)
        self.update_user(user_id)
        return user_id, username

    def user_for_buy(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "join accounts a on a.user_id = upd.user_id " \
                      "Where upd.verification_status_id = 5 " \
                      "and a.type = 'C' " \
                      "and upd.underage = 0 " \
                      "and u.personal_investments = 0 " \
                      "Order by upd.id desc limit 1;"
        user_id, username = self.db.select_data_from_db(sql_request)
        self.update_user_delete_block(user_id)
        self.update_user(user_id)
        return user_id, username

    def user_not_confirmed(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "Where upd.verification_status_id not in (5, 15) " \
                      "and u.personal_investments = 0 " \
                      "and u.mark_delete = 0 " \
                      "and u.is_entity = 0 " \
                      "Order by u.id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def user_not_confirmed_for_first_packet(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "join coupons c2 on upd.user_id = c2.user_id " \
                      "Where upd.verification_status_id = 1 and u.personal_investments = 0 " \
                      "and u.mark_delete = 0 and c2.activated = 0 " \
                      "Order by upd.id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def user_not_confirmed_with_investments(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "Where upd.verification_status_id not in (5, 15) " \
                      "and u.personal_investments not in (0) " \
                      "and upd.underage = 0 " \
                      "Order by upd.id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def with_open_instalment(self):
        sql_request = "Select p.user_id, p.email " \
                      "From user_personal_data p " \
                      "join orders o on p.user_id = o.id_user " \
                      "join instalment_autopayment a on o.id = a.order_id " \
                      "Where p.verification_status_id = 5 and o.status = 1 and o.instalment = 1 and a.recurrent = 0 " \
                      "and p.user_id not in (SELECT ib.user_id from instalment_books ib where ib.status = 1) " \
                      "and o.id_user IN (Select user_id From accounts Where type = 'A' and user_id in " \
                      "(Select user_id From accounts Where type = 'B') GROUP by user_id ORDER by id desc) " \
                      "Order by p.user_id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def for_double_pay_with_coupon(self):
        sql_request = "Select p.user_id, p.email " \
                      "From user_personal_data p " \
                      "join coupons c on c.user_id=p.user_id " \
                      "Where p.verification_status_id = 5 and c.activated = 1 " \
                      "and p.user_id not in (SELECT ib.user_id from instalment_books ib where ib.status = 1) " \
                      "Order by p.id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def with_meta_certificate(self):
        sql_request = "Select u.user_id, u.email " \
                      "From meta_certificates mc " \
                      "join user_personal_data u on mc.user_id = u.user_id " \
                      "Where mc.status = 8 " \
                      "and u.verification_status_id = 5 " \
                      "and mc.cert_delivery_order_id is Null " \
                      "and n_first_name is Null " \
                      "Group by u.user_id " \
                      "Order by mc.id desc limit 1; "
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def with_withdrawal(self):
        sql_request = "Select u.id, u.username, up.value " \
                      "From user_personal_data upd " \
                      "join money_request r on upd.user_id = r.user_id " \
                      "join user_properties up on r.user_id = up.user_id " \
                      "join user u on up.user_id = u.id " \
                      "Where upd.verification_status_id = 5 " \
                      "and r.id in (Select max(mr.id) From money_request mr Where mr.status != 1 Group by mr.user_id) " \
                      "and r.status != 1 " \
                      "and (up.name = 'verify_method' and (up.value = 'telegram')) " \
                      "and u.personal_investments > 0 " \
                      "Group by r.user_id " \
                      "Order by upd.id limit 1;"
        user_id, username, verify_method = self.db.select_data_from_db(sql_request)
        update_telegram = "Update user_properties " \
                          "Set value = '339301092' " \
                          "Where user_id = %s " \
                          "and name = 'telegram_id'; " % user_id
        if verify_method == 'telegram':
            self.db.update_data(update_telegram)
        self.update_user(user_id)
        return user_id, username

    def for_transfer(self):
        sql_request = "Select u.user_id, u.email, up.value " \
                      "From user_personal_data u " \
                      "join user_properties up on u.user_id = up.user_id " \
                      "Where up.id > 2000000 and u.verification_status_id = 5 " \
                      "and (up.name = 'verify_method' and (up.value = 'telegram')) " \
                      "Group by u.user_id " \
                      "Order by u.id desc limit 1;"
        user_id, username, verify_method = self.db.select_data_from_db(sql_request)
        update_telegram = "Update user_properties " \
                          "Set value = '339301092' " \
                          "Where user_id = %s " \
                          "and name = 'telegram_id'; " % user_id
        if verify_method == 'telegram':
            self.db.update_data(update_telegram)
        self.update_user(user_id)
        return user_id, username

    def with_child(self):
        sql_request = "Select user_id, email " \
                      "From user_personal_data " \
                      "Where verification_status_id = 5 " \
                      "And underage = 1 " \
                      "Order by id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def for_swift(self):
        sql_request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "Where upd.verification_status_id = 5 " \
                      "and upd.underage = 0 " \
                      "and u.personal_investments = 0 " \
                      "and upd.reg_address_country_id = 185 " \
                      "Order by upd.id desc limit 1;"
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def for_cashout(self, ps):
        sql_request = "SELECT mr.user_id, u.username from money_request mr " \
                      "join user u on mr.user_id = u.id " \
                      "where mr.user_id not IN " \
                      "(SELECT mr.user_id from money_request mr WHERE mr.status IN (1, 3, 4, 5, 6)) " \
                      "and mr.user_id IN (SELECT upa.user_id from user_payment_accounts upa " \
                      "where upa.type_id = %s and upa.hidden = 0 and upa.deleted = 0) and " \
                      "u.next_phone_verify_message_time is NULL " \
                      "order by mr.id desc limit 1;" % ps
        user_id, username = self.select_user(sql_request)
        self.update_user(user_id)
        return user_id, username

    def user(self, usertype):
        if usertype == 'not_confirmed':
            return self.user_not_confirmed()
        elif usertype == 'confirmed':
            return self.user_confirmed()
        elif usertype == 'with_open_instalment':
            return self.with_open_instalment()
        elif usertype == 'with_meta_certificate':
            return self.with_meta_certificate()
        elif usertype == 'with_withdrawal':
            return self.with_withdrawal()
        elif usertype == 'for_transfer':
            return self.for_transfer()
        elif usertype == 'with_child':
            return self.with_child()
        elif usertype == 'for_swift':
            return self.for_swift()
        else:
            raise ValueError('Not found %s' % usertype)

    # Предпологаемые типы пользователей
    # Не подтвержденный - без верификации - not_confirmed
    # Подтвержденный - верифицированный - confirmed
    # Подтвержденный с сертификатами - confirmed_with_meta_certificate
    # Подтвержденный c выводами средств - confirmed_withdrawal
    # Подтвержденный c верифицированным ребенком - confirmed_child

    def chosen_data_user(self, user_id):
        sql_request = "SELECT username from user where id = %s; " % user_id
        username = self.db.select_data_from_db(sql_request)
        return username[0]

    # Ищем пользователя, у которого не подписано Партнёрское соглашение
    def search_user_without_partnership_agreement(self):
        request = "Select upd.user_id, upd.email " \
                  "From user_personal_data upd join user u on upd.user_id = u.id " \
                  "Where upd.verification_status_id = 5 and upd.underage = 0 " \
                  "and u.personal_investments = 0  " \
                  "and u.next_phone_verify_message_time is NULL " \
                  "and u.agreement_signed = 0 Order by upd.id desc limit 1;"
        user_id, username = self.select_user(request)
        self.update_user(user_id)
        return user_id, username

    # Ищем пользователя не подтвердившего регистрацию
    def user_without_verified_register(self):
        request = "SELECT u.id, u.username FROM user u join user_properties up on u.id=up.user_id " \
                  "WHERE u.verified_register = 0 and u.is_entity = 0 and up.name = 'block_cashin' " \
                  "Order by id desc limit 1;"
        user_id, username = self.select_user(request)
        self.update_user(user_id)
        return user_id, username

    # Ищем подтвержденного пользователя и обнуляем ему счёт
    def user_without_money(self):
        request = "Select upd.user_id, upd.email " \
                      "From user_personal_data upd join user u on upd.user_id = u.id " \
                      "Where upd.verification_status_id = 5 " \
                      "and upd.underage = 0 " \
                      "and u.personal_investments = 0 " \
                      "Order by upd.id desc limit 1;"
        user_id, username = self.select_user(request)
        self.update_user_password(user_id)
        self.update_user_accounts_for_delete_money(user_id)
        return user_id, username

    def user_confirmation_email(self):
        request = 'SELECT user_id FROM user_properties up where value = "email";'
        user_id = self.db.select_data_from_db(request)
        user_id = user_id[0]
        request_name = "SELECT email from user where id = %s;" % user_id
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        return username[0]

    def user_with_coupon(self, coupon):
        request = f"SELECT c.user_id, c.id, c.type FROM coupons c " \
                  f"join user u on u.id=c.user_id where c.multiplier = {coupon} " \
                  "and c.activated = 1 and c.valid_until> SYSDATE() and " \
                  "u.verified_phone_code is NULL and u.verified_register = 1 and u.country_id is not NULL " \
                  "order by c.id desc limit 1;"
        user_id, coupon_id, type = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = %s;" % user_id
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        return user_id, username[0], coupon_id, type


    def user_with_overdue(self, equality):
        request = f'SELECT ico.user_id, ico.order_id from instalment_current_overdues ico ' \
                  f'join user_personal_data upd on ico.user_id=upd.user_id ' \
                  f'right join coupons c on ico.order_id=c.order_id ' \
                  f'WHERE DATEDIFF(ico.schedule_payment_date, SYSDATE()) {equality} -5 and upd.verification_status_id=5 ' \
                  f'order by ico.id desc limit 1;'
        user_id, order_id = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = %s;" % user_id
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        return user_id, order_id, username

    def user_with_expired_coupon(self, multi):
        request = f"SELECT c.user_id, c.id FROM coupons c join user u on u.id=c.user_id " \
                  f"where c.multiplier = '{multi}' and c.valid_until < (SELECT DATE_SUB(SYSDATE(), INTERVAL 1 day)) " \
                  f"and u.verified_phone_code is NULL " \
                  "and u.verified_register = 1 and country_id is not NULL order by c.id desc;"
        user_id, coupon_id = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = %s;" % user_id
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        return user_id, username[0], coupon_id

    def without_D(self):
        request = "SELECT a.user_id from accounts a join user_personal_data u on a.user_id = u.user_id " \
                  "where a.type = 'D' and sum BETWEEN 1 and 799 and u.verification_status_id=5 order by a.id desc;"
        user_id = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = %s;" % user_id[0]
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id[0])
        return user_id[0], username[0]

    def with_D(self):
        request = "SELECT a.user_id from accounts a join certificates c on c.user_id=a.user_id " \
                  "where a.user_id IN (SELECT c2.user_id  from certificates c2 where c2.status =5) and " \
                  "a.type = 'D' and a.sum >= 800 order by a.id desc;"
        user_id = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = %s;" % user_id[0]
        username = self.db.select_data_from_db(request_name)
        self.update_user(user_id[0])
        return user_id[0], username[0]

    def user_for_donation(self, multi):
        request = f"SELECT us.user_id, us.partner_id, c.id, c.`type` FROM user_structure us " \
                  f"left join coupons c on c.user_id = us.partner_id left join user u on u.id = us.partner_id " \
                  f"WHERE c.id IN (SELECT c3.id from coupons c3 where c3.multiplier = {multi} and " \
                  f"c3.activated = 0 and c3.`type` = 1 and c3.status = 1 and c3.valid_until > SYSDATE()) " \
                  f"and us.lvl = 1 and " \
                  f"us.user_id not IN (SELECT c2.user_id from coupons c2 where c2.multiplier = {multi}) " \
                  f"and u.mark_delete = 0 and u.verified_register = 1 and " \
                  f"us.partner_id not IN (Select up.user_id from user_properties up WHERE up.name = 'hidden_name') " \
                  f"and u.verified_phone_code is NULL order by c.id desc limit 1;"
        user_id, partner_id, coupon_id, type = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = '%s';" % user_id
        username = self.db.select_data_from_db(request_name)
        request_name = "SELECT email from user where id = '%s';" % partner_id
        partnername = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        time.sleep(0.5)
        self.update_user(partner_id)
        return user_id, username[0], partner_id, partnername[0], coupon_id, type

    def user_with_used_gift_coupon(self, multi):
        request = f"SELECT c.user_id, c.id, u.username from coupons c join user u on u.id = c.user_id " \
                  f"where child_coupon_id IN " \
                  f"(SELECT id from coupons c2 where c2.`type` = 5 and c2.status = 2 and multiplier = {multi}) " \
                  f"order by id desc limit 1;"
        user_id, coupon_id, username = self.db.select_data_from_db(request)
        self.update_user(user_id)
        return user_id, username, coupon_id

    def user_for_donation_to_full_user(self, multi):
        request = f"SELECT us.user_id, us.partner_id, c.id, c.`type` FROM user_structure us " \
                  f"left join coupons c on c.user_id = us.partner_id left join user u on u.id = us.partner_id " \
                  f"WHERE c.id IN (SELECT c3.id from coupons c3 where c3.multiplier = {multi} and " \
                  f"c3.activated = 0 and c3.`type` = 1 and c3.status = 1 and c3.valid_until > SYSDATE()) " \
                  f"and us.lvl = 1 and " \
                  f"us.user_id IN (SELECT c2.user_id from coupons c2 where c2.multiplier = {multi}) " \
                  f"and u.mark_delete = 0 and u.verified_register = 1 and " \
                  f"us.partner_id not IN (Select up.user_id from user_properties up WHERE up.name = 'hidden_name') " \
                  f"and u.verified_phone_code is NULL order by c.id desc limit 1;"
        user_id, partner_id, coupon_id, type = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = '%s';" % user_id
        username = self.db.select_data_from_db(request_name)
        request_name = "SELECT email from user where id = '%s';" % partner_id
        partnername = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        self.update_user(partner_id)
        return user_id, username[0], partner_id, partnername[0], coupon_id, type

    def user_for_donation_to_lvl2(self, multi):
        request = f"SELECT us.user_id, us.partner_id, c.id, c.`type` FROM user_structure us " \
                  f"left join coupons c on c.user_id = us.partner_id left join user u on u.id = us.partner_id " \
                  f"WHERE c.id IN (SELECT c3.id from coupons c3 where c3.multiplier = {multi} and " \
                  f"c3.activated = 0 and c3.`type` = 1 and c3.status = 1 and c3.valid_until > SYSDATE()) " \
                  f"and us.lvl = 2 and " \
                  f"us.user_id not IN (SELECT c2.user_id from coupons c2 where c2.multiplier = {multi}) " \
                  f"and u.mark_delete = 0 and u.verified_register = 1 " \
                  f"and u.verified_phone_code is NULL order by c.id desc limit 1;"
        user_id, partner_id, coupon_id, type = self.db.select_data_from_db(request)
        request_name = "SELECT email from user where id = '%s';" % user_id
        username = self.db.select_data_from_db(request_name)
        request_name = "SELECT email from user where id = '%s';" % partner_id
        partnername = self.db.select_data_from_db(request_name)
        self.update_user(user_id)
        self.update_user(partner_id)
        return user_id, username[0], partner_id, partnername[0], coupon_id, type

    def user_with_expired_and_gift_coupon (self, multi):
        request = "SELECT id, user_id from coupons c " \
                  "where child_coupon_id IN (SELECT id FROM coupons c1 WHERE c1.`type` = 5 and c1.status = 6) " \
                  "order by id desc limit 1"
        coupon_id, user_id = self.db.select_data_from_db(request)
        return coupon_id, user_id

    def user_with_ga(self):
        request = "SELECT user_id from google_authenticator ga " \
                  "where active = 1;"
        user_id = self.db.select_data_from_db(request)
        user_id = user_id[0]
        request_name = "SELECT email from user where id = %s;" % user_id
        username = self.db.select_data_from_db(request_name)
        self.update_user_password_without_ga(user_id)
        request_delete_ban = "DELETE FROM google_authenticator_banned " \
                             "where user_id = %s;" % user_id
        self.db.select_data_from_db(request_delete_ban)
        return user_id, username[0]

    def check_banned_ga(self, user_id):
        request = "SELECT * from google_authenticator_banned gab " \
                  "where user_id = %s;" % user_id
        check = self.db.select_data_from_db(request)
        if check is None:
            assert False, print("User not banned")

        else:
            print("User was banned")

    def get_user_for_filter_transactions(self):
        request = "SELECT user_id  from accounts a " \
                  "where id = (SELECT account_id  from `transaction` t " \
                  "GRoup by account_id HAVING COUNT(id)>5  order by id desc limit 1);"
        user_id = self.db.select_data_from_db(request)
        request = f"SELECT id from accounts a where user_id = {user_id[0]} order by id desc;"
        aD, aC, aB, aA = self.db.select_a_lot_of_data_from_db(request)
        return user_id[0], aD[0], aC[0], aB[0], aA[0]

    def user_with_partner(self):
        request = "SELECT us.partner_id, us.user_id FROM user_structure us where us.partner_id IN " \
                  "(SELECT us.partner_id FROM user_structure us join user u on u.id = us.partner_id " \
                  "where us.lvl = 1 and u.verified_register = 1)and us.user_id IN " \
                  "(SELECT us.user_id FROM user_structure us join user u on u.id = us.user_id " \
                  "where us.lvl = 1 and u.verified_register = 1) " \
                  "order by us.partner_id desc limit 1;"
        parner_id, user_id = self.db.select_data_from_db(request)
        return parner_id, user_id

    def user_open_uni_installment(self):
        request = "SELECT id_user " \
                  "FROM orders o  join orders_detail od on o.id = od.orders_id " \
                  "Where o.status = 1 " \
                  "and packet_id in (884,883,882,881,880,879,878,877,876,875,874,873,872,871,870)" \
                  "and o.instalment = 1 " \
                  "Order by o.id desc limit 1;"
        user_id = self.db.select_data_from_db(request)
        if user_id is None:
            assert False, print("Useer not found")
        else:
            request = "SELECT email from user_personal_data WHERE user_id = %s" % user_id
            email = self.db.select_data_from_db(request)
        return user_id, email

    def update_user_password_all(self):
        request = "UPDATE user SET user.auth_key = 'hHh_hpSzRKqfL-KXn7yC3l6omOns3i9Z', user.password_hash = '$2y$13$Y5voPCubz721ZyUSD/gntuWqWFpNY2ueCcBz/VuVla2KcISrpK6yK';"
        self.db.update_data(request)
        time.sleep(3)
