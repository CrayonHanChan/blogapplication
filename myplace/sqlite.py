import sqlite3

conn = sqlite3.connect("fastapi.db")
cursor = conn.cursor()
cursor.execute("SELECT sqlite_version();")
print(f"SQLite Version: {cursor.fetchone()[0]}")
conn.close()
