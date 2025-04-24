import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

# 加载并分割文档
loader = TextLoader(file_path='3 Chain\data\demo.txt', encoding='utf-8')
spliter = RecursiveCharacterTextSplitter(
    chunk_size=350,
    chunk_overlap=0
)
documents = spliter.split_documents(loader.load())[:15]

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0.2)

chain = load_summarize_chain(
    llm=llm,
    chain_type='stuff'
)
print(chain.run(documents))