from .element import Element, Shared

from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Code(Element):
    
    id: int
    style: str
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            color: str = "default"
        ):
        
        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
        
        self.ui = Shared.ui
        self.isSelected = False
        
        self.label = label
        self.style = style
        self.color = color
        
        self.have_js = True
        self.id = str(uuid4()).replace("-","")

    

    def update_element(self, data):
        self.isSelected = data['event']
        if self.on_update != None:
            self.on_update(self)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        
        
        window.updateStyle{self.id} = (newStyle) => {{
            setStyleClass{self.id}(newStyle);
        }};
        
        '''
        return js_code
    
    def set_style(self, style: str = ""):
        self.style = style
        self.ui.webview.win.evaluate_js(f'window.updateStyle{self.id}("{self.style}")')
    
    def render(self):
        color_arg = f'color="{self.color}"'
        style_arg = f'className={{styleClass{self.id}}}'
        return (f'<Code bridge-id="{self.id}" {style_arg} {color_arg}>{self.label}</Code>')