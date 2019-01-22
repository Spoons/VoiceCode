from aenea import *

class i3Rule(MappingRule):
    mapping = {
        'dmenu': Key('a-d'),
        '[<n>] focus down': Key('a-down:%(n)s'),
        '[<n>] focus right': Key('a-right:%(n)s'),
        '[<n>] focus left': Key('a-left:%(n)s'),
        '[<n>] focus up': Key('a-up:%(n)s'),
        'open calibre': Key('as-m'),
        'open firefox': Key('a-w'),
        'open mixer': Key('a-a'),
        'open pass': Key('a-d'),
        'open ranger': Key('a-r'),
        'open terminal': Key('a-enter'),
        'open thunar': Key('as-i'),
        'open virt': Key('as-v'),
        '[<n>] resize down': Key('as-c:%(n)s'),
        '[<n>] resize left': Key('as-h:%(n)s'),
        '[<n>] resize right': Key('as-s:%(n)s'),
        '[<n>] resize up': Key('as-t:%(n)s'),
        'split horizontal': Key('a-g'),
        'split vertical': Key('a-v'),
        'window fullscreen': Key('a-f'),
        '[<n>] window down': Key('as-down:%(n)s'),
        '[<n>] window left': Key('as-left:%(n)s'),
        '[<n>] window right': Key('as-right:%(n)s'),
        '[<n>] window up': Key('as-up:%(n)s'),
        'workspace <w>': Key('a-%(w)s'),
    }
    extras = [
        IntegerRef("w", 0, 10),
        IntegerRef("n", 0, 10),
    ]
    defaults = {
        "n":1
    }


grammar = Grammar('i3')
grammar.add_rule(i3Rule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
