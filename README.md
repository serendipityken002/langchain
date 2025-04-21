### langchain 入门

#### 一、介绍
1. 主要功能
- 将 LLM 与外部数据源进行连接
- 允许与 LLM 进行交互
2. 基础功能
- Models 模型：集成了很多流行的 LLM
- Loader 加载器：从指定源加载数据（文件夹、csv文件、网页等）
- Text Spltters 文本分割：将长文本分割成小块
- Vectorstores 向量数据库：将文本转换为向量存储
- Chains 链式处理：任务一个接一个去做
- Agent 代理：大模型自动选择调用哪个工具

#### 二、实战 
**1 环境准备**
**1.1 安装python环境**
- `conda create -n langchain python=3.9`
- 激活后下载requirements.txt中的包

**1.2 通过Google搜索并返回答案**
- 利用 agent 调用 serpapi 工具
- chat、agent 的调用方式都是使用 invoke 方法
![serpapi](images/serpapi.png)

**1.3 函数调用**
- 无法运行，晚些再看看原因