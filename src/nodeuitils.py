from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="pre", value=text_node.text)
        case TextType.LINK:
            props = {'href' : text_node.url}
            return LeafNode(tag="a", value=text_node.text, props=props)
        case TextType.IMAGE:
            props = {
                        'src': text_node.url,
                        'alt': text_node.text,
                     }
            return LeafNode(tag="img",value=None, props=props)
        case _:
            raise TypeError("No such type")

