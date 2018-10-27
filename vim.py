from dragonfly import Choice

def VimMotion(name="motion"):
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
        "sent up": "lparen",
        "sent down": "rparen",
        "pare up": "lbrace",
        "pare down": "rbrace",
        "next": "n",
        "pecks": "N",
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
        '(paren | laip)': 'rparen',
        '(brackets | rack)': 'rbracket',
        '(brace | race)': 'rbrace',
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

class VimNormalMode(MappingRule):
    mapping = {
        "[<n>] <motion>": Key("%(n)d, %(motion)s"),
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
        },
    extras = [
            IntegerRef("n", 1, 25),
            VimMotion("motion")
            ]
    defaults = {
            "n": 1,
            }
