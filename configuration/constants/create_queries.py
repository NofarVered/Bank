drop_db = """
            DROP DATABASE IF EXISTS Bank_manager;
            """


create_db = """
            CREATE DATABASE IF NOT EXISTS Bank_manager;
            """

use_db = """
        use Bank_manager;
        """

create_users_table = """
            CREATE TABLE IF NOT EXISTS users(
                user_id INT NOT NULL PRIMARY KEY,
                balance FLOAT
                );
            """

create_categories_table = """
            CREATE TABLE IF NOT EXISTS categories(
                category_name VARCHAR(255) NOT NULL PRIMARY KEY
                );
            """

create_transactions_table = """
            CREATE TABLE IF NOT EXISTS transactions(
                id INT NOT NULL PRIMARY KEY,
                amount FLOAT,
                vendor VARCHAR(255),
                category_name VARCHAR(255),
                user_id INT,
                FOREIGN KEY(category_name) REFERENCES categories(category_name),
                FOREIGN KEY(user_id) REFERENCES users(user_id)
                );
            """
