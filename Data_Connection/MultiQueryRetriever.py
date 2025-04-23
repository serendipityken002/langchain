import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

import logging
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import MultiQueryRetriever
import shutil
from langchain.chat_models import ChatOpenAI

loader = WebBaseLoader(
    'https://www.yixue.com/%E7%96%BE%E7%97%85%E7%9A%84%E5%88%86%E7%B1%BB'
)
data = loader.load()

# 分割数据
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)
splits = splitter.split_documents(data)

# 每次运行前清除旧数据库
if os.path.exists("./chroma_test/"):
    shutil.rmtree("./chroma_test/")

# 存入向量数据
vectordb = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1"),
    persist_directory="./chroma_test/",
)

# 初始化检索器
llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(),
    llm=llm,
)

# 设置日志级别
logging.basicConfig()
logging.getLogger(
    'langchain.retrievers.multi_query'
).setLevel(logging.INFO)

# 进行检索
docs = retriever_from_llm.get_relevant_documents(
    query="什么是遗传病？"
)
for doc in docs:
    print(doc.page_content)
    print("===" * 10)