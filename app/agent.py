from app.sql_generator import generate_sql
from app.db import run_query
from app.analysis import plot_growth
from app.report import generate_report


def run_data_analyst_agent(question):

    sql = generate_sql(question)

    df = run_query(sql)

    chart = plot_growth(df)

    report = generate_report(df)

    result = {
        "question": question,
        "sql": sql,
        "data": df.to_dict(orient="records"),
        "report": report,
        "chart_path": chart
    }

    return result