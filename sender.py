# python 3.6

import random
from signal import signal
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def send_signals(client,signalType):
    """
        Sends a signal every _RECPIES_SECONDS_DELAY
    """
    message = ""

    while True:
        if signalType == "urgenta":
            senzor = random.randint(0, 1)
            if(senzor == 1):
                message = "A avut loc un accident"
            else:
                message = "Nu a avut loc niciun accident"
        """
        if(signalType == "dezaburire"):
        if(signalType == "faruri"):
        if(signalType == "franare"):
        """
        if signalType == 'dezaburire':
            indice_refractie = random.uniform(1.45, 1.80)
            if indice_refractie <= 1.60:
                message = 'Geamul nu este aburit.'
            else:
                message = 'Geamul este aburit!'

        if signalType == 'franare':
            #  Generam distanta (in metri) pana la urmatoarea masina si viteza curenta
            distance = random.randint(20, 200)
            speed = random.randint(10, 250)
            time_to_brake = distance / speed * 0.75

            if time_to_brake <= 7.0:
                message = "Frana!"
            else:
                message = "Nu frana automat!"

        if signalType == "ambiental":
            #  Greutatea persoanei din dreapta.
            senzor = random.randint(35, 120)  
            message = "S-a asezat o persoana pe scaunul din dreapta. Greutate: %d" % (senzor)

            

        new_publish(client,message)
        time.sleep(5)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def new_publish(client, message):
    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent message `{message}`")
    else:
        print(f"Failed to send message to topic {topic}")

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    send_signals(client,"urgenta")


if __name__ == '__main__':
    run()
