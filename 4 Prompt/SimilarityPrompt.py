import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./api_key.env")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_KEY")

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import MaxMarginalRelevanceExampleSelector
from langchain.prompts import PromptTemplate, FewShotPromptTemplate

examples = [
    {'input' : 'happy', 'output' : 'sad'},
    {'input' : 'good', 'output' : 'bad'},
    {'input' : 'fast', 'output' : 'slow'},
    {'input' : 'big', 'output' : 'small'},
    {'input' : 'hot', 'output' : 'cold'},
    {'input' : 'young', 'output' : 'old'},
    {'input' : 'rich', 'output' : 'poor'},
    {'input' : 'strong', 'output' : 'weak'},
]

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,
    embeddings=OpenAIEmbeddings(openai_api_base="https://api.chatanywhere.tech/v1"),
    vectorstore_cls=Chroma,
    k=2
)

example_prompt = PromptTemplate.from_template(
    '{input}的反义词是{output}'
)

prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    prefix="请学习examples并回答问题",
    example_prompt=example_prompt,
    suffix="请问{input}的反义词是什么？",
    input_variables=["input"],
)

print(prompt.format(input="suuny"))