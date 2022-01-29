"""
    Entry point of the server.
"""

import contextlib
import threading, time, os
import logging

import connection.mqtt_connection as mqtt_connection


def start():
    c = mqtt_connection.Client()
    print("Server started.")
    c.load_client("server")
    c.subscribe()
    c.start_forever()
