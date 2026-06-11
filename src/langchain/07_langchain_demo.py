from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
model=ChatOllama(model="deepseek-r1:8b",base_url="http://localhost:11434",api_key="dummy")

# 2. 带占位符的标准提示词模板 {query} 为输入变量
prompt = PromptTemplate.from_template(
    """
你是专业AI助手，请认真回答用户问题。
用户问题：{query}
    """
)
chain=prompt|model 
# 3. invoke 传入字典（对应模板里的 {query}）
res = chain.invoke({"query": "解释一下 LangChain 是什么"})
print("同步结果：")
print(res.content)
# 4. stream 流式调用
print("\n流式输出：")
for chunk in chain.stream({"query": "用两句话介绍 Python"}):
    print(chunk.content, end="", flush=True)
# 查看链类型
print(f"\n\n链对象类型：{type(chain)}")