import client.runner as client_runner
import brain.runner as brain_runner
import connection.mqtt_connection as mqtt_connection



def main():

    client_runner.start()

if __name__ == '__main__':
    main()
