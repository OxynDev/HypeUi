
from hypeUI.hypeUI.hypeui import *

PRODUCTION = False

ui = Ui(
    dark_mode=True,
    frameless=True,
    width=1000,
    height=600
)

if PRODUCTION == False:
    development_svg = []
    
    svg_moon = open("moon.jsx","r").read()
    
    development_svg.append([
        svg_moon, # Svg jsx
        'MoonIcon' # import name
    ])

    
    

ui.set_global_css("""
#nextSwitch > .text-foreground {
    color: black;
}
""")

box_css = 'flex flex-row justify-between rounded-lg p-2 m-2 bg-gradient-to-r from-cyan-500 to-blue-500 items-center'


with Root(ui) as root:
    
    with Box(style='flex flex-row gap-4 bg-slate-900 rounded-lg p-1 m-2') as text_box:
        Text(label='HypeUI', style='font-semibold text-xl pl-1')
        Text(label='0.0', style='text-xl text-slate-400 mt-auto')
    
    with Tabs(style='m-2') as tabs:
        
        with Tab(key='components', title='components') as tab_1:

            def on_click(ele: Box):
                print(ele)
                
            # TEXT
            with Box(style=box_css, on_click=on_click) as text_box:
                text = Text(label='Text', style='text-black font-semibold')
                code = Snippet(label="Text()")
            
            # BUTTON
            with Box(style=box_css) as button_box:
                def on_press(ele: Button):
                    print(ele)
                button = Button(label='HypeUI', on_press=on_press, variant='shadow', style='font-semibold', end_content='MoonIcon')
                code = Snippet(label="Button()")

            # SWITCH
            with Box(style=box_css) as switch_box:
                def on_switch(ele: Switch):
                    print(ele.isSelected, ele)
                switch = Switch(label='Switch', on_update=on_switch, size='sm', color='success')
                code = Snippet(label="Switch()")

            # CARD
            with Box(style=box_css) as card_box:
                with Card() as card:
                    with CardBody() as cardbody:
                        text = Text(label='Card', style='font-semibold')
                code = Snippet(label="Card(), CardBody()")

            # LINK
            with Box(style=box_css) as link_box:
                with Card() as card:
                    with CardBody() as cardbody:
                        link = Link(label='Github', show_anchor_icon=True ,href='https://github.com/OxynDev/HypeUi')
                code = Snippet(label="Link()")

            # INPUT
            with Box(style=box_css) as card_box:
                def on_change(ele: Input):
                    print(ele.value)
                Input(on_change=on_change, label='Input', placeholder='Enter text', style='w-30')
                code = Snippet(label="Input()")

            # SVG
            with Box(style=box_css) as text_box:
                def on_click(ele: Svg):
                    print(ele)
                with Card() as card:
                    with CardBody() as cardbody:
                        text = Svg(svg='MoonIcon', on_click=on_click)
                code = Snippet(label="Svg()")

        with Tab(key='github', title='github') as tab_2:
            with Box(style=box_css) as text_box:
                text = Text(label='https://github.com/OxynDev/HypeUi', style='text-black font-semibold')

        

ui.run(
    root=root,
    production=PRODUCTION,
    svg_list=development_svg
)


