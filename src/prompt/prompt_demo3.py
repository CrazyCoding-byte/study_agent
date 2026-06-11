# 正确导入
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 初始化本地 Ollama 模型
llm = ChatOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy",
    model="deepseek-r1:8b"
)

# 模板定义
template = '你是一个{role},请用{style}风格回答问题：{question}'
prompt = PromptTemplate.from_template(template)

# 链式调用（LangChain 主流用法）
chain = prompt | llm

# 执行请求
result = chain.invoke({
    "role": "数学老师",
    "style": "通俗易懂",
    "question": "勾股定理是什么？"
})

print(result.content)