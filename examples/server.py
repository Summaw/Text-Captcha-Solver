from flask import Flask, jsonify, make_response, request
from captcha_detector import Captcha_detection
from time import sleep
import time
import urllib
import httpx

app = Flask(__name__)

@app.route('/')
def hello_world():
    new_url = request.args.get('url')
    print(request.args.get('url'))

    session = httpx.Client(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'},timeout=30)
    url = new_url
    output_file = 'captcha.png'
    response = session.get(url)

    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)

        print(f"Photo downloaded and saved as '{output_file}'")
    else:
        print(f"Failed to download the photo. Status code: {response.status_code}")

    response = {
        "Solved": True,
        "response": Captcha_detection('captcha.png')
        }
    return make_response(jsonify(response), 200)

if __name__ == '__main__':
    app.run()
