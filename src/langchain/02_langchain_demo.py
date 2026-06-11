from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
#得到模型对象 使用chatOllama不需要写v1
model=ChatOllama(model="deepseek-r1:8b",base_url="http://localhost:11434",api_key="dummy")
#准备消息列表
messages= [
    SystemMessage(content="你是数学老师,请以通俗易懂的方式回答问题"),
    HumanMessage(content="勾股定理是什么？"),
    AIMessage(content="勾股定理是一个数学定理，描述了在一个直角三角形中，斜边的平方等于两条直角边的平方和。换句话说，如果一个三角形的两条直角边分别是a和b，斜边是c，那么就有a² + b² = c²。这个定理在几何学中非常重要，常用于计算距离、设计建筑等领域。"),
    HumanMessage(content="能不能举个例子？")
]

#调用stream流式执行
res=model.stream(input=messages)
#for循环迭代打印输出,通过.content获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
