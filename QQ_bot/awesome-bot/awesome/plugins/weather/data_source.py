from nonebot import on_command, CommandSession
import json, requests, pprint

async def get_weather_of_city(city: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    weatherJsonUrl = "https://www.tianqiapi.com/api?version=v6&appid=21375891&appsecret=fTYv7v5E&city="+city
    print(weatherJsonUrl)
    response = requests.get(weatherJsonUrl)  # 获取并下载页面，其内容会保存在respons.text成员变量里面
    response.raise_for_status()  # 这句代码的意思如果请求失败的话就会抛出异常，请求正常就上面也不会做

    # 将json文件格式导入成python的格式
    weatherData = json.loads(response.text)
    pprint.pprint(weatherData)

    weather_dict = dict()
    weather_dict['tem1'] = weatherData['tem1']
    weather_dict['tem2'] = weatherData['tem2']
    weather_dict['air_tips'] = weatherData['air_tips']
    print(weather_dict)
    print(weather_dict['tem1'])

    return f'{city}的天气是'+'最高'+weather_dict['tem1']+'度'+'；'+'最'+weather_dict['tem2']+'度'+'；'+'温馨提醒'+'：'+weather_dict['air_tips']