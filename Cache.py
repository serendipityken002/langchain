import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_KEY")

import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
import time

langchain.llm_cache = InMemoryCache()
llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
start_time = time.time()
print(llm.invoke("你是谁？").content)
print("第一次调用耗时：", time.time() - start_time)

start_time = time.time()
print(llm.invoke("你是谁？").content)
print("第二次调用耗时：", time.time() - start_time)