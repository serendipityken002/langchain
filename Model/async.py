import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

import time
import asyncio
from langchain_openai import ChatOpenAI

def generate():
    chat = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
    for _ in range(5):
        res = chat.invoke("你是谁?")


async def generate2(chat):
    res = await chat.ainvoke("你是谁?")


async def generate_content():
    chat = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
    tasks = []
    for _ in range(5):
        task = asyncio.create_task(generate2(chat))
        tasks.append(task)
    await asyncio.gather(*tasks)

time_start = time.time()
generate()
print("串行执行时间:", time.time() - time_start)

time_start = time.time()
asyncio.run(generate_content())
print("异步执行时间:", time.time() - time_start)