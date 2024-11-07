from .element import Element
from .root import Shared
from uuid import uuid4

class Tabs(Element):
    def __init__(self,
                style: str = "",
                aria_label: str = "Options"
            ):
        
        self.children = []
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        self.ui = Shared.ui
        
        self.aria_label = aria_label
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
        content = ""
        
        for child in self.children:
            if child.have_js == True:
                rendered_js = child.render_js()
                if not rendered_js in js:
                    js = js + rendered_js + "\n"
                
            res = child.render()
            if type(res) == str:
                content = content + " " + res
            elif type(res) == tuple:
                content = content + " " + res[0]
                if not res[1] in js:
                    js = js + res[1]
            
                
        style_arg = f'className={{styleClass{self.id}}}'
        aria_arg = f'aria-label="{self.aria_label}"'
        return f'<Tabs {style_arg} bridge-id="{self.id}" {aria_arg}> {content} </Tabs>', js