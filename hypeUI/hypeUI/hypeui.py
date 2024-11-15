
from .core import web, node

from .core.components.root import Root
from .core.components.box import Box
from .core.components.text import Text
from .core.components.switch import Switch
from .core.components.code import Code
from .core.components.snippet import Snippet
from .core.components.button import Button
from .core.components.tabs import Tabs
from .core.components.tab import Tab
from .core.components.link import Link
from .core.components.card import Card
from .core.components.cardbody import CardBody
from .core.components.input import Input
from .core.components.html import Html
from .core.components.svg import Svg
from .core.components.slider import Slider
from .core.components.progress import Progress
from .core.components.image import Image
from .core.components.divider import Divider
from .core.components.tooltip import Tooltip
from .core.components.badge import Badge
from .core.components.checkbox import Checkbox

from .core.components.element import get_imports



class Ui:
    def __init__(self,
                 dark_mode: bool = True,
                 frameless: bool = False,
                 height: int = None,
                 width: int = None
                 
                 ):
        
        """
        hypeUI is a Python library for building beautiful user interfaces with React and NextUI.
        args:
            dark_mode: bool = True
                Set the dark mode for the UI.
            frameless: bool = False
                Set the frameless mode for the UI.
            height: int = None
                Set the height of the UI.
            width: int = None
                Set the width of the UI.
        """
        
        self.project = node.Project()
        self.webview = None 
        
        self.width = width
        self.height = height
        self.frameless = frameless
        self.dark_mode = dark_mode
        self.css = ""
    
    
    
    def set_global_css(self, css: str = ""):
        self.css = css

    def render(self):
        if not self.root:
            return ""
        html_output = self.root.render()
        js_output = self.root.render_js()
        return [html_output, js_output]

    def set_dark_mode(self, dark_mode: bool = True):
        self.webview.set_dark_mode(dark_mode=dark_mode)
    
    def run(self, 
            root: Root,
            production: bool = False,
            svg_list: list = None
            ):
        
        render = root.render()
        html = render[0]
        js = render[1]
        
        settings = {
            "dark_mode": self.dark_mode,
            "frameless": self.frameless,
            "height": self.height,
            "width": self.width
        }
        
        if production == False:
            one_file = self.project.process(html, get_imports(), js, self.css, svg_list)
        else:
            one_file = ""
            
        self.webview = web.Web(root=root, settings=settings)
        self.webview.run(html=one_file)
        

