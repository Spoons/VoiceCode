from aenea import *
from common import *
from _terminal import ListToChoice

act = Key('escape/50')
slap = Key('enter/50')

class CountableMotionRule(MappingRule):
    exported = False
    mapping = {
        # left and right movements
        "left": Key("left"),
        "right": Key("right"),
        "zero": Key("0"),
        "line start": Key("caret"),
        "line end": Key("dollar"),
        "find <allchar>": Text("f%(allchar)s"),
        "be find <allchar>": Text("F%(allchar)s"),
        "till <allchar>": Text("t%(allchar)s"),
        "be till <allchar>": Text("T%(allchar)s"),
        "up": Key("up"),
        "down": Key("down"),
        "visible up": Key("g,k"),
        "visible down": Key("g,j"),
        "word": Key("w"),
        "sky word": Key("s-w"),
        "word end": Key("e"),
        "sky end": Key("s-e"),
        "back": Key("b"),
        "sky back": Key("s-b"),
        "line": "line",
        'next section': Key('lbracket, lbracket'),
        'previous section': Key('rbracket, rbracket'),
        'race': Key('rbrace'),
        'lace': Key('lbrace'),
    }
    extras = [
        AllCharacterRef
    ]


class UncountableMotionRule(MappingRule):
    exported = False
    mapping = {
        "bottom": Key("s-g"),
        "top": Key("g,g"),
        "percent": Key("percent"),
        "ex": Key("colon"),
        "mark <letters>": Key("backtick,%(letters)s"),
        "restore position": Key("apostrophe,apostrophe"),
        "(percent|match)": Key("percent"),
        "viewer top": Key("s-h"),
        "viewer middle": Key("s-m"),
        "viewer bottom": Key("s-l"),
    }
    extras = [
        LetterRef
    ]


class VimModifierRule(MappingRule):
    exported = False
    mapping = {
        "a word": Key("a,w"),
        "inner word": Key("i,w"),
        "a sky word": Key("a,s-w"),
        "inner sky word": Key("i,s-w"),
        "a sentence": Key("a,s"),
        "inner sentence": Key("i,s"),
        "a paragraph": Key("a,p"),
        "inner paragraph": Key("i,p"),
        "a lack": Key("a,lbracket"),
        "inner lack": Key("i,lbracket"),
        "a len": Key("a,b"),
        "inner len": Key("i,b"),
        "an lack": Key("a,langle"),
        "inner lack": Key("i,langle"),
        "a tag block": Key("a,t"),
        "inner tag block": Key("i,t"),
        "a lace": Key("a,s-b"),
        "inner lace": Key("i,s-b"),
        "a quote": Key("a,dquote"),
        "inner quote": Key("i,dquote"),
        "a squote": Key("a,quote"),
        "inner squote": Key("i,quote"),
    }


class VimMotionRule(CompoundRule):
    exported = False
    spec = "(<uncountableMotion> | [<n>] (<countableMotion> | <modifier>))"
    extras = [
        RuleRef(name="uncountableMotion", rule=UncountableMotionRule()),
        RuleRef(name="countableMotion", rule=CountableMotionRule()),
        RuleRef(name="modifier", rule=VimModifierRule()),
        IntegerRef("n", 1, 50)
    ]
    defaults = {
        "n": 1
    }

    def value(self, node):
        actions = node.children[0].value()

        if type(actions) is list:
            if type(actions[0]) is int:
                actions[0] = Text("%d" % actions[0])
            return(actions)
        else:
            return ([actions])


class VimVisualRule(MappingRule):
    exported = False
    mapping = {
        'delete': Key('d'),
        'yank': Key('y'),
        'replace': Key('r'),
    }


class VimExRule(MappingRule):
    exported = False
    mapping = {
        'vim save': Key('w') + slap,
        'vim save all': Key('w,a') + slap,
        'vim save quit': Key('w, q') + slap,
        'vim quit': Key('q,enter'),
        'vim file': Text("Files") + slap,
        'tab new': Text("tabnew"),

        'buffer next': Key('b, n') + slap,
        'buffer previous': Key('b, n') + slap,
        'buffer list': Text('ls') + slap,
        'buffer <letters>': Text('b %(letters)s') + slap,

        'vim split': Text('vsp') + slap,
        'horizontal split': Text('sp') + slap,

        #git fugitive
        'git add': Text('Gwrite'),
        'git commit': Text('Gcommit'),
        'git push': Text('Gpush'),
        'git pull': Text('Gpull'),
    }
    extras = [
        LetterRef
    ]


class VimNormalRule(MappingRule):
    exported = False
    mapping = {
        '[<n>] gope': Key('c-u:%(n)d'),
        '[<n>] drop': Key('c-d:%(n)d'),
        '[<n>] slow gope': Key('c-u:%(n)d'),
        '[<n>] slow drop': Key('c-d:%(n)d'),
        'set mark <char>': Key('m, %(char)s'),
        'paste': Key('p'),
        'right split': Key('c-l'),
        'left split': Key('c-h'),
        'up split': Key('c-k'),
        'down split': Key('c-j'),

    }
    extras = [
        RuleRef(rule=Letters(name='letter2'), name='char'),
        IntegerRef('n', 1, 10),
    ]
    defaults = {
        'n':1,
    }

class VimInsertRule(MappingRule):
    exported = False
    mapping = {
        'vim complete': Key('control, p'),
    }

NormalShortcuts = [
    'caw',
    'ciw'
    'daw',
    'diw',
]

class VimShortcutsRule(MappingRule):
    mapping = {
        'append': act + Pause('50') + Key('A'),
        'substitute': act + Key('S'),
        'undo': act + Key('u'),
        '<shortcuts>': act + Text('%(shortcuts)s'),
    }
    extras = [
        ListToChoice(NormalShortcuts, 'shortcuts'),
    ]


class VimRule(CompoundRule):
    spec = '([<action> | <visual>] <motion>) | (<normal>) | (<ex>)'
    extras = [
        RuleRef(name="ex", rule=VimExRule()),
        RuleRef(name="motion", rule=VimMotionRule()),
        RuleRef(name="modifier", rule=VimModifierRule()),
        RuleRef(name="normal", rule=VimNormalRule()),
        Choice(name='action', choices={
            'change': Key('c'),
            'delete': Key('d'),
            'yank': Key('y/3'),
            'swap case': Key('g,tilde'),
            'make lowercase': Key('g,u'),
            'make uppercase': Key('g,s-u'),
            'filter': Key('exclamation'),
            'C filter': Key('equal'),
            'text formatting': Key('g,q'),
            'rotation 13 encoding': Key('g,question'),
            'shift right': Key('rangle'),
            'shift left': Key('langle'),
            'define fold': Key('z,f'),
        }),
        Choice(name='visual', choices={
            'visual': Key('v'),
            'visual block': Key('c-v'),
            'visual line': Key('V')
        })]

    def enter_ex(self):
        Key('escape, colon').execute()

    def _process_recognition(self, node, extras):  # @UnusedVariable

        if 'ex' in extras:
            ex = extras['ex']
            self.enter_ex()
            ex.execute()

        if 'visual' in extras:
            visual = extras['visual']
            visual.execute()

        vim_action = ""
        if 'action' in extras:
            vim_action = extras['action']
            vim_action.execute()

        if 'modifier' in extras:
            modifier = extras['modifier']
            modifier.execute()

        if 'motion' in extras:
            motion = extras['motion']
            for action in motion:
                if action == 'line':
                    vim_action.execute()
                if action is not None:
                    action.execute()
        if 'normal' in extras:
            normal = extras['normal']
            normal.execute()


vim_context = ProxyAppContext(title='VIM')
grammar = Grammar("vim", context=vim_context)
grammar.add_rule(VimRule())
grammar.add_rule(VimShortcutsRule())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
