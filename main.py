import os
import json
import logging
import traceback

from datetime import datetime

from database import Database
from ai import AI

class AskDb:

    def __init__(self):

        #logging
        os.makedirs("logs", exist_ok=True)
        filename = f'logs/app_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

        logging.basicConfig(
            filename=filename,
            filemode='a',
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        self.logger = logging.getLogger(__name__)
        self.logger.info('Starting application v1')

        self.db = Database()
        self.table_def = self.db.desc_tables()

        self.ai = AI(self.table_def)

        os.makedirs("./metadata", exist_ok=True)
        with open(r'./metadata/table_definition.json', 'w') as handler:
            json.dump(self.table_def, handler, indent= 4)

        self.logger.info('Table definition written to JSON file')

    def ai_chat(self):
        try:
            print('AI> Hey, How can i help you today?')

            user_question = input('>>>').lower()
            self.logger.info(f'Human>>> {user_question}')

            query_history = []

            while True:
                if user_question in ('exit', 'close'):
                    print('Good Bye')

                    self.logger.info(f'User Exited')
                    self.db.close_connection()

                    with open('./metadata/query_history.json', 'w') as handler:
                        json.dump(query_history, handler, indent=4)

                    break

                if not user_question:
                    print('Invalid input')
                    user_question = input('>>>').lower()

                ai_sql_query = self.ai.form_sql_query(user_question)

                query_history.append({
                    'datetime' : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'human' : user_question,
                    'generated_sql' : ai_sql_query
                })

                if ai_sql_query and 'NO_QUERY_POSSIBLE' not in ai_sql_query:
                    data = self.db.run_query(ai_sql_query)

                    if data:
                        response = self.ai.ai_response(data, user_question)
                        print(f'AI> {response}')
                    else:
                        print('Something went wrong running that query.')
                else:
                    print('invalid question')

                user_question = input('>>>').lower()
                self.logger.info(f'Human>>> {user_question}')

        except Exception as e:
            self.logger.error(f'unexpected error occurred : {e} - {traceback.format_exc()}')

if __name__ == "__main__":
    askdb = AskDb()
    askdb.ai_chat()
