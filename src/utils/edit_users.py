
add_user = ("INSERT INTO user "
               "(nom, prenom, email) "
               "VALUES (%s, %s, %s)")


select_user = ("SELECT * FROM user WHERE id = %s")

