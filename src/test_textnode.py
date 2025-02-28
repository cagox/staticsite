import unittest

from textnode import TextNode, TextType


class TestTextNodeEqual(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        self.assertNotEqual(node, node3)
    
    def test_repr(self):
        text = "Static Site Generator"
        text_type = TextType.BOLD
        url = "https://github.com/cagox/staticsite/"

        node = TextNode(text, text_type, url)
        expected = f"TextNode({text}, {text_type.value}, {url})"
        actual = f"{node}"
        self.assertEqual(expected, actual)





if __name__ == "__main__":
    unittest.main()