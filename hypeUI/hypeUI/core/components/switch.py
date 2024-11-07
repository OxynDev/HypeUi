from .element import Element, Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Switch(Element):
    
    id: int
    style: str
    name: str = 'nextSwitch'
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            size: str = "sm",
            color: str = "default",
            on_update: Optional[Callable[['Switch'], None]] = None
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        self.isSelected = False
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.on_update = on_update
        self.label = label
        self.style = style
        self.size = size
        self.color = color
        
    def update_element(self, data):
        self.isSelected = data['event']
        if self.on_update != None:
            self.on_update(self)

    def render_js(self):
        js_code = f'''
        const [isChecked{self.id}, setIsChecked{self.id}] = useState(false);
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        
        const handleChange{self.id} = (e) => {{
            setIsChecked{self.id}(e.target.checked);
            pywebview.api.update({{id: '{self.id}', event: e.target.checked}});
        }};
        
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
        size_arg  = f'size="{self.size}"'
        event_arg = f'onChange={{handleChange{self.id}}}'
        style_arg = f'className={{styleClass{self.id}}}'
        
        return (f'<Switch bridge-id="{self.id}" id="nextSwitch" {event_arg} {style_arg} {size_arg} {color_arg}>{self.label}</Switch>')