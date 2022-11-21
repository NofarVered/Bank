import pymysql
from .dal import Dal
from typing import List, Dict
from ..models import *
from utils import *


class MysqlDal(Dal):
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bank_manager",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def _execute_insert_query(self, sql_query: str, params: List):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            self.connection.commit()

    def _execute_select_all_query(self, sql_query: str, params: List):
        with self.connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            result = [obj for obj in cursor.fetchall()]
            return result

    def _execute_select_one_query(self, sql_query: str, params: List = None):
        with self.connection.cursor() as cursor:
            cursor.execute(
                sql_query, params) if params else cursor.execute(sql_query)
            result = cursor.fetchone()
            return result

    def _is_transaction_exist(self, id: int) -> bool:
        result = self._execute_select_one_query(GET_TRANSACTION_BY_ID, [id])
        return len(result) != 0

    def _is_user_exist(self, user_id: int) -> bool:
        result = self._execute_select_one_query(GET_USER_BY_ID, [user_id])
        return len(result) != 0

    def _is_category_exist(self, category_name: str) -> bool:
        result = self._execute_select_one_query(
            GET_CATEGORY_BY_NAME, [category_name])
        return len(result) != 0

    def _update_user_balance(self, user_id: int, amount: int) -> None:
        user_record = self._execute_select_one_query(GET_USER_BY_ID, [user_id])
        user = User(**user_record)
        new_balance = user.balance + amount
        self._execute_insert_query(UPDATE_BALANCE_OF_USER, [
                                   new_balance, user_id])

    def add_transaction(self, transaction: Transaction) -> None:
        self._execute_insert_query(INSERT_TRANSACTION, [
                                   transaction.id, transaction.amount, transaction.vendor, transaction.category_name, transaction.user_id])
        self._update_user_balance(transaction.user_id, transaction.amount)

    def delete_transaction(self, transaction: Transaction) -> None:
        self._execute_insert_query(DELETE_TRANSACTION_BY_ID, [transaction.id])
        self._update_user_balance(transaction.user_id, -1 * transaction.amount)

    def get_all_transactions_by_user_id(self, user_id: int) -> List[Transaction]:
        result = self._execute_select_all_query(GET_TRANSACTION_BY_ID, user_id)
        return [Transaction(**record) for record in result]

    def get_all_expenses_by_category(self, user_id):
        result = self._execute_select_all_query(
            GET_USER_EXPENSES_BY_CATEGORIES, user_id)
        return result

    def get_user_balance(self, user_id: int) -> float:
        user_record = self._execute_select_one_query(GET_USER_BY_ID, [user_id])
        user = User(**user_record)
        return user.balance


db_manager: Dal = MysqlDal()
