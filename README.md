# HypeUi

**Status**: In development (work in progress)

## Overview

HypeUi is a Python library for creating native web GUIs with an emphasis on simplicity and flexibility. It integrates seamlessly with **React** and **NextUI** components, offering a modern and dynamic approach to building web interfaces directly in Python.

## Features

- Easy-to-use syntax for creating web-based UIs with native Python code.
- React and NextUI integration for enhanced, component-based design (https://nextui.org/docs/components/).

## Goals

The main goal of HypeUi is to provide developers with a Python-based toolkit to create web GUIs that feel native, all while leveraging the power of modern front-end frameworks.


![demo](https://github.com/OxynDev/HypeUi/blob/main/demo.png?raw=true)

## Installation

```bash
pip install hypeui
```

(Soon)

# Getting Started
Here's an example code snippet to help you get started with HypeUi:

```python

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



```

## Components

HypeUi currently includes the following components, with more to come as the library develops:

- **Switch**: [NextUi switch](https://nextui.org/docs/components/switch).
- **Box**: A flexible container component for grouping other components, allowing for structured layouts.


# Contributing
If you're interested in contributing to this project or have ideas for improvement, feel free to reach out! You can contact me on Discord: oxyn.banned. I welcome feedback and collaboration.
