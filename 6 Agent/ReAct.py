import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain_openai import ChatOpenAI
from langchain_community.docstore.wikipedia import Wikipedia
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.agents.react.base import DocstoreExplorer

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0)

docstore = DocstoreExplorer(Wikipedia())
tools = [
    Tool(
        name='Search',
        func=docstore.search,
        description='当你需要搜索的时候使用'
    ),
    Tool(
        name='Lookup',
        func=docstore.lookup,
        description='当你需要查找的时候使用'
    )
]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.REACT_DOCSTORE,
    verbose=True
)
print(agent.run('2023年微软CEO出生在哪个国家？'))