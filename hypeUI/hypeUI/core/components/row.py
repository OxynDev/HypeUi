from .element import Element
from uuid import uuid4

class Row(Element):
    def __init__(self):
        self.children = []
        self.have_js = False
        self.id = str(uuid4()).replace("-","")
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def add(self, child):
        self.children.append(child)

    def render_js(self):
        js = ""
        for child in self.children:
            if child.have_js == True:
                js = js + child.render_js() + "\n"
        return js
    
    def render(self):
        
        js = ""
        for child in self.children:
            if child.have_js == True:
                js = js + child.render_js() + "\n"
   
        content = ''.join(child.render() for child in self.children)
        return f"<div>{content}</div>", js