import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
prompt = PromptTemplate.from_template(
    '请给我将{count}个关于{topic}的中文问题，问题要简短且有趣。'
)

chain = LLMChain(llm=llm, prompt=prompt)

# response = chain.run(count=5, topic="人工智能")
# print(response)

inputs = [
    {'count': 1, 'topic': '人工智能'},
    {'count': 2, 'topic': '机器学习'},
    {'count': 1, 'topic': '深度学习'}
]
res = chain.apply(inputs)
for i in range(len(inputs)):
    print(res[i])