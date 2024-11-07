
from hypeUI.hypeUI.hypeui import *

ui = Ui(
    dark_mode=True,
    frameless=True,
    width=1000,
    height=600
)

with Root(ui) as root:

    # TEXT
    with Box(style='rounded-lg p-5 m-2 bg-gradient-to-r from-cyan-500 to-blue-500 max-w-96') as text_box:
        
        switch1 = Text(label='HypeUI', style='text-black font-semibold')
        text_box.add(switch1)
        
    root.add(text_box)
    
    # SWITCH
    with Box(style='rounded-lg p-5 m-2 bg-gradient-to-r from-cyan-500 to-blue-500 max-w-96') as switch_box:
        
        def on_switch(ele: Switch):
            print(ele)
            
        switch1 = Switch(on_update=on_switch)
        switch_box.add(switch1)
        
    root.add(switch_box)
    
ui.run(root)


