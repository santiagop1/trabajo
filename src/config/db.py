import mariadb

config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '1',
    'database': 'flask_mvc'
}

DB = mariadb.connect(**config)
DB.autocommit = True 