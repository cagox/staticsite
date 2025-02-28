import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        properties = {
            'href': 'https://github.com/cagox/staticsite',
            'target': '_blank',
            }
        node = HTMLNode(tag="a", value="StaticSite Repo", props=properties)
        expected = f" href=\"{properties['href']}\" target=\"{properties['target']}\""
        actual = f"{node.props_to_html()}"
        self.assertEqual(expected, actual)

    def test_children_none(self):
        properties = {
            'href': 'https://github.com/cagox/staticsite',
            'target': '_blank',
            }
        node = HTMLNode(tag="a", value="StaticSite Repo", props=properties)
        self.assertEqual(node.children, None)
    
    def test_repr(self):
        properties = {
            'href': 'https://github.com/cagox/staticsite',
            'target': '_blank',
            }
        node = HTMLNode(tag="a", value="StaticSite Repo", props=properties)

        expected = f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"
        actual = f"{node}"
        self.assertEqual(expected, actual)

