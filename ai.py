import os
import traceback
import logging

# from groq import Groq
from dotenv import load_dotenv

from prompts import forming_query, ai_to_human
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

class AI:

    def __init__(self, table_def):
        try:
            load_dotenv()
            self.logger = logging.getLogger('askdb.ai')

            self.client = ChatGroq(api_key=os.getenv('GROQ_API_KEY'), model=os.getenv('MODEL', 'openai/gpt-oss-120b'), temperature=0.2)

            self.sql_ai_message = [
                SystemMessage(content=forming_query.format(desc= table_def))
            ]

            self.response_ai_message = [
                SystemMessage(content=ai_to_human)
            ]

        except Exception as e:
            self.logger.error(f'Error occurred - {e} : {traceback.format_exc()}')

    def form_sql_query(self, question):

        try:

            self.sql_ai_message.append(HumanMessage(content=question))

            completion = self.client.invoke(input = self.sql_ai_message)
            response = completion.content

            self.sql_ai_message.append(AIMessage(content=response))
            self.logger.info(f'AI SQL query >> {response}')

            return response

        except Exception as e:
            self.logger.error(f'Error occurred while forming the query with help of AI - {e} : {traceback.format_exc()}')
            return None

    def ai_response(self, data, question):

        try:

            self.response_ai_message.append(HumanMessage(content= f"Question : {question}, Data Set : {data}"))

            completion = self.client.invoke(input = self.response_ai_message)
            response = completion.content

            self.response_ai_message.append(AIMessage(content=response))
            self.logger.info(f'AI response >> {response}')

            return response

        except Exception as e:
            self.logger.error(f'Error occurred while responding to user with help of AI - {e} : {traceback.format_exc()}')
            return None
