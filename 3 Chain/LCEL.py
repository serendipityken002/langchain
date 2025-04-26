import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import ConfigurableField
from langchain.schema.runnable import RunnablePassthrough

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")

story = PromptTemplate.from_template('给我讲一个关于{question}的故事')
joke = PromptTemplate.from_template('给我讲一个关于{question}的笑话')

prompt = PromptTemplate.from_template(
    '给我讲一个关于{question}的演讲词'
).configurable_alternatives(
    ConfigurableField(id='prompt'),
    story=story,
    joke=joke,
    default_key='speech' # 默认的可选项
)

# chain = prompt | llm
# # print(chain.invoke({'question': '程序员'}))

# res = chain.with_config(
#     configurable={'prompt': 'joke'}
# ).invoke({'question': '程序员'})

# print(res)

def handel_query(data):
    return '前端' + data['question']

def handle_metadata(data):
    return {'user': 'xiaoming'}

chain = (RunnablePassthrough.assign(
    metadata=handle_metadata, 
    question=handel_query
    ) | prompt | llm
)

print(chain.invoke({'question': '程序员'}))