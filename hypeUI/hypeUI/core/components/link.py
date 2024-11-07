from .element import Element
from .root import Shared

from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Link(Element):
    
    id: int
    style: str
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            href: str = ""
        ):
        
        self.ui = Shared.ui
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.label = label
        self.style = style
        self.href = href
    

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
        style_arg = f'className={{styleClass{self.id}}}'
        href_arg = f'href="{self.href}"'
        
        return (f'<Link bridge-id="{self.id}" {style_arg} {href_arg}>{self.label}</Link>')