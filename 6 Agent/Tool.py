import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain_openai import ChatOpenAI
from langchain.tools import StructuredTool
from langchain.agents import initialize_agent, AgentType

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

plus_tool = StructuredTool.from_function(
    func=plus,
    name="plus",
    description="加法运算"
)
minus_tool = StructuredTool.from_function(
    func=minus,
    name="minus",
    description="减法运算"
)
multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="乘法运算"
)
divide_tool = StructuredTool.from_function(
    func=divide,
    name="divide",
    description="除法运算"
)

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0)

agent = initialize_agent(
    tools=[plus_tool, minus_tool, multiply_tool, divide_tool],
    llm=llm,
    agent_type=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
print(agent.run('6加10等于多少？'))