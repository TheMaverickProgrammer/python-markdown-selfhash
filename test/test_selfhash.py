import unittest
import textwrap
import markdown
import mkdselfhash

class TestSecrets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        selfhash = mkdselfhash.SelfHashExtension()
        cls.markdowner = markdown.Markdown(extensions=[selfhash])

    def assertExpectedMarkdown(self, md_input, expected_output):
        output = self.markdowner.convert(textwrap.dedent(md_input))
        expected = textwrap.dedent(expected_output)
        self.assertEqual(output, expected)

    def test_one(self):
        md_input = '1. {#item-one} Share this.'
        self.assertExpectedMarkdown(md_input, 
         '<ol>\n'
         '<li>'
         '<a href="#item-one" class="mkdselfhash">item-one</a>'
         '<span id="item-one"></span>'
         ' Share this.'
         '</li>\n'
         '</ol>')
        
    def test_many(self):
        md_input = '1. {#item-one} Share this. But there is also {#this}!'
        self.assertExpectedMarkdown(md_input, 
         '<ol>\n'
         '<li>'
         '<a href="#item-one" class="mkdselfhash">item-one</a>'
         '<span id="item-one"></span>'
         ' Share this. But there is also '
         '<a href="#this" class="mkdselfhash">this</a>'
         '<span id="this"></span>'
         '!'
         '</li>\n'
         '</ol>')

    def test_urlencode(self):
        md_input = 'This link is {#cR"AZ"Y!}.'
        self.assertExpectedMarkdown(md_input, 
         '<p>This link is '
         '<a href="#cR%22AZ%22Y%21" class="mkdselfhash">cR&quot;AZ&quot;Y!</a>'
         '<span id="cR%22AZ%22Y%21"></span>'
         '.</p>')
        
    def test_hidden(self):
        md_input = '2. {-#2} Share this.'
        self.assertExpectedMarkdown(md_input, 
         '<ol>\n'
         '<li>'
         '<a href="#2" class="mkdselfhash"></a>'
         '<span id="2"></span>'
         ' Share this.'
         '</li>\n'
         '</ol>')
        
if __name__ == '__main__':
    unittest.main()
