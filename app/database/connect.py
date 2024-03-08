import sqlite3

connect = sqlite3.connect('cryolife_database.db')
cursor = connect.cursor()

# Создание 1 таблицы в БД (USERS)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    chat_id INTEGER NOT NULL)
''')
connect.commit()

# Создание 2 таблицы в БД(PRICE_LIST)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS price_list (
    price_work TEXT(1000),
    liquid_nitrogen TEXT(1000),
    dry_ice TEXT(1000),
    thermos_rental TEXT(1000))
''')
connect.commit()
cursor.close()
