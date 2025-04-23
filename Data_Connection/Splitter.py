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
doc_str_cn = """
这是一个很长的文档，需要拆分成更小的块。
文本拆分器将通过根据指定的字符限制将文本分成更小的片段来帮助我们做到这一点。这对于以更易于管理的方式处理大型文档非常有用。
文本拆分器可以配置为以不同的字符限制拆分文本，从而灵活地处理文本。
这在处理可能过于繁琐而无法完整处理的大型文档时特别有用。
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

# 基于token的文本拆分器
text_splitter = TokenTextSplitter(
    chunk_size=50,
    chunk_overlap=20,
    # model_name="gpt-3.5-turbo",
    encoding_name="gpt2",
)

docs = text_splitter.create_documents([doc_str_cn])
token_encoder = tiktoken.get_encoding("gpt2")
for doc in docs:
    print(doc)
    print(f"tokens: {len(token_encoder.encode(doc.page_content))}")
    print("=" * 66)