GET_TRANSACTION_BY_ID = """SELECT * FROM Transactions WHERE id = %s"""

GET_USER_BY_ID = """SELECT * FROM Users WHERE user_id = %s """

GET_CATEGORY_BY_NAME = """SELECT * FROM Categories WHERE category_name = %s """

INSERT_TRANSACTION = """INSERT INTO Transactions VALUES(%s, %s, %s, %s, %s)"""

DELETE_TRANSACTION_BY_ID = """DELETE FROM Transactions WHERE id = %s"""

GET_ALL_TRANSACTIONS_BY_USER_ID = """SELECT * FROM Transactions WHERE user_id = %s"""

GET_EXPENSES_BY_CATEGORIES = """SELECT category_name, SUM(amount) as total
                                FROM Transactions 
                                WHERE user_id = %s 
                                GROUP BY category"""

UPDATE_BALANCE_OF_USER = """UPDATE Users
                            SET balance = %s
                            WHERE user_id = %s
                         """
