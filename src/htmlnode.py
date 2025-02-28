
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        text = ""
        for key in self.props.keys():
            text += f" {key}=\"{self.props[key]}\""
        return text
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def open_tag(self):
        text = f"<{self.tag}"
        if self.props != None:
            text += super().props_to_html()
        text += ">"
        return text
    
    def close_tag(self):
        return f"</{self.tag}>"
