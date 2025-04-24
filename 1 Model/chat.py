import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# 加载 OpenAI 模型
chat = ChatOpenAI(model="gpt-3.5-turbo", base_url="https://api.chatanywhere.tech/v1")
batch_messages = [
    [
    SystemMessage(content="you are a singer"),
    HumanMessage(content="你是谁？")
    ],
    [
    SystemMessage(content="you are a doctor"),
    HumanMessage(content="你是谁？")
    ],
]
res = chat.generate(batch_messages)
print(res)