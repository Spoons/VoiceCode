# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from maps import *

from natlink import setMicState
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Mimic,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')


release = Key("shift:up, ctrl:up, alt:up, win:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")



def handle_word(text):
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Navigation keys.
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "page up [<n>]": Key("pgup:%(n)d"),
        "page down [<n>]": Key("pgdown:%(n)d"),

        "home": Key("home"),
        "end": Key("end"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),
        # Functional keys.
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "(enter|slap|slop) [<n>]": release + Key("enter:%(n)d"),
        "tab key [<n>]": Key("tab:%(n)d"),

        "delete [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "backspace [<n>]": release + Key("backspace:%(n)d"),
        "application key": release + Key("apps/3"),
        "super key": release + Key("win/3"),

        "cut [that]": release + Key("c-x/3"),
        "select all": release + Key("c-a/3"),
        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "[(hold|press)] super": Key("win:down/3"),
        "release super": Key("win:up"),
        "release [all]": release,
        "press key <pressKey>": Key("%(pressKey)s"),

        # Closures.
        "angle brackets": Key("langle, rangle, left/3"),
        "[square] brackets": Key("lbracket, rbracket, left/3"),
        "[curly] braces": Key("lbrace, rbrace, left/3"),
        "(parens|parentheses)": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "backticks": Key("backtick:2, left"),
        "single quotes": Key("squote, squote, left/3"),

        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.
        'triple tab': Key('tab/3') * 3,
        'double tab': Key('tab/3') * 2,
        'triple back tab': Key('s-tab/3') * 3,

        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        "(dot|period|dit|point) [<n>]": Key("dot:%(n)d"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        'len [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        '(ren|wren) [<n>]':   Key('rparen:%(n)d'),

        "act [<n>]": Key("escape:%(n)d"),
        "calm [<n>]": Key("comma:%(n)d"),
        'into': Key('space,bar,space'),
        'care':        Key('home'),
        '(doll|dole)': Key('end'),
        'chuck [<n>]':       Key('del:%(n)d'),
        'scratch [<n>]':     Key('backspace:%(n)d'),
        "visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),
        "doc save": Key("c-s"),
        "arrow": Text("->"),

        'gope [<n>]':  Key('pgup:%(n)d'),
        'drop [<n>]':  Key('pgdown:%(n)d'),

        'lope [<n>]':  Key('c-left:%(n)d'),
        '(yope|rope) [<n>]':  Key('c-right:%(n)d'),
        '(hill scratch|hatch) [<n>]': Key('c-backspace:%(n)d'),

        'hexadecimal': Text("0x"),
        'suspend': Key('c-z'),

        #Formatting rules
        #TODO put into seperate rule
        #'reserve <text>': Function(handle_word),
        '[number] <num>': Text("%(num)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),
        "pad <char>": Text(" %(char)s "),

        #'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Text corrections.
        # "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        # "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        # "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        #"[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8

        #"click": Mouse("right"),
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }
