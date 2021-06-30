
request_add_user = ("INSERT INTO user "
               "(name, first_name, email) "
               "VALUES (%s, %s, %s)")

request_select_user = ("SELECT * FROM user WHERE id = %s")

request_add_entry = ("INSERT INTO diary_entry "
               "(user_id, date, content, emotion) "
               "VALUES (%s, %s, %s, %s)")

request_entries_from_user = ("SELECT * FROM diary_entry WHERE user_id = %s")

request_entries_from_user_and_date = ("SELECT * FROM diary_entry WHERE user_id = %s AND date = %s")

request_delete_user = ("DELETE FROM user WHERE id = %s")

request_display_all_users = ("SELECT * FROM user")

request_update_user = ("UPDATE user SET name = %s, first_name = %s, email = %s WHERE id = %s")