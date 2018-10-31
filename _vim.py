#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Vim grammar.

Rules for everything vim and vim-like. Actually consists
of multiple grammars for context purposes.

TODO: window mode, :commands, rest of normal keybindings, filters
    other modes, vi-like mode, pentadactyl bindings, plugins, dutch translations
"""

from aenea import (
    Grammar,
    MappingRule,
    CompoundRule,
    RuleRef,
    Literal,
    Choice,
    Alternative,
    Repetition,
    Key,
    AppContext,
    ProxyAppContext)
from common import sum_actions

from common import _, extract_values
from context import vim_normal_mode
from global_ import Number, AnyCharacter

##################################
#  Rules with multiple purposes  #
##################################

class MotionRule(MappingRule):

    """Motion commands."""

    exported = False

    def __init__(self, *args, **kwargs):
        self.mapping = {
            ################
            #  left/right  #
            ################
            _("(backward|left)"): Key("h"),
            _("(forward|right)"): Key("l"),
            _("(zero|first char[acter])"): Key("0"),
            _("(caret|first non-blank char[acter])"): Key("caret"),
            _("(dollar|last char[acter])"): Key("dollar"),
            _("last visible non-blank char[acter]"): Key("g,underscore"),
            _("fist visible char[acter]"): Key("g,0"),
            _("first visible non-blank char[acter]"): Key("g,caret"),
            _("middle of line"): Key("g,m"),
            _("last visible char[acter]"): Key("g,dollar"),
            _("(pipe|column)"): Key("bar"),
            _("find <char>"): Key("f,%(char)s"),
            _("backwards find <char>"): Key("s-f,%(char)s"),
            #############
            #  up/down  #
            #############
            _("up"): Key("k"),
            _("down"): Key("j"),
            _("visible up"): Key("g,k"),
            _("visible down"): Key("g,j"),
            _("(minus|linewise non-blank up)"): Key("minus"),
            _("(plus|linewise non-blank down)"): Key("plus"),
            _("(underscore|first non-blank line down)"): Key("underscore"),
            _("line"): Key("s-g"),
            _("end of [last] line"): Key("c-end"),
            _("first non-blank char[acter] on line"): Key("g,g"),
            _("percent"): Key("percent"),
            ##########
            #  word  #
            ##########
            _("word"): Key("w"),
            _("(big|cap) word"): Key("s-w"),
            _("end"): Key("e"),
            _("(big|cap) end"): Key("s-e"),
            _("back"): Key("b"),
            _("(big|cap) back"): Key("s-b"),
            _("backward end"): Key("g,e"),
            _("backward (big|cap) end"): Key("g,s-e"),
            #################
            #  text object  #
            #################
            _("((open|left) paren|previous sentence)"): Key("lparen"),
            _("((close|right) paren|next sentence)"): Key("rparen"),
            _("((left|open) curly brace|previous paragraph)"): Key("lbrace"),
            _("((right|close) curly brace|next paragraph)"): Key("rbrace"),
            _("next section start"): Key("rbracket,rbracket"),
            _("next section end"): Key("rbracket,lbracket"),
            _("previous section start"): Key("lbracket,rbracket"),
            _("previous section end"): Key("lbracket,lbracket"),
            ###########
            #  other  #
            ###########
            _("ex"): Key("colon"),
            ###########
            #  marks  #
            ###########
            # TODO: tighten char to [a-vA-Z0-9]
            _("mark <char>"): Key("backtick,%(char)s"),
            _("mark <char> first non-blank"): Key("apostrophe,%(char)s"),
            _("mark <char> [and] keep jumps"): Key("g,backtick,%(char)s"),
            _("mark <char> first non-blank [and] keep jumps"): Key("g,apostrophe,%(char)s"),
            _("first char[acter] of last (change|yank)"): Key("apostrophe,lbracket"),
            _("last char[acter] of last (change|yank)"): Key("apostrophe,rbracket"),
            _("start of last selection"): Key("apostrophe,langle"),
            _("end of last selection"): Key("apostrophe,rangle"),
            _("restore position"): Key("apostrophe,apostrophe"),
            _("restore position at last buffer exit"): Key("apostrophe,dquote"),
            _("restore position at last insert"): Key("apostrophe,caret"),
            _("restore position at last change"): Key("apostrophe,dot"),
            _("first non-blank char[acater] of next lowercase mark"): Key("rbracket,apostrophe"),
            _("next lowercase mark"): Key("rbracket,backtick"),
            _("first non-blank char[acter] of previous lowercase mark"): Key("lbracket,apostrophe"),
            _("previous lowercase mark"): Key("lbracket,backtick"),
            #####################
            #  various motions  #
            #####################
            _("(percent|match of next item)"): Key("percent"),
            _("previous unmatched (open|left) paren"): Key("lbracket,lparen"),
            _("previous unmatched (open|left) [curly] brace"): Key("lbracket,lbrace"),
            _("next unmatched (close|right) paren"): Key("rbracket,rparen"),
            _("next unmatched (close|right) [curly] brace"): Key("rbracket,rbrace"),
            _("next start of method"): Key("rbracket,m"),
            _("next end of method"): Key("rbracket,s-m"),
            _("previous start of method"): Key("lbracket,m"),
            _("previous end of method"): Key("lbracket,s-m"),
            _("previous unmatched macro"): Key("lbracket,hash"),
            _("next unmatched macro"): Key("rbracket,hash"),
            _("previous start of comment"): Key("lbracket,asterisk"),
            _("next end of comment"): Key("rbracket,asterisk"),
            _("line from top"): Key("s-h"),
            _("middle [of (window|screen)]"): Key("s-m"),
            _("line from bottom"): Key("s-l"),
            }
        self.extras = [
            RuleRef(name='char', rule=AnyCharacter())]

        MappingRule.__init__(self, *args, **kwargs)

class VisualMotionRule(MappingRule):

    """
    Motion commands wich are only valid in visual modes and after operators.
    """

    exported = False

    def __init__(self, *args, **kwargs):
        self.mapping = {
            _("a word"): Key("a,w"),
            _("inner word"): Key("i,w"),
            _("a (big|cap) word"): Key("a,s-w"),
            _("inner (big|cap) word"): Key("i,s-w"),
            _("a sentence"): Key("a,s"),
            _("inner sentence"): Key("i,s"),
            _("a paragraph"): Key("a,p"),
            _("inner paragraph"): Key("i,p"),
            _("a bracket block"): Key("a,lbracket"),
            _("inner bracket block"): Key("i,lbracket"),
            _("a paren block"): Key("a,b"),
            _("inner paren block"): Key("i,b"),
            _("an angle block"): Key("a,langle"),
            _("inner angle block"): Key("i,langle"),
            _("a tag block"): Key("a,t"),
            _("inner tag block"): Key("i,t"),
            _("a curly block"): Key("a,s-b"),
            _("inner curly block"): Key("i,s-b"),
            _("a quoted string"): Key("a,dquote"),
            _("inner quoted string"): Key("i,dquote"),
            }

        MappingRule.__init__(self, *args, **kwargs)

class MotionOperatorRule(CompoundRule):

    """Commands with motion component."""

    exported = False

    def __init__(self, *args, **kwargs):
        self.spec = _(
            "<operator> "
            "(<line>|[to] "
            "(<motion>|<operatormotion>) "
            "[<numbers>] "
            "[<mode> mode])")
        self.extras = [
            Choice(name='operator', choices={
                _('change'): Key('c'),
                _('delete'): Key('d'),
                _('yank'): Key('y'),
                _('swap case'): Key('g,tilde'),
                _('make lowercase'): Key('g,u'),
                _('make uppercase'): Key('g,s-u'),
                _('filter'): Key('exclamation'),
                _('C filter'): Key('equal'),
                _('text formatting'): Key('g,q'),
                _('rotation 13 encoding'): Key('g,question'),
                _('shift right'): Key('rangle'),
                _('shift left'): Key('langle'),
                _('define fold'): Key('z,f'),
                _('call function'): 'g,at'}),
            Literal(name='line', text=_('line')),
            Repetition(
                name='numbers',
                child=RuleRef(rule=Number()),
                min=0,
                max=3),
            RuleRef(name='motion', rule=MotionRule()),
            RuleRef(name='operatormotion', rule=VisualMotionRule()),
            Choice(name='mode', choices={
                _("character"): Key("v"),
                _("line"): Key("s-v"),
                _("block"): Key("c-v"),
                })
            ]

        CompoundRule.__init__(self, *args, **kwargs)

    def value(self, node):
        cmd_elements = []

        ######################################
        #  buffer to place affected text in  #
        ######################################
        if node.has_child_with_name('buffer'):
            cmd_elements.append("dquote")
            cmd_elements.append(
                node.get_child_by_name('buffer').value())

        #####################
        #  motion operator  #
        #####################
        cmd_elements.append(
            node.get_child_by_name('operator').value())

        #########################
        #  operator repetition  #
        #########################
        # e.g: delete line : dd
        if node.has_child_with_name('line'):
            cmd_elements.append(cmd_elements[-1])

        ##########
        #  mode  #
        ##########
        # overwrites operator's default mode
        # think blockwise, linewise, charwise
        if node.has_child_with_name('mode'):
            cmd_elements.append(
                node.get_child_by_name('mode').value())

        ##########################
        #  numerator for motion  #
        ##########################
        # is multiplied with any numbers preceding
        # this command by vim
        cmd_elements.extend(extract_values(node, Number, recurse=True))

        ###################
        #  actual motion  #
        ###################
        # think w
        if node.has_child_with_name('motion'):
            cmd_elements.append(
                node.get_child_by_name('motion').value())
        if node.has_child_with_name('operatormotion'):
            cmd_elements.append(
                node.get_child_by_name(
                    'operatormotion').value())

        return sum_actions(cmd_elements)

    def _process_recognition(self, node, extras):
        self.value(node).execute()

class VimNormalRule(MappingRule):

    """Commands for vim normal mode."""

    exported = False

    def __init__(self, *args, **kwargs):
        self.mapping = {
            _("interrupt"): Key("c-c"),
            _("display file name"): Key("c-g"),
            _("redraw screen"): Key("c-l"),
            _("suspend"): Key("c-z"),
            _("store and exit"): Key("s-z,s-z"),
            _("unsafe exit"): Key("s-z,s-q"),
            _("edit alternate"): Key("c-caret"),
            _("help"): Key("f1"),
            ###########
            #  jumps  #
            ###########
            _("next jumplist"): Key("c-i"),
            _("previous jumplist"): Key("c-o"),
            _("previous changelist"): Key("g,semicolon"),
            _("next changlist"): Key("g,comma"),
            ###########
            #  marks  #
            ###########
            _("set mark <char>"): Key("m,%(char)s"),
            _("set previous mark"): Key("m,apostrophe"),
            _("set (open|left) [square] bracket mark"): Key("m,lbracket"),
            _("set (close|right) [square] bracket mark"): Key("m,rbracket"),
            _("set (open|left) angle bracket mark"): Key("m,langle"),
            _("set (close|right) angle bracket mark"): Key("m,rangle"),
            ###############
            #  scrolling  #
            ###############
            _("scroll down half"): Key("c-d"),
            _("scroll extra up"): Key("c-e"),
            _("scroll forward screen"): Key("c-f"),
            _("scroll back screen"): Key("c-b"),
            _("scroll down"): Key("c-y"),
            _("scroll half up"): Key("c-u"),
            ###########
            #  modes  #
            ###########
            _("insert"): Key("i"),
            _("insertmode"): Key("c-backslash,c-g"),
            _("insert at start of line"): Key("s-i"),
            _("insert on newline"): Key("o"),
            _("insert on newline before"): Key("s-o"),
            _("append"): Key("a"),
            _("(cap|big) append"): Key("s-a"),
            _("substitute"): Key("s"),
            _("replace [mode]"): Key("s-r"),
            _("external [mode]"): Key("s-q"),
            _("visual"): Key("v"),
            _("visual line"): Key("s-v"),
            _("visual block"): Key("c-v"),
            ######################
            #  undo/redo/repeat  #
            ######################
            _("redo"): Key("c-r"),
            _("undo"): Key("u"),
            _("undo on line"): Key("s-u"),
            _("(repeat|period)"): Key("dot"),
            _("(at|repeat register <register>)"): Key("at,%(register)s"),
            _("repeat previous register repeat"): Key("at,at"),
            _("repeat ex"): Key("at,colon"),
            _("(ampersand|repeat [last] (search|replace))"): Key("ampersand"),
            _("(semicolon|repeat (find|tag))"): Key("semicolon"),
            _("(comma|reverse repeat (find|tag))"): Key("comma"),
            _("record <register>"): Key("q,%(register)s"),
            _("stop recording"): Key("q"),
            _("edit ex"): Key("q,colon"),
            _("edit search"): Key("q,slash"),
            _("edit backward search"): Key("q,question"),
            ##################
            #  text editing  #
            ##################
            _("addition"): Key("c-a"),
            _("subtract"): Key("c-x"),
            _("indent"): Key("c-rbracket"),
            _("join lines"): Key("s-j"),
            _("delete char[acter]"): Key("x"),
            _("backwards delete char[acter]"): Key("s-x"),
            _("replace <char>"): Key("r,%(char)s"),
            _("(tilde|switch case)"): Key("tilde"),
            ####################
            #  copy and paste  #
            ####################
            _("copy to end of line"): Key("s-c"),
            _("paste"): Key("p"),
            _("paste before"): Key("s-p"),
            _("register <register>"): Key("dquote,%(register)s"),
            _("diff get"): Key("d,o"),
            _("diff put"): Key("d,p"),
            ############
            #  search  #
            ############
            _("lookup keyword"): Key("s-k"),
            _("backward next"): Key("s-n"),
            _("next"): Key("n"),
            _("after <char>"): Key("t,%(char)s"),
            _("backward move after <char>"): Key("s-t,%(char)s"),
            _("tag older"): Key("c-t"),
            _("(hash|backward search)"): Key("hash"),
            _("(asterisk|forward search)"): Key("asterisk"),
            _("(slash|search)"): Key("slash"),
            _("(question [mark]|backward search)"): Key("question"),
            ############
            #  window  #
            ############
            _("window increase height"): Key("c-w,plus"),
            _("window decrease height"): Key("c-w,hyphen"),
            _("window increase width"): Key("c-w,rangle"),
            _("window decrease width"): Key("c-w,langle"),
            _("window equalise"): Key("c-w,equal"),
            _("window move (H|hotel|left)"): Key("c-w,s-h"),
            _("window move (J|juliet|down)"): Key("c-w,s-j"),
            _("window move (K|kilo|up)"): Key("c-w,s-k"),
            _("window move (L|lima|right)"): Key("c-w,s-l"),
            _("window preview"): Key("c-w,s-p"),
            _("window rotate up"): Key("c-w,s-r"),
            _("window move to [new] tab"): Key("c-w,s-t"),
            _("window previous"): Key("c-w,s-w"),
            _("window split and jump"): Key("c-w,rbracket"),
            _("window split and edit alternate"): Key("c-w,caret"),
            _("window set height"): Key("c-w,underscore"),
            _("window bottom"): Key("c-w,b"),
            _("window close"): Key("c-w,c"),
            _("window split and jump to definition"): Key("c-w,d"),
            _("window split and edit file"): Key("c-w,f"),
            _("window split edit file and jump"): Key("c-w,s-f"),
            # TODO: add c-w,g,] and c-w,g,}
            _("window tab and edit file"): Key("c-w,g,f"),
            _("window tab edit file and jump"): Key("c-w,g,s-f"),
            _("window (H|hotel|left)"): Key("c-w,h"),
            _("window split and jump to declaration"): Key("c-w,i"),
            _("window (J|juliet|down)"): Key("c-w,j"),
            _("window (K|kilo|up)"): Key("c-w,k"),
            _("window (L|lima|right)"): Key("c-w,l"),
            _("window new"): Key("c-w,n"),
            _("window only"): Key("c-w,o"),
            _("window last"): Key("c-w,p"),
            _("window rotate"): Key("c-w,r"),
            _("window split [horizontal]"): Key("c-w,s"),
            _("window top"): Key("c-w,t"),
            _("window split vertical"): Key("c-w,v"),
            _("window next"): Key("c-w,w"),
            _("window exchange"): Key("c-w,x"),
            _("window close preview"): Key("c-w,z"),
            _("window width"): Key("c-w,bar"),
            _("window tag in preview"): Key("c-w,rbrace"),
            }
        self.extras = [
            # TODO: tighten register to [a-zA-Zs-9.%#:-"]
            RuleRef(name='register', rule=AnyCharacter()),
            RuleRef(name='char', rule=AnyCharacter())]

        MappingRule.__init__(self, *args, **kwargs)

####################################
#  Rules for true vim normal mode  #
####################################

class TrueVimNormalRule(CompoundRule):

    """All the repeatable commands for vim's normal mode."""

    exported = False

    def __init__(self, *args, **kwargs):
        self.spec = _("<cmd>")
        self.extras = [
            Alternative(name='cmd', children=(
                RuleRef(
                    name='motion_operator',
                    rule=MotionOperatorRule()),
                RuleRef(
                    name='motion', rule=MotionRule()),
                RuleRef(
                    name='normal', rule=VimNormalRule()),
                RuleRef(name='number', rule=Number()),
                ))
            ]

        CompoundRule.__init__(self, *args, **kwargs)

    def value(self, node):
        if node.has_child_with_name('motion_operator'):
            return node.get_child_by_name(
                'motion_operator').value()
        elif node.has_child_with_name('motion'):
            return node.get_child_by_name(
                'motion').value()
        elif node.has_child_with_name('normal'):
            return node.get_child_by_name(
                'normal').value()
        elif node.has_child_with_name('number'):
            return node.get_child_by_name(
                'number').value()
        else:
            pass

    def _process_recognition(self, node, extras):
        self.value(node).execute()

class TrueVimNormalRepetitionRule(CompoundRule):

    """Repeat TrueVimNormalRule."""

    def __init__(self, *args, **kwargs):
        self.spec = _("<cmds>")
        self.extras = [
            Repetition(
                name='cmds',
                child=RuleRef(rule=TrueVimNormalRule()),
                min=1,
                max=5)
            ]

        CompoundRule.__init__(self, *args, **kwargs)

    def value(self, node):
        extras = extract_values(node, (
            TrueVimNormalRule), recurse=True)
        return sum_actions(extras)

    def _process_recognition(self, node, extras):
        self.value(node).execute()


gvim_exec_context = AppContext(executable="gvim")
vim_putty_context = AppContext(title="vim")
rvim = ProxyAppContext(title='VIM')

vim_context = (gvim_exec_context | vim_putty_context | rvim)

grammar = Grammar("vim", context = vim_context)
grammar.add_rule(TrueVimNormalRepetitionRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
grammar = None

