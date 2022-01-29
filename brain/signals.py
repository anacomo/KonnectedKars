"""
    Sends every X seconds a list of recipes.
"""

import threading
import time
import common.mqtt_connection as mqtt_connection

_RECIPES_SECONDS_DELAY = 5

def _recipes_sender():
    """
        Sends a signal every _RECPIES_SECONDS_DELAY
    """
    while True:
        recipes = [i for i in database.get_recipes().find()]
        for i in recipes:
            del i['_id']
        recipes_book = mqtt_messages.build_recipes_book_from_dict({"recipes": recipes})

        mqtt_connection.publish(mqtt_topics.AVAILABLE_RECIPES, recipes_book)
        time.sleep(_RECIPES_SECONDS_DELAY)

def start_recipes_broadcast():
    """
        Starts a thread handling the broadcast.
    """
    threading.Thread(target=_recipes_sender).start()