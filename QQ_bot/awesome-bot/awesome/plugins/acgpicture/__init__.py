from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from .data_source import get_picture_of_acg
from nonebot import CommandSession, IntentCommand, NLPSession, message, on_command, on_natural_language


@on_command('acgpicture', aliases=('来点涩图','涩图'))
async def acgpicture(session: CommandSession):
    # # 取得消息的内容，并且去掉首尾的空白符
    # city = session.current_arg_text.strip()
    # # 如果除了命令的名字之外用户还提供了别的内容，即用户直接将城市名跟在命令名后面，
    # # 则此时 city 不为空。例如用户可能发送了："天气 南京"，则此时 city == '南京'
    # # 否则这代表用户仅发送了："天气" 二字，机器人将会向其发送一条消息并且等待其回复
    # if not city:
    #     city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
    #     # 如果用户只发送空白符，则继续询问
    #     while not city:
    #         city = (await session.aget(prompt='要查询的城市名称不能为空呢，请重新输入')).strip()
    # # 获取城市的天气预报
    message = await get_picture_of_acg(1)
    print(message)
    await session.send(message)


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'涩图'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    city = None
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'ns':
            # ns 词性表示地名
            city = word.word
            break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'acgpicture', current_arg=city or '')