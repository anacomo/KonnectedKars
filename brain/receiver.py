from paho.mqtt import client as mqtt_client
from car_control_unit import CarControlUnit

broker = 'broker.emqx.io'
port = 1883
topic = 'konnectedKars'
client_id = 'python-mqtt-client-0'
username = ''
password = ''

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected to MQTT broker!')
        else:
            print('Failed to connect, return code %d\n', rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client, car_control_unit):
    def on_message(client, userdata, msg):
        message = msg.payload.decode()
        print(f"Received `{message}` from `{msg.topic}` topic")
        car_control_unit.handle_message(message)

    client.subscribe(topic)
    client.on_message = on_message


def run(car_control_unit):
    client = connect_mqtt()
    subscribe(client, car_control_unit)
    client.loop_forever()

if __name__ == '__main__':
    car_control_unit = CarControlUnit()
    run(car_control_unit)
