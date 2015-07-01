__author__ = 'Girish'
import html.parser as par

class parser(par.HTMLParser):
    def __init__(self):
        super().__init__()
    def handle_starttag(self, tag, attrs):
        if tag =='td':
            print(attrs)
