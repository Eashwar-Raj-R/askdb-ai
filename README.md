# AskDB AI

AskDB AI is a Text-to-SQL application built with Python, MySQL, and Groq. It allows users to query a MySQL database using natural language. The application generates SQL queries from user questions, executes them against the database, and returns the results in a conversational format.

## Features

- Convert natural language into SQL queries
- Execute read-only SQL queries on a MySQL database
- Generate human-readable responses using an LLM
- Automatically read the database schema
- Logging for debugging and troubleshooting
- Modular object-oriented architecture
- Configuration using environment variables

## Tech Stack

- Python
- MySQL
- Groq API
- python-dotenv
- mysql-connector-python

## Project Structure

```
askdb-ai/
│
├── ai.py
├── database.py
├── prompts.py
├── main.py
│
├── metadata/
├── logs/
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## How It Works

```
User Question
      │
      ▼
Generate SQL using LLM
      │
      ▼
Execute SQL on MySQL
      │
      ▼
Retrieve Results
      │
      ▼
Generate Natural Language Response
      │
      ▼
Display Answer
```

## Installation

Clone the repository.

```bash
git clone https://github.com/Eashwar-Raj-R/askdb-ai.git
cd askdb-ai
```

Install the dependencies.

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file.

```env
HOSTNAME=localhost
USER=root
PASSWORD=your_password
DATABASE=your_database

GROQ_API_KEY=your_api_key
MODEL=openai/gpt-oss-120b
```

## Run

```bash
python main.py
```

## Example

```
AI > Hey, How can I help you today?

>>> Show the top 5 customers by total purchase.

AI >
The top five customers are:

1. John Doe
2. Jane Smith
3. Alex Johnson
```

## Current Workflow

1. Read the database schema.
2. Send the schema and user question to the LLM.
3. Generate a SQL query.
4. Execute the query on MySQL.
5. Send the query results back to the LLM.
6. Return a conversational response.

## Roadmap

- [x] Natural language to SQL generation
- [x] SQL execution
- [x] AI-generated responses
- [x] Logging
- [x] Object-oriented architecture
- [ ] SQL validation before execution
- [ ] Chat history
- [ ] Web interface
- [ ] Docker support
- [ ] PostgreSQL support
- [ ] Data visualization
- [ ] Unit tests

## Notes

This project is currently in active development. Future versions will focus on improving SQL validation, adding a web interface, supporting multiple databases, and enhancing overall reliability.

## License

This project is licensed under the MIT License.