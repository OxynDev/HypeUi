from .element import Element
from .root import Shared
from uuid import uuid4

class Box(Element):
    def __init__(self,
                style: str = "",
            ):
        self.children = []
        self.have_js = False
        self.id = str(uuid4()).replace("-","")
        self.ui = Shared.ui
        self.style = style
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def add(self, child):
        self.children.append(child)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        
        window.updateStyle{self.id} = (newStyle) => {{
            setStyleClass{self.id}(newStyle);
        }};
        
        '''
        for child in self.children:
            if child.have_js == True:
                js_code = js_code + child.render_js() + "\n"
        return js_code

    def set_style(self, style: str = ""):
        self.style = style
        self.ui.webview.win.evaluate_js(f'window.updateStyle{self.id}("{self.style}")')
    
    def render(self):
        
        js = ""
        for child in self.children:
            if child.have_js == True:
                js = js + child.render_js() + "\n"
   
        content = ''.join(child.render() for child in self.children)
        style_arg = f'className={{styleClass{self.id}}}'
        return f'<div {style_arg} bridge-id="{self.id}"> {content} </div>', js