import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.vectorstores import FAISS
import shutil
em_model = OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1")

# em_query = em_model.embed_query("What is your name?")
# print(em_query)

text = [
    '在这里！',
    '你好啊！',
    '你好，世界！',
    '你叫什么名字？',
    '我和我的朋友们都称呼我为小明',
    '哦，那太棒了！',
]

# 每次运行前清除旧数据库
if os.path.exists("./chroma_test/"):
    shutil.rmtree("./chroma_test/")

db = Chroma.from_texts(
    text,
    OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1"),
    persist_directory="./chroma_test/",
)

# 相关性搜索
query = '谈话中和名字相关的有哪些？'
docs = db.similarity_search(query, k=3)
for doc in docs:
    print(doc.page_content)
    print("===" * 10)


# db = FAISS.from_texts(
#     text,
#     OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1")
# )

# query = "谈话中和名字相关的有哪些？"
# em_vector = OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1").embed_query(query)
# docxs = db.similarity_search_by_vector(em_vector, k=3)
# for doc in docxs:
#     print(doc.page_content)
#     print("===" * 10)