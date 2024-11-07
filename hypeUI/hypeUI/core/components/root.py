from .element import Element
from dataclasses import dataclass

class Shared():
    ui = None

@dataclass(order=True)
class Root(Element):
    
    children: list
    
    def __init__(self, ui):
        Shared.ui = ui
        self.children = []
        self.have_js = False
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    
    def add(self, child):
        self.children.append(child)

    
    def render(self):
        
        js = ""
        content = ""
        
        for child in self.children:
            if child.have_js == True:
                js = js + child.render_js() + "\n"
                
            res = child.render()
            if type(res) == str:
                content = content + " " + res
            elif type(res) == tuple:
                content = content + " " + res[0]
                #js = js + res[1]
        
        return content, js