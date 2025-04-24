import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

db = SQLDatabase.from_uri(
    "mysql+pymysql://root:123456@localhost:3306/study_test"
)

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
excutor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True
)






print(excutor.run("judy的'数据库'这门课考多少分？"))