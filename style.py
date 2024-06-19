from abc import ABC, abstractmethod
import json

# 风格接口（抽象产品）
class Style(ABC):
    @abstractmethod
    def render(self, data):
        pass

# 树形风格（具体产品）
class TreeStyle(Style):
    def render(self, data):
        self.print_tree(data)
        
    # 树状结构输出函数
    def print_tree(self,data, level=0):
        if isinstance(data, dict):
            for key, value in data.items():
                # 检查是否是最后一个键
                last_key = key == list(data.keys())[-1]
                connector = "└─" if last_key else "├─"
                print(f"{'│   ' * level}{connector} {key}")
                self.print_tree(value, level + 1)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                # 检查是否是列表中的最后一个元素
                last_item = i == len(data) - 1
                connector = "   " if last_item else "├──"
                print(f"{'│   ' * level}{connector} {item}")
                self.print_tree(item, level + 1)


# 风格工厂接口（抽象工厂）
class StyleFactory(ABC):
    @abstractmethod
    def create_style(self):
        pass

# 树形风格工厂（具体工厂）
class TreeStyleFactory(StyleFactory):
    def create_style(self):
        return TreeStyle()

# 矩形风格工厂（具体工厂）
class RectangleStyleFactory(StyleFactory):
    def create_style(self):
        pass
    
class JsonStyleConverter:
    def __init__(self, style_factory: StyleFactory):
        self.style = style_factory.create_style()

    def convert_json_to_style(self, json_data):
        # 假设我们有一个函数来解析JSON数据，并准备渲染
        # 这里我们只是简单地将JSON数据传递给风格对象进行渲染
        self.style.render(json_data)


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
# 使用示例
if __name__ == "__main__":
    # 选择风格工厂
    tree_style_factory = TreeStyleFactory()

    # 创建转换器实例
    converter_tree_style = JsonStyleConverter(tree_style_factory)

    file_path = 'a.json'
    data = read_json_file(file_path)

    # 转换并应用树形风格
    converter_tree_style.convert_json_to_style(data)
