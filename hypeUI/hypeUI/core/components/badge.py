from .element import Element, Shared
from uuid import uuid4
from typing import Callable, Optional

class Badge(Element):
    
    id: int
    
    def __init__(self,
                style: str = "",
                text: str = "",
                color: str = "primary",
                size: str = "md",
                variant: str = "solid"
            ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.children = []
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        self.ui = Shared.ui
        
        self.variant = variant
        self.size = size
        self.color = color
        self.text = text
        self.style = style

    def update_element(self, data):
        pass
            
    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        const [content{self.id}, setContent{self.id}] = useState("{self.text}");
        
        window.updateStyle{self.id} = (newStyle) => {{
            setStyleClass{self.id}(newStyle);
        }};

        window.updateContent{self.id} = (newContent) => {{
            setContent{self.id}(newContent);
        }};
    
        '''
        for child in self.children:
            if child.have_js == True:
                js_code = js_code + child.render_js() + "\n"
        return js_code

    def set_style(self, style: str = ""):
        self.style = style
        self.ui.webview.win.evaluate_js(f'window.updateStyle{self.id}("{self.style}")')

    def set_content(self, text: str):
        self.text = text
        self.ui.webview.win.evaluate_js(f'window.updateContent{self.id}("{self.text}")')
        
    def render(self):
        
        js = ""
        content_ = ""
        
        for child in self.children:
            if child.have_js == True:
                rendered_js = child.render_js()
                if not rendered_js in js:
                    js = js + rendered_js + "\n"
                
            res = child.render()
            if type(res) == str:
                content_ = content_ + " " + res
            elif type(res) == tuple:
                content_ = content_ + " " + res[0]
                if not res[1] in js:
                    js = js + res[1]
        

        style_arg = f'className={{styleClass{self.id}}}'
        content_arg = f'content={{content{self.id}}}'
        color_arg = f'color="{self.color}"'
        size_arg = f'size="{self.size}"'
        variant_arg = f'variant="{self.variant}"'
        
        return f"""<Badge {content_arg} {color_arg} {size_arg} {variant_arg} bridge-id="{self.id}" {style_arg} >
        {content_}
        </Badge>""", js