from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_ollama import ChatOllama
model=ChatOllama(model="deepseek-r1:8b",base_url="http://localhost:11434",api_key="dummy")

#示例模板
example_template=PromptTemplate.from_template("单词:{word},反义词:{antonym}")

#示例的动态数据注入 要求是list内部套字典
examples_data=[
    {"word": "大", "antonym": "小"},
    {"word": "高", "antonym": "低"}
]
few_shot_template=FewShotPromptTemplate(
    example_prompt=example_template, #示例数据的模板
    examples=examples_data, #示例数据
    prefix="告知我单词的反义词,我提供如下示例:", #示例之前的提示词
    suffix="基于前面的示例,请告诉我单词{word}的反义词是什么?", #示例之后的提示词
)