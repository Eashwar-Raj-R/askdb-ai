from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv('GROQ_API_KEY'))

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def form_query(desc, question):

    messages = [{
                "role": "system",
                "content": f"""You are a MySQL query generator. Convert the user's natural language question into ONE valid, read-only MySQL query, using only the schema provided.

                    SCHEMA:{desc}
                    USER:{question}
                    RULES:
                    - Output ONLY the raw SQL query. No markdown, no explanations, no extra text.
                    - Only SELECT statements. Never INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, CREATE, or multiple statements.
                    - Use only the exact table/column names from the given schema. Never invent one.
                    - If the question can't be answered with the schema, output exactly: NO_QUERY_POSSIBLE
                    - Use JOINs when the question spans multiple tables.
                    - Add LIMIT 100 by default, unless the question asks for a count/aggregate.
                    - Use COUNT/SUM/AVG/GROUP BY for summary-type questions.
                    - If ambiguous, pick the most reasonable business interpretation — don't ask for clarification."""
            }]

    completion = client.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=messages,
        temperature=0.2,
        max_completion_tokens=2048,
    )

    messages.append({
        'role' : 'assistant',
        'content' : completion.choices[0].message.content
    })

    # print(messages)
    return completion.choices[0].message.content

def ai_response(data, question):

    messages = [
        {
            'role' : 'system',
            'content' : f"""You are a helpful assistant that answers a client's question using only the SQL query result data provided.
                        SQL RESULT SET : {data}
                        QUESTION : {question}
                        RULES:
                        - Answer only using the given data. Never assume or add information not present in it.
                        - Be clear, conversational, and concise — no SQL, technical jargon, or column names unless the user asks for them.
                        - If the data is empty or has no rows, say no matching results were found.
                        - If the data only partially answers the question, answer what you can and note what's missing.
                        - Do not mention that the data came from a database or SQL query."""
        }
    ]

    completion = client.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=messages,
        temperature=0.2,
        max_completion_tokens=2048,
    )

    messages.append({
        'role' : 'assistant',
        'content' : completion.choices[0].message.content
    })

    # print(messages)
    return completion.choices[0].message.content

