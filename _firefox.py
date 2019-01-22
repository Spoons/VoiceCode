# from common import *
from aenea import *

class FirefoxRule(MappingRule):
    # exported = False
    mapping = {
        'page top': Text('gg'),
        'page bottom': Text('G'),
        'link': Text('f'),
        '[<n>] page back': Text('H'),
        '[<n>] page forward': Text('L'),
        'reload': Text('r'),
        '[<n>] next tab': Key("J:%(n)d"),
        '[<n>] back tab': Key("K:%(n)d"),
        '<n> tab': Text("b%(n)s") + Key('enter'),
        'buffer': Text('b'),
        'open': Text('o'),
        'current open': Text('o'),
        'open tab': Text('t'),
        'close tab': Text('d'),
        'reopen tab': Text('u'),
        'duplicate tab': Text('zd')
    }
    extras = [
        IntegerRef("n", 0, 10),
    ]
    defaults={
        "n":1
    }

firefox_context = ProxyAppContext(title="Firefox")
grammar = Grammar("Firefox")
grammar.add_rule(FirefoxRule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
