import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationTokenBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")

memory = ConversationSummaryBufferMemory(
    llm = llm,
    max_token_limit=100
)

memory.save_context({"input": "你是谁啊？"}, {"output": "我叫小天，一个智能助手。"})
memory.save_context({"input": "你能做什么？"}, {"output": "我可以回答你的问题，提供信息和建议，帮助你完成任务。"})
memory.save_context({"input": "你能帮我写代码吗？"}, {"output": "当然可以，我可以帮助你编写Python、JavaScript等多种语言的代码。"})
memory.save_context({"input": "我喜欢吃什么？"}, {"output": "你喜欢吃披萨和汉堡。"})

# 获取历史消息
print(memory.load_memory_variables({}))

chain = ConversationChain(llm=llm, memory=memory, verbose=True)
print(chain.run("你是谁？"))