import sqlite3
from pathlib import Path


database_path = Path("data/jobs.db")


def create_database():
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


def add_job(company, title, location, url, date_found):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO jobs
    (company, title, location, url, date_found)
    VALUES (?, ?, ?, ?, ?)
    """, (
        company,
        title,
        location,
        url,
        date_found
    ))

    connection.commit()
    connection.close()


def get_jobs():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT company, title, location
    FROM jobs
    """)

    jobs = cursor.fetchall()

    connection.close()

    return jobs