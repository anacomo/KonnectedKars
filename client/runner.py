"""
    Entry point of the client (coffee machines)
"""

import logging
import connection.mqtt_connection as mqtt_connection


def start():

    # Start the client -- connect to the MQTT brocker
    print("Client started. Starting MQTT Server...")
    mqtt_connection.load_client("client")
    mqtt_connection.start_client()
    mqtt_connection.publish()

    # Register the callbacks to be called when stuff happens.
    print("MQTT server started. Registering callbacks")
