import mysql.connector
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

class Database():
# Establish connection

    # def db_connect(self):
    #     db = mysql.connector.connect(
    #         host=os.getenv('HOSTNAME'),
    #         user=os.getenv('USER'),
    #         password=os.getenv('PASSWORD'),
    #         database=os.getenv('DATABASE'),
    #     )
    #     # print('Database connection opened')
    #     return db

    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host=os.getenv('HOSTNAME'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                database=os.getenv('DATABASE'),
            )

            print('Database connection opened')

        except Exception as e:
            print(f'Error occured while connecting to database : {e} - {traceback.format_exc()}')

    def get_tables(self):
        try:

            tables = []

            # db = self.db_connect()
            cursor = self.db.cursor()
            cursor.execute('show tables')
            # print('Fetching tables names from database')

            for table in cursor.fetchall():
                tables.append(table[0])

            return tables

        except Exception as e:
            print(f'Error occured while fetching tables from database : {e} - {traceback.format_exc()}')

    def desc_tables(self):
        try:

            tables = self.get_tables()
            desc = {}

            # db = self.db_connect()
            cursor = self.db.cursor()

            for table in tables:
                # print(table)
                cursor.execute(f'describe {table}')
                # res = cursor.fetchall()
                # print(res)
                desc[table] = cursor.fetchall()

            return desc

        except Exception as e:
            print(f'Error occured while fetching table description from database : {e} - {traceback.format_exc()}')

    def run_query(self, query):
        try:
            # db = self.db_connect()
            cursor = self.db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()

            return result

        except Exception as e:
            print(f'Error occured while executing the query in database : {e} - {traceback.format_exc()} | query - {query}')
