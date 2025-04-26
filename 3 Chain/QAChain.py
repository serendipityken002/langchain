import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
import shutil

text = [
    '你好啊！',
    '你叫什么名字？',
    '我的朋友们都叫我小明',
    '我的年龄是18岁',
    '我喜欢打篮球',
]

# 每次运行前清除旧数据库
if os.path.exists("./chroma_test/"):
    shutil.rmtree("./chroma_test/")

db = Chroma.from_texts(
    text,
    OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1"),
    persist_directory="./chroma_test/",
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(base_url="https://api.chatanywhere.tech/v1"),
    retriever=db.as_retriever()
)

chat_history = []
res = qa_chain({
    "question": "你叫什么名字？",
    "chat_history": chat_history,
})

chat_history.append((res["question"], res["answer"]))
print(chat_history)

print(qa_chain({
    "question": "你喜欢什么运动？",
    "chat_history": chat_history,
}))