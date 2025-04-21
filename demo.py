import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_KEY")

from langchain_openai import ChatOpenAI


# 加载 OpenAI 模型
chat = ChatOpenAI(model="gpt-3.5-turbo", base_url="https://api.chatanywhere.tech/v1")
res = chat.invoke('给我将一个故事')
print(res)