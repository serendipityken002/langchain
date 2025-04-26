import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

prompt1 = PromptTemplate.from_template(
    '你是一个优秀的物理专家，你很擅长用简单易懂的方式解释物理问题。'
    '请用中文回答以下问题：{input}'
)

prompt2 = PromptTemplate.from_template(
    '你是一个优秀的数学专家，你很擅长用简单易懂的方式解释数学问题。'
    '请用中文回答以下问题：{input}'
)

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0.1)

# 并行执行两个链
math_chain = prompt1 | llm
physics_chain = prompt2 | llm
map_chain = RunnableParallel(math = math_chain, physics = physics_chain)
print(map_chain.invoke(
    {"input": "请问牛顿第一定律是什么？"}
))