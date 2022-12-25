from flask import Flask
from captcha_detector import Captcha_detection

app = Flask(__name__)

@app.route('/')
def hello_world():
    return Captcha_detection('12.png')

if __name__ == '__main__':
    app.run()
