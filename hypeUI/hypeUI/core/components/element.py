class Element:
    ui = None
    def render(self):
        raise NotImplementedError("Subclasses should implement this!")

def get_imports():
    imports = """
import { Card, Input, Switch, Progress } from '@nextui-org/react';
    """
    return imports