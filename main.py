import json

d={"name":"周杰伦","age":44,"gender":"男"}
json_str='{"name": "周杰", "age": 44,"gender": "男"}'

def json_to_dict(json_str):
    #将json字符串转换为字典
    return json.loads(json_str)
def main():
    print("Hello from studyagent2!")
    #将字典转换为json字符串
    s= json.dumps(d,ensure_ascii=False)
    print(s)


if __name__ == "__main__":
    json_dict = json_to_dict(json_str)
    print(json_dict)
    main()
    
