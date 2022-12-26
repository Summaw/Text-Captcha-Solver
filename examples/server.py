from flask import Flask, jsonify, make_response
from captcha_detector import Captcha_detection

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = {
        "Answer": Captcha_detection('12.png'),
        "Solved": True,
    }
    return make_response(jsonify(response), 200)
    # print(Captcha_detection('12.png'))

if __name__ == '__main__':
    app.run()
