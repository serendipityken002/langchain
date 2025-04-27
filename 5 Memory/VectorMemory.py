import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain_openai import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain.chains import ConversationChain
import shutil

# 每次运行前清除旧数据库
if os.path.exists("./chroma_test/"):
    shutil.rmtree("./chroma_test/")

db = Chroma(
    embedding_function=OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1"),
    persist_directory="./chroma_test/",
)

retriever = db.as_retriever(search_kwargs={"k": 1})

memory = VectorStoreRetrieverMemory(retriever=retriever)

chain = ConversationChain(
    llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1"),
    memory=memory,
    verbose=True,
)
chain.run('请记住我最喜欢的水果是葡萄')
chain.run('你能为我做什么')
print(chain.run('我最喜欢的水果是什么？'))