from aenea import *


class AtomRule(MappingRule):
    mapping = {
        'atom save': Key('c-s'),
        'atom save as': Key('cs-s'),
        'atom add project folder': Key('cs-a'),
        'toggle treeview': Key('a-slash'),
        'focus treeview': Key('a-slash'),
        'atom new file': Key('a-slash') + Key('A'),
        'fuzzy search': Key('c-p'),
        'buffer search': Key('c-b'),
    }
