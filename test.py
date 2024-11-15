
from hypeUI.hypeUI.hypeui import *
import time

PRODUCTION = False

ui = Ui(
    dark_mode=True,
    frameless=False,
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

    
# div[data-slot="tabList"] {
#     display: none;
# }
# Hide tabs

ui.set_global_css("""
#nextSwitch > .text-foreground {
    color: black;
}

""")

box_css = 'flex flex-row justify-between rounded-lg p-2 m-2 bg-gradient-to-r from-cyan-500 to-blue-500 items-center'


with Root(ui) as root:
    
    with Box(style='flex flex-row gap-4 bg-slate-900 rounded-lg p-1 m-2'):
        Text(label='HypeUI', style='font-semibold text-xl pl-1')
        Text(label='0.0', style='text-xl text-slate-400 mt-auto')
    
    with Tabs(style='m-2', 
              #selected_key='components'
              ) as tabs:
        
        with Tab(key='components', title='components') as tab_1:

            def on_click(ele: Box):
                print(ele)
                #tabs.set_selected_key('github')
                
                
            # TEXT
            with Box(style=box_css, on_click=on_click):
                text = Text(label='Text', style='text-black font-semibold')
                code = Snippet(label="Text()")
            
            # BUTTON
            with Box(style=box_css):
                def on_press(ele: Button):
                    print(ele)
                button = Button(label='HypeUI', on_press=on_press, variant='shadow', style='font-semibold', end_content='MoonIcon')
                code = Snippet(label="Button()")

            # SWITCH
            with Box(style=box_css):
                def on_switch(ele: Switch):
                    print(ele.is_selected, ele)
                switch = Switch(label='Switch', default_selected=True, on_update=on_switch, size='sm', color='success')
                code = Snippet(label="Switch()")

            # CARD
            with Box(style=box_css):
                with Card():
                    with CardBody():
                        text = Text(label='Card', style='font-semibold')
                code = Snippet(label="Card(), CardBody()")

            # LINK
            with Box(style=box_css):
                with Card():
                    with CardBody():
                        link = Link(label='Github', show_anchor_icon=True ,href='https://github.com/OxynDev/HypeUi')
                code = Snippet(label="Link()")

            # INPUT
            with Box(style=box_css):
                def on_change(ele: Input):
                    print(ele.value)
                Input(on_change=on_change, label='Input', placeholder='Enter text', style='w-30')
                code = Snippet(label="Input()")

            # SVG
            with Box(style=box_css):
                def on_click(ele: Svg):
                    print(ele)
                with Card():
                    with CardBody():
                        text = Svg(svg='MoonIcon', on_click=on_click)
                code = Snippet(label="Svg()")

            # SLIDER
            with Box(style=box_css):
                def on_change(ele: Slider):
                    print(ele.value)
                    #time.sleep(0.3)
                    #ele.set_value(30)
                    
                with Card(style='w-32'):
                    with CardBody(style='w-32'):
                        slider = Slider(label="Slider", max_value=100.0, min_value=1.0, default_value=1.0, step=1.0, on_change=on_change)
                code = Snippet(label="Slider()")

            # PROGRESS
            with Box(style=box_css):
                with Card(style='w-32'):
                    with CardBody(style='w-32 flex flex-column gap-3'):
                        slider = Progress(label="Loading",default_value=0)
                        def on_press(ele: Button):
                            ele.set_disabled(True)
                            for i in range(100):
                                slider.set_value(i)
                                time.sleep(0.05)
                            time.sleep(3)
                            slider.set_value(0)
                            ele.set_disabled(False)
                        button = Button(label='Load', on_press=on_press, variant='shadow', style='font-semibold')
                code = Snippet(label="Progress()")

            # IMAGE
            with Box(style=box_css):
                with Card(style='w-32'):
                    with CardBody(style='w-32 flex flex-column gap-3'):
                        image = Image(src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1024px-Image_created_with_a_mobile_phone.png',
                                      alt='HypeUI',
                                      is_blurred=True
                                      )
                code = Snippet(label="Image()")

            # DIVIDER
            with Box(style=box_css):
                with Card(style='w-32'):
                    with CardBody(style='w-32 flex flex-column gap-3'):
                        Divider()
                code = Snippet(label="Divider()")

            # TOOLTIP
            with Box(style=box_css):
        
                with Tooltip(text='This is a tooltip', show_arrow=True):
                    Button(label='ToolTip', variant='shadow', style='font-semibold')
                    
                code = Snippet(label="Tooltip()")

            # BADGE
            with Box(style=box_css):
        
                with Badge(text='3', variant='solid'):
                    Button(label='Check', variant='shadow', style='font-semibold')
                    
                code = Snippet(label="Badge()")

        with Tab(key='github', title='github'):
            with Box(style=box_css):
                text = Text(label='https://github.com/OxynDev/HypeUi', style='text-black font-semibold')

        

ui.run(
    root=root,
    production=PRODUCTION,
    svg_list=development_svg
)


