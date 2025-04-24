import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0.8)

prompt1 = PromptTemplate.from_template(
    '你是一个优秀的编剧，请用你丰富的想象力根据我写的标题编写一个故事概要。'
    '标题是：{title}。'
)

chain1 = LLMChain(llm=llm, prompt=prompt1)

prompt2 = PromptTemplate.from_template(
    '你是一个优秀的广告写手，请根据我给的故事概要，'
    '为这个故事编写一个吸引人的广告语。'
    '故事概要：{story}'
)

chain2 = LLMChain(llm=llm, prompt=prompt2)

# 将剧本和广告语的链条串联起来
chain = SimpleSequentialChain(
    chains=[chain1, chain2], 
)
print(chain.run("孙悟空大战变形金刚"))