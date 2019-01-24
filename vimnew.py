from aenea import *
from common import *

from _terminal import ListToChoice

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
UncountableMotionRef = RuleRef(rule=UncountableMotionRule(), name="uncountable")

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
        "word": Key("w"),
        "sky word": Key("s-w"),
        "(word end|wend)": Key("e"),
        "sky end": Key("s-e"),
        "back": Key("b"),
        "sky back": Key("s-b"),
        # "backward end": Key("g,e"),
        # "backward sky end": Key("g,s-e"),
        "real line": Key("s-g"),
        # "line": "line",
        'next section': Key('lbracket, lbracket'),
        'previous section': Key('rbracket, rbracket'),
    }
    extras = [
        AllCharacterRef
    ]

CountableMotionRef = RuleRef(rule=CountableMotionRule(), name='motion')

# class MotionModifierRule(MappingRule):
#     exported = False
#     mapping = {
#         "a word": Key("a,w"),
#         "inner word": Key("i,w"),
#         "a sky word": Key("a,s-w"),
#         "inner sky word": Key("i,s-w"),
#         "a sentence": Key("a,s"),
#         "inner sentence": Key("i,s"),
#         "a paragraph": Key("a,p"),
#         "inner paragraph": Key("i,p"),
#         "a lack": Key("a,lbracket"),
#         "inner lack": Key("i,lbracket"),
#         "a len": Key("a,b"),
#         "inner len": Key("i,b"),
#         "an lack": Key("a,langle"),
#         "inner lack": Key("i,langle"),
#         "a tag block": Key("a,t"),
#         "inner tag block": Key("i,t"),
#         "a lace": Key("a,s-b"),
#         "inner lace": Key("i,s-b"),
#         "a quote": Key("a,dquote"),
#         "inner quote": Key("i,dquote"),
#         "a squote": Key("a,quote"),
#         "inner squote": Key("i,quote"),
#     }
# MotionModifierRef = RuleRef(rule=MotionModifierRule(), name="modifier")



actions = Choice(name='action', choices={
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
})

class VimRule(MappingRule):
    mapping = {
        'append': act + Key('A'),
        'substitute': act + Key('S'),
        '<shortcuts>': act + Text('%(shortcuts)s'),
        '<uncountable>': act,
    }
    extras = [
        ListToChoice(NormalShortcuts, 'shortcuts'),
        actions,
        # MotionModifierRef,
        CountableMotionRef,
        UncountableMotionRef,
    ]

vim_context = ProxyAppContext(title='VIM')
grammar = Grammar("vim", context=vim_context)
grammar.add_rule(VimRule())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
grammar = None

