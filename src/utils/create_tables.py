import sys
import mysql.connector
from mysql.connector import errorcode


sys.path.insert(0, '/home/apprenant/simplon_projects/personal_diary/')
from src.config import USER, PASSWORD


# MySQL Connector
DB_NAME = 'personal_diary'
db_connection = mysql.connector.connect(user=USER, database=DB_NAME, password=PASSWORD)
cursor = db_connection.cursor()


# TABLES dictionnary

TABLES = {}

TABLES['client'] = (
    '''
    CREATE TABLE client (
        id smallint unsigned NOT NULL AUTO_INCREMENT,
        nom VARCHAR(100),
        prenom VARCHAR(100) NOT NULL,
        email VARCHAR(60) NOT NULL,
        PRIMARY KEY (id)
    )   ENGINE=InnoDB
    '''
)

TABLES['diary_entry'] = (
    '''
    CREATE TABLE diary_entry (
        id smallint unsigned NOT NULL AUTO_INCREMENT,
        client_id smallint unsigned NOT NULL,
        date DATETIME,
        content VARCHAR(500) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY (client_id)
            REFERENCES client (id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )   ENGINE=InnoDB
    '''
)

TABLES['emotion'] = (
    '''
    CREATE TABLE emotion (
        id smallint unsigned NOT NULL AUTO_INCREMENT,
        diary_entry_id smallint unsigned NOT NULL,
        name VARCHAR(60) NOT NULL,
        probability DECIMAL(3,3),
        PRIMARY KEY (id),
        FOREIGN KEY (diary_entry_id)
            REFERENCES diary_entry (id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    )   ENGINE=InnoDB
    '''
)



# Create database function

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


# Create database if not exists

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db_connection.database = DB_NAME
    else:
        print(err)
        exit(1)


# Create tables of the TABLES dictionnary

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
db_connection.close()
