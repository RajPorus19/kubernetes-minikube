from flask import Flask, request
import datetime
import json
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
app.config['TIMEOUT'] = 300
CORS(app)

@app.route('/', methods=['GET'])
def main_route():
    name = os.environ.get('HOSTNAME','NO NAME FOUND')
    url = os.environ.get("URL_TO_CHECK","NONE")
    response = {"greeting":"Hello, my name is "+name+" !"}
    if url != "NONE":
        res = requests.get(url)
        if res.status_code == 200 and res.text == "Hello, world":
            response["healthcheck"] = "Website is up ! :)"
        else:
            response["healthcheck"] = "Website is down ! :("

    return response, 200


if __name__ == "__main__":
    app.run()
