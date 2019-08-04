import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code.strip())
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


def md_render(content):
    return mistune.markdown(content)


# https://github.com/lepture/mistune#renderer
def md_render_with_hl(content):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(content)


if __name__ == '__main__':
    print(md_render('```python\nassert 1 == 1\n```'))
