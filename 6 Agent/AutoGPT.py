from langchain.agents import Tool
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from langchain_experimental.auto_gpt import AutoGPT
from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.file_management.write import WriteFileTool

search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name='Search',
        func=search.run,
        description='当你需要搜索的时候使用'
    ),
    WriteFileTool(),
    ReadFileTool(),
]

embedding = OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1")
vectorstore = Chroma(
    persist_directory="./chroma_test",
    embedding_function=embedding
)

agent = AutoGPT.from_llm_and_tools(
    llm=ChatOpenAI(madel_name='gpt-4.1-nano', base_url="https://api.chatanywhere.tech/v1", temperature=0),
    tools=tools,
    ai_name='Tom',
    ai_role='Tom是一个AI助手，帮助用户完成任务',
    memory=vectorstore.as_retriever(),
)

agent.chain.verbose = True

agent.run('请帮我写一个Python程序，计算1到100的和，并将结果保存到文件中。文件名为demo.py')