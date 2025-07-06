import sqlite3
from flask import Flask, jsonify, request

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

@app.route('/api/latest_reading', methods=['GET'])
def latest_reading():
    conn = sqlite3.connect('plant_data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM plant_readings ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        latest_reading_dict = {key: row[key] for key in row.keys()}
        return jsonify(latest_reading_dict)
    else:
        return jsonify({"message": "No readings found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
