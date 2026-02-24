import re
import urllib.parse
from html import escape
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

pattern = r'{#(.*?)}'

class SelfHashExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            SelfHasher(md), "selfhasher", 20)

class SelfHasher(Preprocessor):
    def run(self, lines):
        for i in range(len(lines)):
            line = lines[i]
            m = re.findall(pattern, line)

            if len(m) > 0:
                for n in m:
                    subpattern = r'{#'+n+r'}'
                    html = self._html(n)
                    line = re.sub(subpattern, html, line)

            lines[i] = line
        return lines
    
    def _html(self, s):
         us = urllib.parse.quote(s)
         hs = escape(s, quote=True)
         return '<a href="#' + us + '" class="mkdselfhash">' + hs + '</a><span id="' + us + '"></span>'

def makeExtension(*args, **kwargs):
        return SelfHashExtension(*args, **kwargs)

