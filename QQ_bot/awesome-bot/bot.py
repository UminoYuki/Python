import nonebot
from os import path
# 导入配置
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),    # 导入/awesome/plugins下的插件
        'awesome.plugins'
    )
    nonebot.run()