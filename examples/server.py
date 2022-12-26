from flask import Flask, jsonify, make_response, request
from captcha_detector import Captcha_detection
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib

app = Flask(__name__)

@app.route('/')
def hello_world():
    new_url = request.args.get('url')
    print(request.args.get('url'))
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-web-security")
    options.add_argument("--log-level=3")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(new_url)
    m = driver.find_element(By.XPATH, '/html/body/img')
    m.screenshot("captcha.png")
    driver.close()
    time.sleep(5)

    response = {
        "Solved": True,
        "response": Captcha_detection('captcha.png')
        }
    return make_response(jsonify(response), 200)
    # print(Captcha_detection('12.png'))

if __name__ == '__main__':
    app.run()
