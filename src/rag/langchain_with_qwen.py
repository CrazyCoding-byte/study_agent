from langchain_community.llms.tongyi import Tongyi
model=Tongyi(model="qwen3:4b", temperature=0.2, max_tokens=2048)
res=model.invoke("请介绍一下你自己。")
print(res)  