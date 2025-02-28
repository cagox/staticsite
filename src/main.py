from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
    print(node)

    leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()

    print(leaf)

    parent = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], 
    )
    print(parent.to_html())




main()