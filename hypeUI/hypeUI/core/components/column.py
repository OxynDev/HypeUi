from .element import Element
from uuid import uuid4

class Column(Element):
    def __init__(self):
        self.children = []
        self.have_js = False
        self.id = str(uuid4()).replace("-","")
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        content = ''.join(child.render() for child in self.children)
        return f"<div>{content}</div>"