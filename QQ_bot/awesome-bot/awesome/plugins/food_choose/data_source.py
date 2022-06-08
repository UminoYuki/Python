import requests
from nonebot import message
import urllib.request


async def get_food(city: str) -> str:
    url = 'https://api.mz-moe.cn/img.php'
    r = requests.get(url, allow_redirects=False)
    urlx = r.headers['Location']
    message=[
        {
            "type": "image",
            "data": {
                "file": urlx
            }
        }
    ]
    return message