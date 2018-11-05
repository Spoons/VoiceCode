from aenea import *
from common import *
from dragonfly.actions.action_base import BoundAction

class CountableMotionRule(MappingRule):
    exported = False
    mapping = {
        #
        "(backward|left)": Key("h"),
        "(forward|right)": Key("l"),
        "(zero|first char[acter])": Key("0"),
        "(caret|first non-blank char[acter])": Key("caret"),
        "(dollar|last char[acter])": Key("dollar"),
        # "(pipe|column)": Key("bar"),
        # "find <char>": Key("f,%(char)s"),
        # "backwards find <char>": Key("s-f,%(char)s"),

        "up": Key("k"),
        "down": Key("j"),
        # "visible up": Key("g,k"),
        # "visible down": Key("g,j"),
        # "(minus|linewise non-blank up)": Key("minus"),
        # "(plus|linewise non-blank down)": Key("plus"),
        # "(underscore|first non-blank line down)": Key("underscore"),

        "word": Key("w"),
        # "(big|cap) word": Key("s-w"),
        "end": Key("e"),
        # "(big|cap) end": Key("s-e"),
        "back": Key("b"),
        # "(big|cap) back": Key("s-b"),
        # "backward end": Key("g,e"),
        # "backward (big|cap) end": Key("g,s-e"),
    }

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
        # "line": Key("s-g"),
        # "end of [last] line": Key("c-end"),
        # "first non-blank char[acter] on line": Key("g,g"),
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
        #"mark <char>": Key("backtick,%(char)s"),
        #"mark <char> first non-blank": Key("apostrophe,%(char)s"),
        #"mark <char> [and] keep jumps": Key("g,backtick,%(char)s"),
        #"mark <char> first non-blank [and] keep jumps": Key("g,apostrophe,%(char)s"),
        #"first char[acter] of last (change|yank)": Key("apostrophe,lbracket"),
        #"last char[acter] of last (change|yank)": Key("apostrophe,rbracket"),
        #"start of last selection": Key("apostrophe,langle"),
        #"end of last selection": Key("apostrophe,rangle"),
        #"restore position": Key("apostrophe,apostrophe"),
        #"restore position at last buffer exit": Key("apostrophe,dquote"),
        #"restore position at last insert": Key("apostrophe,caret"),
        #"restore position at last change": Key("apostrophe,dot"),
        #"first non-blank char[acater] of next lowercase mark": Key("rbracket,apostrophe"),
        #"next lowercase mark": Key("rbracket,backtick"),
        #"first non-blank char[acter] of previous lowercase mark": Key("lbracket,apostrophe"),
        #"previous lowercase mark": Key("lbracket,backtick"),
        ######################
        ##  various motions  #
        ######################
        #"(percent|match of next item)": Key("percent"),
        #"previous unmatched (open|left) paren": Key("lbracket,lparen"),
        #"previous unmatched (open|left) [curly] brace": Key("lbracket,lbrace"),
        #"next unmatched (close|right) paren": Key("rbracket,rparen"),
        #"next unmatched (close|right) [curly] brace": Key("rbracket,rbrace"),
        #"next start of method": Key("rbracket,m"),
        #"next end of method": Key("rbracket,s-m"),
        #"previous start of method": Key("lbracket,m"),
        #"previous end of method": Key("lbracket,s-m"),
        #"previous unmatched macro": Key("lbracket,hash"),
        #"next unmatched macro": Key("rbracket,hash"),
        #"previous start of comment": Key("lbracket,asterisk"),
        #"next end of comment": Key("rbracket,asterisk"),
        #"line from top": Key("s-h"),
        #"middle [of (window|screen)]": Key("s-m"),
        #"line from bottom": Key("s-l"),
    }

    extras = [
        RuleRef(name='char', rule=AllCharacters())]

class VimModifierRule(MappingRule):
    exported = False
    mapping = {
        "a word": Key("a,w"),
        "inner word": Key("i,w"),
        "a (big|cap word)": Key("a,s-w"),
        "inner (big|cap word)": Key("i,s-w"),
        "a sentence": Key("a,s"),
        "inner sentence": Key("i,s"),
        "a paragraph": Key("a,p"),
        "inner paragraph": Key("i,p"),
        "a bracket block": Key("a,lbracket"),
        "inner bracket block": Key("i,lbracket"),
        "a paren block": Key("a,b"),
        "inner paren block": Key("i,b"),
        "an angle block": Key("a,langle"),
        "inner angle block": Key("i,langle"),
        "a tag block": Key("a,t"),
        "inner tag block": Key("i,t"),
        "a curly block": Key("a,s-b"),
        "inner curly block": Key("i,s-b"),
        "a quoted string": Key("a,dquote"),
        "inner quoted string": Key("i,dquote"),
    }

class VimMotionRule(CompoundRule):
    exported = False
    spec = "(<uncountableMotion> | [<n>] <countableMotion>)"
    extras = [
        RuleRef(name="uncountableMotion", rule=UncountableMotionRule()),
        RuleRef(name="countableMotion", rule=CountableMotionRule()),
        IntegerRef("n", 1, 50)
    ]
    defaults = {
        "n": 1
    }
    def value(self, node):
        return(node.children[0].value())

class VimRule(CompoundRule):
    spec = '<motion>'
    extras = [
        RuleRef(name="motion", rule=VimMotionRule()),
        Choice(name='action', choices={
            'change': Key('c'),
            'delete': Key('d'),
            'yank': Key('y'),
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
        })]

    def _process_recognition(self, node, extras):  # @UnusedVariable

        if 'motion' in extras:
            motion = extras['motion']
            # motion zero always contains the key count
            if motion[0] is not None:
                Key("{}".format(motion[0])).execute()
            motion[1].execute()

vim_context = ProxyAppContext(title='VIM') 
grammar = Grammar("vim", context=vim_context)
grammar.add_rule(VimRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
