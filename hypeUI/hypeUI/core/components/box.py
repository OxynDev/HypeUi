from .element import Element, Shared
from uuid import uuid4

class Box(Element):
    
    id: int
    
    def __init__(self,
                style: str = "",
            ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.children = []
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        self.ui = Shared.ui
        
        self.style = style


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
        return f'<div {style_arg} bridge-id="{self.id}"> {content} </div>', js