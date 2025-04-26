import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

prompt_tql = PromptTemplate.from_template(
    '请帮我用{language}语言写一个打印"Hello World"的程序。'
)

# prompt_tql.save("4 Prompt/prompt_tql.json") # 保存为json文件

prompt = prompt_tql.partial(language="Python") # partial 允许提供部分参数

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0.1)
res = llm.invoke(prompt_tql.format(language="Python"))
print(res)