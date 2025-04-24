import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.chains.router import MultiPromptChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import (
    LLMRouterChain,
    RouterOutputParser,
)
from langchain.chains.router.multi_prompt_prompt import (
    MULTI_PROMPT_ROUTER_TEMPLATE
)

prompt1 = PromptTemplate.from_template(
    '你是一个优秀的物理专家，你很擅长用简单易懂的方式解释物理问题。'
    '请用中文回答以下问题：{input}'
)

prompt2 = PromptTemplate.from_template(
    '你是一个优秀的数学专家，你很擅长用简单易懂的方式解释数学问题。'
    '请用中文回答以下问题：{input}'
)

# 创建模板信息列表
templates = [
    {
        "name": "物理",
        "description": "用于解答物理相关的问题",
        "prompt": prompt1,
    },
    {
        "name": "数学",
        "description": "用于解决数学相关的问题",
        "prompt": prompt2,
    },
]

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1", temperature=0.1)

# 生成键为模板名称，值为chain的字典
destination_chains = {}
for template in templates:
    destination_chains[template["name"]] = LLMChain(
        llm=llm,
        prompt=template["prompt"]
    )

# 创建路由器链
destinations = [f'{p["name"]}: {p["description"]}' for p in templates]
destination_str = '\n'.join(destinations)

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destination_str,
)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(
    llm=llm,
    prompt=router_prompt
)

default_chain = ConversationChain(llm=llm, output_key="text")
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

print(chain.invoke(
    {"input": "请问牛顿第一定律是什么？"}
    # {"input": "如何进行矩阵乘法？"}
))