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

[Example](https://github.com/OxynDev/HypeUi/blob/main/test.py)

```python
from hypeUI.hypeUI.hypeui import *

ui = Ui(
    dark_mode=True,
    frameless=True,
    width=1000,
    height=600
)


with Root(ui) as root:
    with Box() as card_box:
        with Card() as card:
            with CardBody() as cardbody:
                text = Text(label='Card', style='font-semibold')

ui.run(root)
```

## Components

HypeUi currently includes the following components, with more to come as the library develops:

- **Switch**
- **Box**
- **Tabs/Tab**
- **Link**
- **Snippet**
- **Button**
- **Text**
- **Card**
- **CardBody**
- **Input**
- **Svg**

  
# Contributing
If you're interested in contributing to this project or have ideas for improvement, feel free to reach out! You can contact me on Discord: oxyn.banned. I welcome feedback and collaboration.
