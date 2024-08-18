import json
import re

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def find_snippet(data, query):
    snippets = data['snippets']
    matches = []

    for snippet in snippets:
        if re.search(query, snippet['name'], re.IGNORECASE):
            matches.append(snippet)

    return matches

def print_snippet(snippet):
    print(f"名称: {snippet['name']}")
    print(f"描述: {snippet['description']}")
    print("内容:")
    for content in snippet['content']:
        print(f"  语言: {content['language']}")
        print(f"  代码:\n{content['value']}\n")

def main():
    data = load_json_data('db.json')

    while True:
        query = input("请输入要查找的代码片段名称 (输入 'q' 退出): ")
        if query.lower() == 'q':
            break

        matches = find_snippet(data, query)

        if not matches:
            print("未找到匹配的代码片段。")
        elif len(matches) == 1:
            print_snippet(matches[0])
        else:
            print(f"找到 {len(matches)} 个匹配的代码片段:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match['name']}")
            choice = input("请选择要查看的代码片段编号 (输入 '0' 取消): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                print_snippet(matches[int(choice) - 1])

if __name__ == "__main__":
    main()