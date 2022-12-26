import requests
import asyncio


async def start(captcha_url):
    url = f'http://127.0.0.1:5000/?url={captcha_url}'

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ in "__main__":
    captcha_url = 'your captcha image url'
    asyncio.run(start(captcha_url))
