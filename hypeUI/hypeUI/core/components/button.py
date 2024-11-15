from .element import Element, Shared

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
            variant: str = "default",
            start_content: str = None,
            end_content: str = None,
            is_disabled: bool = False,
            on_press: Optional[Callable[['Button'], None]] = None
            
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.start_content = start_content
        self.end_content = end_content
        self.variant = variant
        self.on_press = on_press
        self.label = label
        self.style = style
        self.size = size
        self.color = color
        self.is_disabled = is_disabled
        
    def set_disabled(self, is_disabled: bool):
        self.is_disabled = is_disabled
        self.ui.webview.win.evaluate_js(f'window.setDisabled{self.id}({str(is_disabled).lower()})')
        
    def update_element(self, data):
        if data['event'] == 'onPress':
            if self.on_press != None:
                self.on_press(self)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        const [isDisabled{self.id}, setIsDisabled{self.id}] = useState(false);


        const handleChange{self.id} = (e) => {{
            pywebview.api.update({{id: '{self.id}', event: 'onPress'}});
        }};
        
        window.updateStyle{self.id} = (newStyle) => {{
            setStyleClass{self.id}(newStyle);
        }};

        window.setDisabled{self.id} = (isDisabled) => {{
            setIsDisabled{self.id}(isDisabled);
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
        variant_arg = f'variant="{self.variant}"'

        if self.end_content: end_content = f"endContent={{<{self.end_content}/>}}"
        else: end_content = ""

        if self.start_content: start_content = f"startContent={{<{self.start_content}/>}}"
        else: start_content = ""
        
        disabled_arg = f'isDisabled={{isDisabled{self.id}}}'
        
        return (f'<Button bridge-id="{self.id}" id="{self.name}" {disabled_arg} {start_content} {end_content} {variant_arg} {event_arg} {style_arg} {size_arg} {color_arg}>{self.label}</Button >')