import webview

from . import api

class Web:
    def __init__(self, root):
        self.root = root
        self.win = None
        
    def run(self,
            html: str
        ):
        
        self.win = webview.create_window('HypeUi', html=html, js_api=api.Api(self.root))
        webview.start(user_agent='hypeUI', debug=True)


