import json
import difflib

def load_snippets(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['snippets']

def find_closest_snippets(snippets, keyword):
    matches = difflib.get_close_matches(keyword, [snippet['name'] for snippet in snippets if snippet['name']], n=1, cutoff=0.1)
    if not matches:
        return "No matching snippets found."
    return next((snippet for snippet in snippets if snippet['name'] == matches[0]), "No matching snippets found.")

def format_snippet(snippet):
    formatted = f"Name: {snippet['name']}\nDescription: {snippet.get('description', 'No description')}\n"
    for content in snippet['content']:
        formatted += f"\n{content['label']} ({content['language']}):\n{content['value']}\n"
    return formatted

def main():
    snippets = load_snippets('db.json')  # 确保文件名和路径正确
    while True:
        keyword = input("Enter a keyword to search for code snippets (type 'exit' to quit): ")
        if keyword.lower() == 'exit':
            print("Exiting program.")
            break
        closest_snippet = find_closest_snippets(snippets, keyword)
        if isinstance(closest_snippet, str):
            print(closest_snippet)
        else:
            print(format_snippet(closest_snippet))

if __name__ == '__main__':
    main()
