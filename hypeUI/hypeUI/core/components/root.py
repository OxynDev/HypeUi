from .element import Element, Shared
from dataclasses import dataclass



@dataclass(order=True)
class Root(Element):
    
    children: list
    
    def __init__(self, ui):
        Shared.ui = ui
        self.children = []
        self.have_js = False
        
        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
    
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