from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
model=ChatOllama(model="deepseek-r1:8b",base_url="http://localhost:11434",api_key="dummy")
prompt_template=PromptTemplate.from_template("我的邻居姓{lastname},刚生了{gender},你帮我起个名字,简单回答")
#调用.format方法注入信息
#prompt_text=prompt_template.format(lastname="张",gender="女儿")
#res=model.invoke(input=prompt_text)
#print(res.content)
chain=prompt_template|model
res=chain.invoke(input={"lastname":"张","gender":"女"})
print(res)