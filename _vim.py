from aenea import *


def motionChoice(name="motion"):
    return Choice(name, {
        "up": "k",
        "down": "j",
        "left": "h",
        "right": "l",
        "word": "w",
        "big word": "W",
        "board": "b",
        "word end": "e",
        "big end [word]": "E",
        "len up": "lparen",
        "ren down": "rparen",
        "lace up": "lbrace",
        "race down": "rbrace",
        "next": "n",
        "lext": "N",
})

def modifierChoice(name="modifier"):
    return Choice(name, {
        '(in | inside | inner)': 'i',
        '(a | around | outer)': 'a',
})

def objectChoice(name="object"):
    return Choice(name, {
        'word': 'w',
        'big word': 'W',
        'sentence': 's',
        '(paragraph | pare)': 'p',
        'block': 'b',
        'ren': 'rparen',
        'rack': 'rbracket',
        'race': 'rbrace',
        'quote': 'dquote',
        '(post | troth)': 'apostrophe',
})

def findChoice(name="find"):
    return Choice(name, {
        "find": "f",
        "bind": "F",
        "(until | till)": "t",
        "bill": "T",
})

def uncountableMotionChoice(name="uncountableMotion"):
    return Choice(name, {
        "start": "0",
        "front": "caret",
        "(end | rest)": "dollar",
        "match": "percent",
        "top": "g,g",
        "bottom": "G",
})

def verbChoice(name="verb"):
    return Choice(name, {
        "delete": "d",
        "(copy | yank)": "y",
        "(select | visual)": "v",
        "case lower": "g,u",
        "case upper": "g,U",
        "format": "g,q",
        "comment": "g,c",
        "(indent | reindent)": "equal",
        "(flow | reflow)": "g,q",
        "shift left": "langle",
        "shift right": "rangle",
})
def viewerChoice(name="viewMotion"):
    return Choice(name, {
        "vorth": "c-u",
        "vown": "c-d",
})


#Actions that are commonly used from normal mode
class VimNormalMode(MappingRule):
    mapping = {
        "[<n>] <motion>": Key("%(n)s, %(motion)s"),
        "<uncountableMotion>": Key("%(uncountableMotion)s"),

        # "<verb> <motion_rule>": Key("%(verb)s") + execute_rule('motion_rule'),
        # "<verb> <object>": Key("%(verb)s") + execute_rule('object'),
        # "[<n>] <simple_verb>": Key("%(n)s, %(simple_verb)s"),
        # "[<n>] <verb> line": Key("%(n)s, %(verb)s:2"),

        # "<viewMotion>": Key("%(viewMotion)s"),

        "select line": Key("V"),
        "insert": Key("i"),

        "vim save": Key("escape, colon, w, enter"),
        "vim quit": Key("escape, colon, q, enter"),
        "vim really quit": Key("escape, colon, q, exclamation, enter"),
        "vim edit": Key("escape, colon, e, space"),
        "vim save and quit": Key("escape, colon, w, q, enter"),
        "vim split": Text(":sp "),
        "vim vertical split": Text(":vs "),
        "vim tab new": Text(":tabnew "),
        "vim tab close": Text(":tabclose\n"),

        "vim (switch|toggle|swap)": Key('c-w, c-w'),
        "vim rotate": Key('c-w, r'),
        "vim try that": Key('escape, colon, w, enter, a-tab/5, up, enter'),
        }
    extras = [
            IntegerRef("n", 1, 25),
            motionChoice("motion"),
            verbChoice(),
            viewerChoice(),
            uncountableMotionChoice("uncountableMotion"),
            ]
    defaults = {
            "n": 1,
            }

gvim_exec_context = AppContext(executable="gvim")
vim_putty_context = AppContext(title="vim")
rvim = aenea.ProxyAppContext(title='VIM')

vim_context = (gvim_exec_context | vim_putty_context | rvim)

grammar = Grammar("vim", context = vim_context)
grammar.add_rule(VimNormalMode())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
grammar = None

