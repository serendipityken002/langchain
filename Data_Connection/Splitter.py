from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter
import tiktoken

doc_str = """
This is a long document that needs to be split into smaller chunks. 
The text splitter will help us do that by breaking the text into smaller pieces based on a specified character limit. This is useful for processing large documents in a more manageable way.
The text splitter can be configured to split the text at different character limits, allowing for flexibility in how the text is processed. 
This is particularly useful when working with large documents that may be too cumbersome to handle in their entirety.
"""

# # 分隔符是一个字符串，默认为"\n\n"
# text_splitter = CharacterTextSplitter(
#     separator="\n", # 分隔符
#     chunk_size=200, # 每个块的最大大小
#     chunk_overlap=50, # 重叠的字符数
#     length_function=len, # 用于计算长度的函数
# )

# # 分隔符是一个列表，默认为["\n\n", "\n", " ", ""]
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=50,
#     chunk_overlap=20,
#     keep_separator=True,
# )

# docs = text_splitter.create_documents([doc_str])
# for doc in docs:
#     print(doc.page_content)
#     print(f"length: {len(doc.page_content)}")
#     print("=" * 66)

# # 基于token的文本拆分器
# text_splitter = TokenTextSplitter(
#     chunk_size=50,
#     chunk_overlap=20,
#     # model_name="gpt-3.5-turbo",
#     encoding_name="gpt2",
# )

# docs = text_splitter.create_documents([doc_str])
# token_encoder = tiktoken.get_encoding("gpt2")
# for doc in docs:
#     print(doc)
#     print(f"tokens: {len(token_encoder.encode(doc.page_content))}")
#     print("=" * 66)

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.document_transformers.openai_functions import (
    create_metadata_tagger)
import json

doc_str_cn = """
《鸣潮》是广州库洛公司开发的一款开放世界ARPG游戏，于2024年5月23日发布。
"""
documents = [Document(page_content=doc_str_cn)]

chat = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
propertiers = {
    'properties': {
        'name': {'type': 'string', 'description': '游戏名称'},
        'conpany': {'type': 'string', 'description': '公司名称'},
        'date': {'type': 'string', 'description': '发售日期，按照YYYY-MM-DD格式'},
    }
}

# 下面两行用于使用create_metadata_tagger函数创建一个文档转换器
document_transformer = create_metadata_tagger(
    metadata_schema=propertiers,
    llm=chat,
)
enhanced_docs = document_transformer.transform_documents(documents)

print(json.dumps(
    enhanced_docs[0].metadata, 
    indent=2, 
    ensure_ascii=False
))