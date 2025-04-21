import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_KEY")

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage, ChatMessage
import json

functions = [
    {
        'name': 'get_current_weather',
        'description': '通过城市名称获取城市当前天气',
        'parameters': {
            'type': 'object',
            'properties': {
                'city_name': {
                    'type': 'string',
                    'description': '城市名称',
                },
            },
            'required': ['city_name'],
        },
    }
]

def get_current_weather(city_name):
    return f'20度，晴天'

llm = ChatOpenAI()
messages = llm.predict_messages(
    [HumanMessage(content='请告诉我北京的天气')],
    functions=functions,
)

function_name = messages.additional_kwargs['function_call']['name']
function_args = json.loads(messages.additional_kwargs['function_call']['arguments'])
function_res = globals()[function_name](**function_args)

second_response = llm.predict_messages(
    [
        HumanMessage(content='请告诉我北京的天气'),
        AIMessage(content=str(messages.additional_kwargs)),
        ChatMessage(
            role='function',
            additional_kwargs={'name': function_name},
            content=function_res,
        ),
    ]
)
print(second_response)