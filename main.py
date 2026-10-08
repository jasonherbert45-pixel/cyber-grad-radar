import sqlite3
from pathlib import Path


database_path = Path("data/jobs.db")

database_path.parent.mkdir(exist_ok=True)

connection = sqlite3.connect(database_path)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    title TEXT NOT NULL,
    location TEXT,
    url TEXT UNIQUE NOT NULL,
    date_found TEXT,
    status TEXT DEFAULT 'new',
    score INTEGER
)
""")

connection.commit()
connection.close()

print("Cyber Grad Radar database ready.")