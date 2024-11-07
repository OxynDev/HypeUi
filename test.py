
from hypeUI.hypeUI.hypeui import *

ui = Ui(
    dark_mode=True,
    frameless=True,
    width=1000,
    height=600
)

ui.set_global_css("""
#nextSwitch > .text-foreground {
    color: black;
}
""")

box_css = 'flex flex-row justify-between rounded-lg p-5 m-2 bg-gradient-to-r from-cyan-500 to-blue-500 items-center'

with Root(ui) as root:

    with Tabs(style='m-2') as tabs:
        
        with Tab(key='components', title='components') as tab_1:
            
            # TEXT
            with Box(style=box_css) as text_box:
                
                text = Text(label='HypeUI', style='text-black font-semibold')
                code = Snippet(label="Text(label='HypeUI', style='text-black font-semibold')")

                text_box.add(text)
                text_box.add(code)
            
            tab_1.add(text_box)

            # BUTTON
            with Box(style=box_css) as button_box:

                def on_press(ele: Button):
                    print(ele)
                    
                button = Button(label='HypeUI', on_press=on_press, style='font-semibold')
                code = Snippet(label="Button(label='HypeUI', on_press=on_press, style='font-semibold')")

                button_box.add(button)
                button_box.add(code)
            
            tab_1.add(button_box)
            
            # SWITCH
            with Box(style=box_css) as switch_box:
                
                def on_switch(ele: Switch):
                    print(ele.isSelected, ele)
                    
                switch = Switch(label='Switch', on_update=on_switch, size='sm', color='success')
                code = Snippet(label="Switch(label='Switch', on_update=on_switch, size='sm', color='success')")
                
                switch_box.add(switch) 
                switch_box.add(code)
            
            tab_1.add(switch_box)

            # LINK
            with Box(style=box_css) as link_box:

                link = Link(label='Github',href='https://github.com/OxynDev/HypeUi')
                code = Snippet(label="Link(label='Github',href='https://github.com/OxynDev/HypeUi')")
                
                link_box.add(link) 
                link_box.add(code)
            
            tab_1.add(link_box)

            # CARD
            with Box(style=box_css) as card_box:
                
                with Card() as card:
                    with CardBody() as cardbody:
                        text = Text(label='Card', style='font-semibold')
                        cardbody.add(text)
                    card.add(cardbody)
                    
                code = Snippet(label="with Card() as card: with CardBody() as cardbody:")
                
                card_box.add(card)
                card_box.add(code)
                        
            tab_1.add(card_box)
            
        tabs.add(tab_1)

        with Tab(key='github', title='github') as tab_2:
            
            with Box(style=box_css) as text_box:
                
                text = Text(label='https://github.com/OxynDev/HypeUi', style='text-black font-semibold')

                text_box.add(text)
            
            tab_2.add(text_box)

        tabs.add(tab_2)
        
    root.add(tabs)
    
ui.run(root)


