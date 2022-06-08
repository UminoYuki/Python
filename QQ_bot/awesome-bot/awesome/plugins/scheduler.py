# 整点报时

from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():

    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    msg = [
        {
            "type": "text",
            "data": {
                "text": f'现在{now.hour}点整啦！'
            }
        },
        # 'file:///D:/PyProject/spider/qqbot/src/plugins/pic1.png'
        {
            "type": "image",
            "data": {
                "file": 'file:///C:/Users/Umino/Documents/Python/QQ_bot/awesome-bot/1.jpg',
            }
        }
    ]
    try:
        await bot.send_group_msg(group_id=1014821985,
                                 message=msg)
    except CQHttpError:
        pass