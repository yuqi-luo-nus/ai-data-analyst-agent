# from app.db import run_query
# from app.analysis import plot_growth
# from app.report import generate_report

# sql = """
# WITH revenue_by_quarter AS (
#     SELECT
#         product_category,
#         quarter,
#         SUM(revenue) AS total_revenue
#     FROM sales
#     GROUP BY product_category, quarter
# ),
# pivoted AS (
#     SELECT
#         product_category,
#         MAX(CASE WHEN quarter = 'Q1' THEN total_revenue END) AS q1_revenue,
#         MAX(CASE WHEN quarter = 'Q2' THEN total_revenue END) AS q2_revenue
#     FROM revenue_by_quarter
#     GROUP BY product_category
# )
# SELECT
#     product_category,
#     q1_revenue,
#     q2_revenue,
#     ROUND((q2_revenue - q1_revenue) * 100.0 / q1_revenue, 2) AS growth_rate
# FROM pivoted
# ORDER BY growth_rate DESC
# """

# df = run_query(sql)

# chart_path = plot_growth(df)

# report = generate_report(df)

# print("SQL query result:")
# print(df)

# print("\nReport:")
# print(report)

# print(f"\nChart saved to: {chart_path}")
from app.sql_generator import generate_sql

question = "Which product category had the highest revenue growth in the last quarter?"

sql = generate_sql(question)

print("Question:")
print(question)

print("\nGenerated SQL:")
print(sql)