import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

@app.route('/api/readings', methods=['GET'])
def get_readings():
    conn = sqlite3.connect('plant_data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = "SELECT * FROM plant_readings"
    params = []

    if start_date and end_date:
        query += " WHERE timestamp BETWEEN ? AND ?"
        params.extend([start_date, end_date])
    elif start_date:
        query += " WHERE timestamp >= ?"
        params.append(start_date)
    elif end_date:
        query += " WHERE timestamp <= ?"
        params.append(end_date)

    query += " ORDER BY timestamp ASC"

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    readings = [{key: row[key] for key in row.keys()} for row in rows]
    return jsonify(readings)

import random
import datetime

def generate_simulated_reading():
    moisture = round(random.uniform(30, 90), 2)
    temperature = round(random.uniform(18, 28), 2)
    light = round(random.uniform(200, 1000), 2)
    timestamp = datetime.datetime.now().isoformat()
    return {
        'timestamp': timestamp,
        'moisture_level': moisture,
        'temperature': temperature,
        'light_intensity': light,
        'notes': 'Simulated data',
        'plant_id': 1
    }

@app.route('/simulate_data', methods=['GET'])
def simulate_data():
    reading = generate_simulated_reading()
    conn = sqlite3.connect('plant_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO plant_readings (timestamp, moisture_level, temperature, light_intensity, notes, plant_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (reading['timestamp'], reading['moisture_level'], reading['temperature'], reading['light_intensity'], reading['notes'], reading['plant_id']))
    conn.commit()
    conn.close()
    return jsonify(reading)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
