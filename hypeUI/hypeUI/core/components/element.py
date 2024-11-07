class Element:
    ui = None
    def render(self):
        raise NotImplementedError("Subclasses should implement this!")

def get_imports():
    imports = """
    import { Card, Input, Switch, Progress, Tabs, Tab, CardBody } from '@nextui-org/react';
    import { Code } from "@nextui-org/code";
    import { Snippet } from "@nextui-org/snippet";
    import { Button, ButtonGroup } from "@nextui-org/button";
    import {Link} from "@nextui-org/link";
    """
    return imports