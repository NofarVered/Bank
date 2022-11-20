import pymysql
import json
from constants import *

CONNECTOR = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="bank_manager",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def create_database():
    try:
        with CONNECTOR.cursor() as cursor:
            cursor.execute(drop_db)
            cursor.execute(create_db)
            CONNECTOR.commit()
    except Exception as e:
        print(e)


def create_all_tables():
    try:
        with CONNECTOR.cursor() as cursor:
            cursor.execute(use_db)
            cursor.execute(create_users_table)
            cursor.execute(create_categories_table)
            cursor.execute(create_transactions_table)
            CONNECTOR.commit()
    except Exception as e:
        print(e)


def load_data():
    data = json_processor()
    users_records = data['Users']
    categories_records = data['Categories']
    transactions_records = data['Transactions']
    try:
        with CONNECTOR.cursor() as cursor:
            for user in users_records:
                cursor.execute(
                    insert_users, [user['user_id'], user['balance']])
            for category in categories_records:
                cursor.execute(insert_categories, [category['category_name']])
            for transaction in transactions_records:
                cursor.execute(insert_transactions, [transaction['id'],
                               transaction['amount'], transaction['vendor'], transaction['category_name'], transaction['user_id']])
            CONNECTOR.commit()
    except Exception as e:
        print(e)


def json_processor():
    data_file = open('./mock_data.json')
    data = json.load(data_file)
    data_file.close()
    return data


# python create_db_script.py
if __name__ == "__main__":
    print("--- START creating DB Bank_manager")
    create_database()
    print("--- START creating tables")
    create_all_tables()
    print("--- DATABSE IS READY")
    load_data()
    print("--- DONE LOAD DATA")
