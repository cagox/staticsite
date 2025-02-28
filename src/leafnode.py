from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        html = ""
        if self.tag != None:
            html += f"<{self.tag}"
            if self.props != None:
                html += self.props_to_html()
            html += ">"
        html += self.value
        if self.tag != None:
            html += f"</{self.tag}>"
        return html
    


