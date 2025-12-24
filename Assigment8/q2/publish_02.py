import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT)
client.loop_start()

appliances = ["home/light1", "home/fan1"]

try:
    while True:
        for topic in appliances:
            # Toggle ON/OFF alternately
            client.publish(topic, "ON", qos=1)
            print(f"Sent {topic}: ON")
            time.sleep(2)

            client.publish(topic, "OFF", qos=1)
            print(f"Sent {topic}: OFF")
            time.sleep(2)

except KeyboardInterrupt:
    print("Exiting controller...")
finally:
    client.loop_stop()
    client.disconnect()