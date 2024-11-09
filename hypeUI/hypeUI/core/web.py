import webview
import asyncio

from . import api



class Web:
    def __init__(self, 
                 root,
                 settings: dict
                 ):
        
        self.settings = settings
        self.root = root
        self.win = None

    async def init_win(self):
        print("WebView started")
        self.set_dark_mode(self.settings['dark_mode'])
    
    async def tasks(self):
        await asyncio.create_task(self.init_win())
        
    def loaded(self):
        asyncio.run(self.tasks())
    
    def set_dark_mode(self, 
                      dark_mode: bool = False
                    ):
        if dark_mode == True:
            self.win.evaluate_js("window.setTheme('dark');")
    
    def run(self,
            html: str
        ):
        
        self.win = webview.create_window('HypeUi', 
                                        html=html, 
                                        js_api=api.Api(self.root), 
                                        frameless=self.settings['frameless'],
                                        width=self.settings['width'],
                                        height=self.settings['height']
                                    )

        self.win.events.loaded += self.loaded
        
        
        webview.start(user_agent='hypeUI', debug=True)


