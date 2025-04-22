from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredFileLoader
from langchain.document_loaders import JSONLoader

# # CSV加载器
# loader = CSVLoader(
#     'Data_Connection\data\demo.csv',
#     encoding='utf-8',
#     source_column='姓名', # 选择指定的列数据作为文档对象的metadata部分
# )

# for doc in loader.load():
#     print(doc)

# # 目录加载器
# loader = DirectoryLoader(
#     'Data_Connection',
#     glob='**/*.md',
# )

# for doc in loader.load():
#     print(doc)

# # HTML加载器
# loader = UnstructuredFileLoader(
#     'Data_Connection\data\demo.html',
# )

# for doc in loader.load():
#     print(doc)

# # JSON加载器
loader = JSONLoader(
    'Data_Connection\data\demo.json',
    jq_schema='.sum[].name' # 指定解析方式，sum键内是一个列表，取出每个列表内的name键的内容
)

for doc in loader.load():
    print(doc)