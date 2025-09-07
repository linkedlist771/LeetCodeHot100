#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的OpenAI Function Calling示例 - 天气查询
"""

import json

from loguru import logger
from openai import OpenAI

# 初始化OpenAI客户端
client = OpenAI()


def get_weather(location):
    """
    获取指定位置的天气信息
    这里使用免费的OpenWeatherMap API作为示例
    """
    try:
        # 这里使用模拟数据，你也可以替换为真实的天气API
        # API_KEY = "你的天气API密钥"
        # url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric&lang=zh_cn"
        # response = requests.get(url)
        # data = response.json()

        # 模拟天气数据
        weather_data = {
            "location": location,
            "temperature": "22°C",
            "description": "晴朗",
            "humidity": "65%",
            "wind": "微风 5km/h",
        }

        return json.dumps(weather_data, ensure_ascii=False)

    except Exception as e:
        return json.dumps({"error": f"获取天气失败: {str(e)}"}, ensure_ascii=False)


# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的当前天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "城市名称，例如：北京、上海、纽约"}
                },
                "required": ["location"],
            },
        },
    }
]


def chat_with_weather():
    """主聊天功能"""

    # 用户问题
    user_question = "今天天气怎么样。北京"
    print(f"用户问题: {user_question}")

    # 消息列表
    messages = [
        {"role": "system", "content": "你是一个天气助手，可以查询世界各地的天气信息。"},
        {"role": "user", "content": user_question},
    ]

    # 第一次API调用 - 让模型决定是否需要调用函数
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        timeout=60,
    )

    response_message = response.choices[0].message
    logger.debug(f"tool_calls:\n{response_message.tool_calls}")
    # 检查是否有函数调用
    if response_message.tool_calls:
        print("🔍 AI决定调用天气查询功能...")

        # 添加AI的响应到消息历史
        messages.append(response_message)

        # 处理函数调用
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            print(f"📍 查询城市: {function_args['location']}")

            # 调用天气函数
            if function_name == "get_weather":
                function_response = get_weather(function_args["location"])
                print(f"🌤️  天气数据: {function_response}")

                # 将函数结果添加到消息历史
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    }
                )

        # 第二次API调用 - 基于天气数据生成最终回复
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            timeout=60,
        )

        final_answer = final_response.choices[0].message.content
        print(f"\n🤖 AI回复: {final_answer}")

    else:
        # 没有函数调用，直接回复
        print(f"🤖 AI回复: {response_message.content}")


if __name__ == "__main__":
    chat_with_weather()
