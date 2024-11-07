from .element import Element
from .root import Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Button(Element):
    
    id: int
    style: str
    name: str = 'nextButton'
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            size: str = "sm",
            color: str = "default",
            on_press: Optional[Callable[['Button'], None]] = None
        ):
        
        self.ui = Shared.ui
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.on_press = on_press
        self.label = label
        self.style = style
        self.size = size
        self.color = color
        
    def update_element(self, data):
        if data['event'] == 'onPress':
            self.on_press(self)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        
        const handleChange{self.id} = (e) => {{
            pywebview.api.update({{id: '{self.id}', event: 'onPress'}});
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
        event_arg = f'onPress={{handleChange{self.id}}}'
        style_arg = f'className={{styleClass{self.id}}}'
        
        return (f'<Button  bridge-id="{self.id}" id="nextButton" {event_arg} {style_arg} {size_arg} {color_arg}>{self.label}</Button >')