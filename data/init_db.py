import duckdb
import pandas as pd

# 读取CSV
df = pd.read_csv("data/sales.csv")

# 创建数据库
con = duckdb.connect("data/business.db")

# 删除旧表
con.execute("DROP TABLE IF EXISTS sales")

# 创建表
con.execute("""
CREATE TABLE sales AS
SELECT * FROM df
""")

print("Database created successfully!\n")

# 查看数据
result = con.execute("SELECT * FROM sales LIMIT 5").fetchdf()

print("Sample data:")
print(result)

con.close()