from .element import Element

class Shared():
    ui = None

class Root(Element):
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
            x = child.render() 
            content = content + x[0] + "\n"
            js = js + child.render_js() + "\n"
   
        return content, js