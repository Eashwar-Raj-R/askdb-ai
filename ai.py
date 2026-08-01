import os
import traceback
import logging

from groq import Groq
from dotenv import load_dotenv
from prompts import forming_query, ai_to_human

class AI:

    def __init__(self, table_def):
        try:
            load_dotenv()
            self.logger = logging.getLogger('askdb.ai')

            self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))

            self.sql_ai_message = [{
                    "role": "system",
                    "content": forming_query.format(desc= table_def)
                }]

            self.response_ai_message = [{
                    'role' : 'system',
                    'content' : ai_to_human
                }]

        except Exception as e:
            self.logger.error(f'Error occurred - {e} : {traceback.format_exc()}')

    def form_sql_query(self, question):

        try:
            self.sql_ai_message.append(
                {
                    "role": "user",
                    "content" : question
                })

            completion = self.client.chat.completions.create(
                model = os.getenv('MODEL', 'openai/gpt-oss-120b'),
                messages = self.sql_ai_message,
                temperature = 0.2,
                max_completion_tokens = 2048,
            )

            response = completion.choices[0].message.content

            self.sql_ai_message.append({
                'role' : 'assistant',
                'content' : response
            })

            self.logger.info(f'AI SQL query >> {response}')

            return response

        except Exception as e:
            self.logger.error(f'Error occurred while forming the query with help of AI - {e} : {traceback.format_exc()}')
            return None

    def ai_response(self, data, question):

        try:
            self.response_ai_message.append(
                {
                    "role": "user",
                    "content" : f"Question : {question}, Data Set : {data}"
                })

            completion = self.client.chat.completions.create(
                model = os.getenv('MODEL', 'openai/gpt-oss-120b'),
                messages=self.response_ai_message,
                temperature=0.2,
                max_completion_tokens=2048,
            )

            response = completion.choices[0].message.content

            self.response_ai_message.append({
                'role' : 'assistant',
                'content' : response
            })

            self.logger.info(f'AI response >> {response}')

            return response

        except Exception as e:
            self.logger.error(f'Error occurred while responding to user with help of AI - {e} : {traceback.format_exc()}')
            return None
