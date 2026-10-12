import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('ilscs_telemetry.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS event_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            floor INTEGER,
            presence_verified BOOLEAN,
            crowd_count INTEGER,
            latency_ms REAL,
            action_taken TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_event(floor, verified, crowd_count, latency, action):
    init_db()
    conn = sqlite3.connect('ilscs_telemetry.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO event_logs (timestamp, floor, presence_verified, crowd_count, latency_ms, action_taken)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.now().isoformat(), floor, verified, crowd_count, latency, action))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    log_event(1, True, 2, 1420.5, "DISPATCHED")
    print("Database initialized successfully. Sample log entry created.")