import sqlite3
from flask import Flask

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('plant_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plant_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            moisture_level REAL,
            temperature REAL,
            light_intensity REAL,
            notes TEXT,
            plant_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
