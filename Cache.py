import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_KEY")

import langchain
from langchain.cache import InMemoryCache
from langchain.cache import GPTCache

from gptcache import Cache
from gptcache.adapter.api import init_similar_cache
from gptcache.embedding import OpenAI as OpenAIEmbedding
from langchain_openai import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
import time

def init_gptcache(cache_obj: Cache, llm_string: str):
    init_similar_cache(
        cache_obj=cache_obj,
        embedding_func=OpenAIEmbedding(),
    )

langchain.llm_cache = InMemoryCache()
# langchain.llm_cache = GPTCache(init_gptcache)
llm = ChatOpenAI(
    base_url="https://api.chatanywhere.tech/v1", 
    streaming=True, 
    callbacks=[StreamingStdOutCallbackHandler()],
)

start_time = time.time()
print(llm.invoke("你是谁？").content)
print("第一次调用耗时：", time.time() - start_time)

start_time = time.time()
print(llm.invoke("你是谁？").content)
print("第二次调用耗时：", time.time() - start_time)