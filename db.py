import sqlite3

conn = sqlite3.connect("messages_db.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
message TEXT NOT NULL 
)
""")
conn.commit()
conn.close()
print(type(c))