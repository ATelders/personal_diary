
request_add_user = ("INSERT INTO user "
               "(nom, prenom, email) "
               "VALUES (%s, %s, %s)")

request_select_user = ("SELECT * FROM user WHERE id = %s")

request_add_entry = ("INSERT INTO diary_entry "
               "(user_id, date, content, emotion) "
               "VALUES (%s, %s, %s, %s)")