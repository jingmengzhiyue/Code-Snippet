import json
from difflib import get_close_matches

# 读取 JSON 数据
def load_data():
    # 使用 'utf-8' 编码打开文件
    with open('db.json', 'r', encoding='utf-8') as file:
        return json.load(file)

data = load_data()

# 函数来搜索代码片段
def find_snippet(snippets_data, snippet_name):
    snippets = snippets_data['snippets']
    snippet_names = {snippet['name']: snippet for snippet in snippets}

    # 找到最接近的匹配项
    close_matches = get_close_matches(snippet_name, snippet_names.keys(), n=1, cutoff=0.5)
    
    if not close_matches:
        return "No matching snippet found."
    
    # 获取最匹配的片段
    best_match_name = close_matches[0]
    best_match_snippet = snippet_names[best_match_name]['content'][0]['value']
    
    return best_match_snippet

# 服务器主循环
def server_loop():
    while True:
        snippet_name = input("Enter the name of the snippet to search (type 'exit' to quit): ")
        if snippet_name.lower() == 'exit':
            print("Exiting the service...")
            break
        result = find_snippet(data, snippet_name)
        print("Snippet Content:\n" + result)

# 运行服务
server_loop()
