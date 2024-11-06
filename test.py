
from hypeUI.hypeUI.hypeui import *

ui = Ui()

with Root(ui) as root:

    with Row() as switch_box:
        
        def on_switch(ele):
            print(ele.set_style("hidden"))
        
        switch1 = Switch('Email verify', on_update=on_switch)
        
        switch_box.add(switch1)
        
        switch_box.add(Switch('Chat access'))
        switch_box.add(Switch('Custom name'))
        switch_box.add(Switch('Avatar changer'))
        switch_box.add(Switch('Bio changer'))
     
    root.add(switch_box)

ui.run(root, get_imports())


