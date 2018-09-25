from aenea import *


class AtomRule(MappingRule):
    exported = False
    mapping = {
        #Utility and tree
        'atom save': Key('c-s'),
        'atom save as': Key('cs-s'),
        'atom open': Key('c-o'),
        'atom open folder': Key('cs-o'),
        'atom add project folder': Key('cs-a'),
        'atom command': Key('cs-p'),
        'toggle treeview': Key('c-backslash/10'),
        'focus treeview': Key('a-backslash/10'),
        'atom new': Key('a-backslash/10') + Key('a'),
        'fuzzy search': Key('c-p'),
        'buffer search': Key('c-b'),

        # Symbols
        'symbol search': Key('c-R'),
        'symbol project': Key('cs-r'),

        # Bookmarks
        'bookmark add': Key('cs-f2'),
        'bookmark next': Key('f2'),
        'bookmark previous': Key('s-f2'),
        'bookmark list': Key('c-f2'),

        # Movement
        'file top': Key('c-home'),
        'file bottom': Key('c-end'),
        'go to line <num>': Key('c-g') + Text('%(num)d') + Key('enter'), #too complex?

        # Selection
        'mark line': Key('c-l'),
        'mark all': Key('c-a'),
        'mark up [<n>]': Key('s-up:%(n)d/3'),
        'mark down [<n>]': Key('s-down:%(n)d/3'),
        'mark left [<n>]': Key('s-left:%(n)d/3'),
        'mark right [<n>]': Key('s-right:%(n)d/3'),
        'mark lope [<n>]':  Key('cs-left:%(n)d/3'),  # Selected beginning of word
        'mark rope [<n>]':  Key('cs-right:%(n)d/3'),  # Selected end of word
        'mark document top': Key('cs-end'),
        'mark document bottom': Key('cs-home'),
        'mark home': Key('c-home'),
        'mark end': Key('c-end'),
        #todo: mark to end of line and mark to first character

    }
    extras = [
        IntegerRef("n", 1, 10),
        IntegerRef("num", 0, 100),
    ]
    defaults = {
        "n": 1,
    }
