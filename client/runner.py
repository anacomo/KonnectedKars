"""
    Entry point of the client (coffee machines)
"""

import logging
import connection.mqtt_connection as mqtt_connection


def start():

    c = mqtt_connection.Client()
    # Start the client -- connect to the MQTT brocker
    print("Client started. Starting MQTT Server...")
    c.load_client("client")
    c.start_client()
    c.publish()

    # Register the callbacks to be called when stuff happens.
    print("MQTT server started. Registering callbacks")
