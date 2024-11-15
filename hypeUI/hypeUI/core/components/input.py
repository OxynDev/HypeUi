from .element import Element, Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Input(Element):
    
    id: int
    style: str
    name: str = 'nextInput'
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            input_type: str = "",
            default_value: str = "",
            placeholder: str = "",
            variant: str = "default",
            color: str = "default",
            is_required: bool = False,
            on_change: Optional[Callable[['Input'], None]] = None
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        self.isSelected = False
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.variant = variant
        self.placeholder = placeholder
        self.is_required = is_required
        self.default_value = default_value
        self.input_type = input_type
        self.on_change = on_change
        self.label = label
        self.style = style
        self.color = color
        self.value = self.default_value
        
        
    def update_element(self, data):
        self.value = data['event']
        if self.on_change != None:
            self.on_change(self)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        
        const handleChange{self.id} = (e) => {{
            pywebview.api.update({{id: '{self.id}', event: e.target.value}});
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
        event_arg = f'onChange={{handleChange{self.id}}}'
        style_arg = f'className={{styleClass{self.id}}}'
        value_arg = f'defaultValue="{self.default_value}"'
        placeholder_arg = f'placeholder="{self.placeholder}"'
        variant_arg = f'variant="{self.variant}"'
        
        if self.input_type != "": type_arg = f'type="{self.input_type}"'
        else: type_arg = ""
        
        if self.is_required: required_arg = f'isRequired'
        else: required_arg = ""
        
        label_var = f'label="{self.label}"'
        
        return (f'<Input bridge-id="{self.id}" id="nextInput" {variant_arg} {event_arg} {placeholder_arg} {label_var} {required_arg} {style_arg} {color_arg} {value_arg} {type_arg}></Input>')