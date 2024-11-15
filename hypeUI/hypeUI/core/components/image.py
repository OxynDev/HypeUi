from .element import Element, Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Image(Element):
    
    id: int
    style: str
    name: str = 'nextImage'
    
    def __init__(self, 
            src: str = "", 
            alt: str = "",
            style: str = "",
            is_blurred: bool = False,
            on_press: Optional[Callable[['Image'], None]] = None
            
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.is_blurred = is_blurred
        self.alt = alt
        self.on_press = on_press
        self.src = src
        self.style = style
        
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
        event_arg = f'onPress={{handleChange{self.id}}}'
        style_arg = f'className={{styleClass{self.id}}}'
        src_arg = f'src="{self.src}"'
        alt_arg = f'alt="{self.alt}"'
        arg_blurred = f'isBlurred={{{str(self.is_blurred).lower()}}}'
        
        return (f'<Image bridge-id="{self.id}" id="{self.name}" {arg_blurred} {src_arg} {alt_arg} {event_arg} {style_arg} ></Image >')