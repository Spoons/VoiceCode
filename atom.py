from aenea import *


class AtomRule(MappingRule):
    mapping = {
        #Utility and tree
        'atom save': Key('c-s'),
        'atom save as': Key('cs-s'),
        'atom add project folder': Key('cs-a'),
        'atom command': Key('cs-p'),
        'toggle treeview': Key('c-slash'),
        'focus treeview': Key('a-slash'),
        'atom new file': Key('a-slash') + Key('A'),
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
        # 'go to line <ln> [<ln>]': Key('c-g\3, %(ln)d/3, colon/3, %(ln)d/3, enter'), #too complex?

        # Selection
        'mark line': Key('c-l'),
        'mark all': Key('c-a'),
        'mark up [<n>]': Key('s-up:%(n)d/3'),
        'mark down [<n>]': Key('s-down:%(n)d/3'),
        'mark left [<n>]': Key('s-left:%(n)d/3'),
        'mark right [<n>]': Key('s-right:%(n)d/3'),
        'mark lope [<n>]':  Key('cs-left:%(n)d'),  # Selected beginning of word
        'mark (yope|rope) [<n>]':  Key('cs-right:%(n)d'),  # Selected end of word
        'mark document top': Key('s-end'),
        'mark document bottom': Key('s-home'),
        #todo: Selected top and bottom of file

    }
    extras = [
        IntegerRef("n", 1, 9),
        IntegerRef("ln", 1, 9),
    ]
    defaults = {
        "n": 1,
        "ln": 1,
    }
