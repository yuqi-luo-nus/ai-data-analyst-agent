import duckdb
import pandas as pd

DB_PATH = "data/business.db"

def run_query(sql: str) -> pd.DataFrame:
    con = duckdb.connect(DB_PATH)
    try:
        df = con.execute(sql).fetchdf()
        return df
    finally:
        con.close()