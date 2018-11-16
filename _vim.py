from aenea import *
from common import *
from dragonfly.actions.action_base import BoundAction
import time


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
        # "backward end": Key("g,e"),
        # "backward sky end": Key("g,s-e"),
        "real line": Key("s-g"),
        "line": "line",
        'next section': Key('lbracket, lbracket'),
        'previous section': Key('rbracket, rbracket'),
        
    }
    extras = [
        RuleRef(rule=AllCharacters(), name='allchar'),
    ]


class UncountableMotionRule(MappingRule):
    exported = False
    mapping = {
        ################
        #  left/right  #
        ################
        # "last visible non-blank char[acter]": Key("g,underscore"),
        # "fist visible char[acter]": Key("g,0"),
        # "first visible non-blank char[acter]": Key("g,caret"),
        # "middle of line": Key("g,m"),
        # "last visible char[acter]": Key("g,dollar"),
        #############
        #  up/down  #
        #############
        "bottom": Key("s-g"),
        # "end of [last] line": Key("c-end"),
        "top": Key("g,g"),
        "percent": Key("percent"),
        #################
        #  text object  #
        #################
        # "((open|left) paren|previous sentence)": Key("lparen"),
        # "((close|right) paren|next sentence)": Key("rparen"),
        # "((left|open) curly brace|previous paragraph)": Key("lbrace"),
        # "((right|close) curly brace|next paragraph)": Key("rbrace"),
        # "next section start": Key("rbracket,rbracket"),
        # "next section end": Key("rbracket,lbracket"),
        # "previous section start": Key("lbracket,rbracket"),
        # "previous section end": Key("lbracket,lbracket"),
        ###########
        #  other  #
        ###########
        "ex": Key("colon"),
        ###########
        #  marks  #
        ###########
        # TODO: tighten char to [a-vA-Z0-9]
        "mark <char>": Key("backtick,%(char)s"),
        # "mark <char> first non-blank": Key("apostrophe,%(char)s"),
        # "mark <char> [and] keep jumps": Key("g,backtick,%(char)s"),
        # "mark <char> first non-blank [and] keep jumps": Key("g,apostrophe,%(char)s"),
        # "first char[acter] of last (change|yank)": Key("apostrophe,lbracket"),
        # "last char[acter] of last (change|yank)": Key("apostrophe,rbracket"),
        # "start of last selection": Key("apostrophe,langle"),
        # "end of last selection": Key("apostrophe,rangle"),
        "restore position": Key("apostrophe,apostrophe"),
        # "restore position at last buffer exit": Key("apostrophe,dquote"),
        # "restore position at last insert": Key("apostrophe,caret"),
        # "restore position at last change": Key("apostrophe,dot"),
        # "first non-blank char[acater] of next lowercase mark": Key("rbracket,apostrophe"),
        # "next lowercase mark": Key("rbracket,backtick"),
        # "first non-blank char[acter] of previous lowercase mark": Key("lbracket,apostrophe"),
        # "previous lowercase mark": Key("lbracket,backtick"),
        ######################
        ##  various motions  #
        ######################
        "(percent|match)": Key("percent"),
        # "previous unmatched (open|left) paren": Key("lbracket,lparen"),
        # "previous unmatched (open|left) [curly] brace": Key("lbracket,lbrace"),
        # "next unmatched (close|right) paren": Key("rbracket,rparen"),
        # "next unmatched (close|right) [curly] brace": Key("rbracket,rbrace"),
        # "next start of method": Key("rbracket,m"),
        # "next end of method": Key("rbracket,s-m"),
        # "previous start of method": Key("lbracket,m"),
        # "previous end of method": Key("lbracket,s-m"),
        # "previous unmatched macro": Key("lbracket,hash"),
        # "next unmatched macro": Key("rbracket,hash"),
        # "previous start of comment": Key("lbracket,asterisk"),
        # "next end of comment": Key("rbracket,asterisk"),
        "viewer top": Key("s-h"),
        "viewer middle": Key("s-m"),
        "viewer bottom": Key("s-l"),
    }
    extras = [
        RuleRef(rule=Letters(name='letters3'), name='char')
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
        'vim save': Key('w') + Key('enter'),
        'vim save all': Key('w,a') + Key('enter'),
        'vim save quit': Key('w, q') + Key('enter'),
        'vim quit': Key('q,enter'),
        
        'vim file': Text("Files") + Key('enter'),
        'tab new': Text("tabnew"),

        'buffer next': Key('b, n') + Key('enter'),
        'buffer previous': Key('b, n') + Key('enter'),
        'buffer list': Text('ls') + Key('enter'),
        'buffer <char>': Text('b %(char)s') + Key('enter'),

        'vim split': Text('vsp') + Key('enter'),
        'horizontal split': Text('sp') + Key('enter'),

        #git fugitive
        'git add': Text('Gwrite'),
        'git commit': Text('Gcommit'),
        'git push': Text('Gpush'),
        'git pull': Text('Gpull'),
        
    }
    extras = [
        RuleRef(rule=Letters(name='letters4'), name='char')
    ]


class VimNormalRule(MappingRule):
    exported = False
    mapping = {
        'gope': Key('c-u'),
        'drop': Key('c-d'),

        'set mark <char>': Key('m, %(char)s'),
        'paste': Key('p'),

        'right split': Key('c-l'),
        'left split': Key('c-h'),
        'up split': Key('c-k'),
        'down split': Key('c-j'),

    }
    extras = [
        RuleRef(rule=Letters(name='letter2'), name='char')
    ]


class VimInsertRule(MappingRule):
    exported = False
    mapping = {
        'vim complete': Key('control, p'),
    }


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
            # print motion

            # print motion
            for action in motion:
                if action == 'line':
                    vim_action.execute()
                    continue
                if action is not None:
                    action.execute()
        if 'normal' in extras:
            normal = extras['normal']
            normal.execute()


vim_context = ProxyAppContext(title='VIM')
grammar = Grammar("vim", context=vim_context)
grammar.add_rule(VimRule())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
