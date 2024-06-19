from style import *
import sys
import re

def extract_from_string(input_str):
    pattern = r'-f\s+(\S+)\s+-s\s+(\S+)'
    match = re.search(pattern, input_str)
    
    if match:
        json_file_path = match.group(1)
        style_name = match.group(2)
        return json_file_path, style_name
    else:
        return None, None

if __name__ == "__main__":
    input_str=input()
    json_file_path, style_name = extract_from_string(input_str)
                
    if json_file_path is None:
        print("empty file")
        exit(0)
    elif style_name is None:
        print("empty style")
        exit(0)


    if style_name=="tree":
        tree_style_factory = TreeStyleFactory()
        converter_tree_style = JsonStyleConverter(tree_style_factory)
        data = read_json_file(json_file_path)
        converter_tree_style.convert_json_to_style(data)
    else:
        print("invalid style")

