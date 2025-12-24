import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

BROKER = "localhost"
PORT = 1883

TOPICS = [("home/light1", 1), ("home/fan1", 1)]

DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # replace with your MySQL user
    "password": "root",
    "database": "smarthome",
    "autocommit": True
}

def insert_status(conn, appliance_name, status, topic):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO appliance_status (appliance_name, status, updated_at, topic)
            VALUES (%s, %s, %s, %s)
            """,
            (appliance_name, status, datetime.utcnow(), topic)
        )

def on_connect(client, userdata, flags, reason_code):
    print("Connected to MQTT with code:", reason_code)
    for t in TOPICS:
        client.subscribe(t)
    print("Subscribed to topics:", [t[0] for t in TOPICS])

def on_message(client, userdata, msg):
    conn = userdata["db_conn"]
    payload = msg.payload.decode("utf-8").strip()
    appliance_name = msg.topic.split("/")[-1]  # e.g., 'light1'
    if payload in ["ON", "OFF"]:
        insert_status(conn, appliance_name, payload, msg.topic)
        print(f"Updated {appliance_name} → {payload}")
    else:
        print("Invalid command:", payload)

def main():
    conn = mysql.connector.connect(**DB_CONFIG)
    client = mqtt.Client()
    client.user_data_set({"db_conn": conn})
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_forever()

if __name__ == "__main__":
    main()