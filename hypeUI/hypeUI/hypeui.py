from .core import web, node

from .core.components.root import Root
from .core.components.row import Row
from .core.components.column import Column
from .core.components.switch import Switch
from .core.components.element import get_imports



class Ui:
    def __init__(self):
        self.project = node.Project()
        self.webview = None
        
    def set_root(self, root_element):
        self.root = root_element

    def render(self):
        if not self.root:
            return ""
        html_output = self.root.render()
        js_output = self.root.render_js()
        return [html_output, js_output]


    def run(self, 
            root,
            imports: str,
            production: bool = False
            ):
        
        render = root.render()
        html = render[0]
        js = render[1]
        if production == False:
            one_file = self.project.process(html, imports, js)
        else:
            one_file = ""
            
        self.webview = web.Web(root=root)
        self.webview.run(html=one_file)