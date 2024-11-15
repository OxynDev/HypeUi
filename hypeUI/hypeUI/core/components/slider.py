from .element import Element, Shared

from typing import Callable
from uuid import uuid4
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(order=True)
class Slider(Element):
    
    id: int
    style: str
    name: str = 'nextSlider'
    
    def __init__(self, 
            label: str = "", 
            style: str = "",
            size: str = "sm",
            max_value: float = 100,
            min_value: float = 1,
            step: float = 1,
            color: str = "default",
            default_value: float = 30,
            on_change: Optional[Callable[['Slider'], None]] = None
        ):

        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self)
            
        self.ui = Shared.ui
        
        self.have_js = True
        self.id = str(uuid4()).replace("-","")
        
        self.on_change = on_change
        self.value = default_value
        self.max_value = max_value
        self.min_value = min_value
        self.step = step
        self.label = label
        self.style = style
        self.size = size
        self.color = color

    def update_element(self, data):
        print(data)
        self.value = data['value']
        if self.on_change != None:
            self.on_change(self)

    def render_js(self):
        js_code = f'''
        const [styleClass{self.id}, setStyleClass{self.id}] = useState("{self.style}");
        const [value{self.id}, setValue{self.id}] = useState({self.value});

        const handleSliderChange{self.id} = (e) => {{
            pywebview.api.update({{id: '{self.id}', value: e}});
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
        label_arg = f'label="{self.label}"' 
        style_arg = f'className={{styleClass{self.id}}}'
        
        step_arg = f'step={{{self.step}}}' 
        max_arg = f'maxValue={{{self.max_value}}}' 
        min_arg = f'minValue={{{self.min_value}}}' 
        value_arg = f'defaultValue={{{self.value}}} onChangeEnd={{handleSliderChange{self.id}}}'
        
        return (f'<Slider bridge-id="{self.id}" id="{self.name}" {value_arg} {min_arg} {max_arg} {step_arg} {label_arg} {style_arg} {size_arg} {color_arg}></Slider>')