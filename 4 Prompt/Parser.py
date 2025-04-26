import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.output_parsers import XMLOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# output_parser = CommaSeparatedListOutputParser()
# output_parser = XMLOutputParser(
#     tags=['movies', 'movie', 'title', 'year', 'director'],
# )

response_schemas = [
    ResponseSchema(
        name='answer',
        description='提问的回答内容'
    ),
    ResponseSchema(
        name='source',
        description='回答内容的出处网址'
    )
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

instructions = output_parser.get_format_instructions()

print(instructions) 
# Your response should be a list of comma separated values, eg: `foo, bar, baz` or `foo,bar,baz`

prompt_tql = PromptTemplate.from_template(
    template='请返回3个最有代表性的{input}.\n\n{instructions}',
    partial_variables={'instructions': instructions},
)

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
prompt = prompt_tql.format(input="中国电影")

# 按要求输出
output = llm.invoke(prompt).content
print(f'output:{output}, type:{type(output)}')

# 将输出结果通过解析器解析（str->list）
output_format = output_parser.parse(output)
print(f'output_format:{output_format}, type:{type(output_format)}')

# # XML格式化为字典输出
# for movie in output_format['movies']:
#     print(movie)

# 自定义的json格式化输出
for name, value in output_format.items():
    print(f'{name}: {value}')