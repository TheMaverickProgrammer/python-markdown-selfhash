import re
import urllib.parse
from html import escape
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension

show_pattern = r'{#(.*?)}'
hide_pattern = r'{-#(.*?)}'

class SelfHashExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            SelfHasher(md), "selfhasher", 1)

class SelfHasher(Preprocessor):
    def run(self, lines):
        for i in range(len(lines)):
            line = lines[i]

            m = re.findall(show_pattern, line)
            if len(m) > 0:
                for n in m:
                    subpattern = r'{#'+n+r'}'
                    html = self._html(n, show_content=True)
                    line = re.sub(subpattern, html, line)

            m = re.findall(hide_pattern, line)
            if len(m) > 0:
                 for n in m:
                    subpattern = r'{-#'+n+r'}'
                    html = self._html(n, show_content=False)
                    line = re.sub(subpattern, html, line)

            lines[i] = line
        return lines
    
    def _html(self, s, show_content=False):
         us = urllib.parse.quote(s)

         hs = ''
         if show_content:
            hs = escape(s, quote=True)

         return '<a href="#' + us + '" class="mkdselfhash">' + hs + '</a><span id="' + us + '"></span>'

def makeExtension(*args, **kwargs):
        return SelfHashExtension(*args, **kwargs)

