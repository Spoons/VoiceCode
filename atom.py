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
        'top file': Key('c-home'),
        'end file': Key('c-end'),
        'line <ln> [<lc>]': Key('c-g\3') + Key('%(ln)d\3, colon\3, %(lc)d\3, enter'),

        # Selection
        'select line': Key('c-L'),
        'select all': Key('c-A'),
        'select up [<n>]': Key('s-up:%(n)d\3'),
        'select down [<n>]': Key('s-down:%(n)d\3'),
        'select left [<n>]': Key('s-left:%(n)d\3'),
        'select right [<n>]': Key('s-right:%(n)d\3'),
        'select lope [<n>]':  Key('cs-left:%(n)d'),  # Selected beginning of word
        'select (yope|rope) [<n>]':  Key('cs-right:%(n)d'),  # Selected end of word
        'select end': Key('s-end'),
        'select beginning': Key('s-home'),
        # todo: Selected top and bottom of file

    }
