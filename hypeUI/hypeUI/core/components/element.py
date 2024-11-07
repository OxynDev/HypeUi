
class Shared():
    ui = None
    context_stack = []
    

class Element:
    ui = None

    def __init__(self):
        self.children = []

    def add_child(self, child):
        if child not in self.children:  
            self.children.append(child)

    def __repr__(self):
        return f"{self.__class__.__name__}(children={self.children})"

    def __enter__(self):
        if Shared.context_stack:
            Shared.context_stack[-1].add_child(self) 
        Shared.context_stack.append(self) 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Shared.context_stack.pop()
        
def get_imports():
    imports = """
    import { Card, Input, Switch, Progress, Tabs, Tab, CardBody } from '@nextui-org/react';
    import { Code } from "@nextui-org/code";
    import { Snippet } from "@nextui-org/snippet";
    import { Button, ButtonGroup } from "@nextui-org/button";
    import {Link} from "@nextui-org/link";
    """
    return imports