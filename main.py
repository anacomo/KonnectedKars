from flask import Flask, request, jsonify, send_file, Response, render_template
import base64
import client.runner as client_runner
import brain.runner as server_runner


def main():

    client_runner.start()

if __name__ == '__main__':
    main()
