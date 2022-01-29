"""
    Entry point of the server.
"""

import contextlib
import threading, time, os
import logging

import common.mqtt_connection as mqtt_connection


def start():
    print("Server started.")
    mqtt_connection.load_client("server")
    mqtt_connection.subscribe()
    mqtt_connection.start_forever()
