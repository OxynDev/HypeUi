from .element import Element, Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Progress(Element):
    
    id: int
    style: str
    name: str = 'nextProgress'
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            size: str = "sm",
            color: str = "default",
            default_value: float = 0,
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.value = default_value
        self.label = label
        self.style = style
        self.size = size
        self.color = color

    def update_element(self, data):
        pass

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        const [value{self.id}, setValue{self.id}] = useState({self.value});

        window.updateValue{self.id} = (newValue) => {{
            setValue{self.id}(newValue);
        }};
        
        window.updateStyle{self.id} = (newStyle) => {{
            setStyleClass{self.id}(newStyle);
        }};
        
        '''
        return js_code
    
    def set_style(self, style: str = ""):
        self.style = style
        self.ui.webview.win.evaluate_js(f'window.updateStyle{self.id}("{self.style}")')

    def set_value(self, value: float):
        self.value = value
        self.ui.webview.win.evaluate_js(f'window.updateValue{self.id}({self.value})')
        
    def render(self):
        color_arg = f'color="{self.color}"'
        size_arg  = f'size="{self.size}"'
        label_arg = f'label="{self.label}"' 
        style_arg = f'className={{styleClass{self.id}}}'
        value_arg = f'value={{value{self.id}}}'
        
        return (f'<Progress bridge-id="{self.id}" id="{self.name}" {value_arg} {label_arg} {style_arg} {size_arg} {color_arg}></Progress>')