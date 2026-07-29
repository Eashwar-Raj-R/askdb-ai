import os

from database import Database
from ai import form_query, ai_response

class Uber():
# def main():
    def __init__(self):
        self.db = Database()
        self.table_def = self.db.desc_tables()

        with open('table_definition.txt', 'w') as t:
            t.write(str(self.table_def))

    def ai_chat(self):
        print('AI> Hey, How can i help you today?')

        user_question = input('>>>').lower()

        while True:
            if user_question in ('exit', 'close'):
                break

            if not user_question:
                print('Invalid input')
                user_question = input('>>>').lower()

            ai_query = form_query(self.table_def, user_question)
            # print(ai_query)
            if 'NO_QUERY_POSSIBLE' not in ai_query:
                data = self.db.run_query(ai_query)

                response = ai_response(data, user_question)
                print(f'AI> {response}')
            else:
                print('invalid question')

            user_question = input('>>>').lower()

if __name__ == "__main__":
    uber = Uber()
    uber.ai_chat()