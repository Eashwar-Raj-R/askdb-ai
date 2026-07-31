import mysql.connector
import os
import traceback
import logging

from dotenv import load_dotenv

class Database:

    def __init__(self):

        try:

            load_dotenv()
            self.logger = logging.getLogger('askdb.database')

            self.db = mysql.connector.connect(
                host=os.getenv('HOSTNAME'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                database=os.getenv('DATABASE'),
            )

            self.logger.info('database connection opened successfully')

        except Exception as e:
            self.logger.error(f'Error occurred while connecting to database : {e} - {traceback.format_exc()}')

    def close_connection(self):
        try:
            self.db.close()
            self.logger.info('Closing database connection')

        except Exception as e:
            self.logger.error(f'Error occurred while closing database connection : {e} - {traceback.format_exc()}')

    def get_tables(self):
        try:

            tables = []

            cursor = self.db.cursor()
            cursor.execute('show tables')

            self.logger.info('Fetching tables names from database')

            for table in cursor.fetchall():
                tables.append(table[0])

            return tables

        except Exception as e:
            self.logger.error(f'Error occurred while fetching tables from database : {e} - {traceback.format_exc()}')

    def desc_tables(self):
        try:

            tables = self.get_tables()
            desc = {}

            cursor = self.db.cursor(dictionary=True)

            for table in tables:
                self.logger.info(f'Getting the table schema : {table}')
                cursor.execute(f'describe {table}')
                desc[table] = cursor.fetchall()

            return desc

        except Exception as e:
            self.logger.error(f'Error occurred while fetching table description from database : {e} - {traceback.format_exc()}')

    def run_query(self, query):
        try:
            cursor = self.db.cursor(dictionary=True)

            forbidden_keywords = ['insert', 'update', 'delete', 'truncate', 'drop', 'merge', 'create', 'alter']

            if not any(keyword in query.lower() for keyword in forbidden_keywords):

                self.logger.info(f'Executing query formed by AI: {query}')

                cursor.execute(query)
                result = cursor.fetchall()

                return result
            else:
                print('DML commands are not allowed')
                return None

        except Exception as e:
            self.logger.error(f'Error occurred while executing the query in database : {e} - {traceback.format_exc()} | query - {query}')
