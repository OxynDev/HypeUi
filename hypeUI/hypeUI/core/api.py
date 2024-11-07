class Api:
    root = None
    
    def __init__(self, root):
        self.root = root

    def update(self, data):
        self._recursive_update(self.root, data)

    def _recursive_update(self, element, data):
        if hasattr(element, 'children'):
            for child in element.children:
                self._recursive_update(child, data)
                
        if hasattr(element, 'id') and element.id == data['id']:
            element.update_element(data)
            return True

    def set_style(self, element_id, style):
        element = self.find_element_by_id(self.root, element_id)
        if element:
            element.style(style)
    
    def find_element_by_id(self, element, element_id):
        if getattr(element, 'id', None) == element_id:
            return element
        if hasattr(element, 'children'):
            for child in element.children:
                found = self.find_element_by_id(child, element_id)
                if found:
                    return found
        return None
