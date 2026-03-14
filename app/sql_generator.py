import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

SCHEMA = """
Table: sales
Columns:
- date (string)
- quarter (string)
- product_category (string)
- revenue (integer)
- units_sold (integer)
- region (string)
"""

def generate_sql(user_question: str) -> str:

    prompt = f"""
You are a data analyst assistant.

Given the following database schema:

{SCHEMA}

Write a DuckDB SQL query that answers this question:

{user_question}

Rules:
1. Only use table sales
2. Return only SQL
3. No explanation
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a text-to-SQL expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql