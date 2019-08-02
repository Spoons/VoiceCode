from aenea import *


class Symbol(MappingRule):
    exported = False
    mapping = {
        "pipe": "|",
        "(dash|minus)": "-",
        "(dot|period)": ".",
        "(com|comma)": ",",
        "backslash": "\\",
        "underscore": "_",
        "(star|asterisk)": "*",
        "colon": ":",
        "(semicolon|semi-colon)": ";",
        "at": "@",
        "[double] quote": '"',
        "squote": "'",
        "hash": "#",
        "dollar": "$",
        "percent": "%",
        "ampersand": "&",
        "slash": "/",
        "equal": "=",
        "plus": "+",
        "space": " ",
        "bang": "!",
        "question": "?",
        "caret": "^",
        'backtick': "`",
        "tilde": "~",
        'langle': '<',
        'lace':   '{:',
        'lack':   '[',
        'len':    '(',
        'rangle': '>',
        'race':   '}',
        'rack':   ']',
        '(ren|wren)':   ')',
    }
SymbolRef = RuleRef(rule=Symbol(), name="symbol")

class Modifiers(MappingRule):
    exported = False
    mapping = {
        "alt": "a",
        "control": "c",
        "shift": "s",
        "super": "w",
    }

RuleRef(rule=Modifiers(), name="mod")

class SingleModifiers(MappingRule):
    exported = False
    mapping = {
        "alt": "alt",
        "control": "ctrl",
        "shift": "shift",
        "super": "win",
    }

RuleRef(rule=SingleModifiers(), name="single_mod")


class Letters(MappingRule):
    exported = False
    mapping = {
        "(arch)": "a",
        "(brav) ": "b",
        "(char) ": "c",
        "(dell) ": "d",
        "(etch) ": "e",
        "(fox) ": "f",
        "(golf) ": "g",
        "(hark) ": "h",
        "(ice) ": "i",
        "(jinks) ": "j",
        "(kilo) ": "k",
        "(lie|line) ": "l",
        "(mike) ": "m",
        "(nerb) ": "n",
        "(ork) ": "o",
        "(pooch) ": "p",
        "(queen) ": "q",
        "(roy) ": "r",
        "(soy) ": "s",
        "(tang) ": "t",
        "(unks) ": "u",
        "(van) ": "v",
        "(wes) ": "w",
        "(trex) ": "x",
        "(yang) ": "y",
        "(zooch) ": "z",
        "(sky arch)": "A",
        "(sky brav) ": "B",
        "(sky char) ": "C",
        "(sky dell) ": "D",
        "(sky etch) ": "E",
        "(sky fox) ": "F",
        "(sky golf) ": "G",
        "(sky hark) ": "H",
        "(sky ice) ": "I",
        "(sky jinks) ": "J",
        "(sky kilo) ": "K",
        "(sky (lie|line)) ": "L",
        "(sky mike) ": "M",
        "(sky nerb) ": "N",
        "(sky ork) ": "O",
        "(sky pooch) ": "P",
        "(sky queen) ": "Q",
        "(sky roy) ": "R",
        "(sky soy) ": "S",
        "(sky tang) ": "T",
        "(sky unks) ": "U",
        "(sky van) ": "V",
        "(sky wes) ": "W",
        "(sky trex) ": "X",
        "(sky yang) ": "Y",
        "(sky zooch) ": "Z",
    }

    def returnMap(self):
        return(self.mapping)

LetterRef = RuleRef(rule=Letters(), name="letters")

class Digits(MappingRule):
    exported = False
    mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
DigitRef = RuleRef(rule=Digits(), name="digit")

class ControlKeys(MappingRule):
    exported = False
    mapping = {
        "left": "left",
        "right": "right",
        "up": "up",
        "down": "down",
        "page up": "pgup",
        "page down": "pgdown",
        "home": "home",
        "end": "end",
        "space": "space",
        "(enter|return)": "enter",
        "escape": "escape",
        "tab": "tab",
        "backspace": "backspace"
    }
ControlRef = RuleRef(rule=ControlKeys(), name="control keys")

# F1 to F12. (do these actually work?)
class FunctionKeys(MappingRule):
    exported = False
    mapping = {
        'F one': 'f1',
        'F two': 'f2',
        'F three': 'f3',
        'F four': 'f4',
        'F five': 'f5',
        'F six': 'f6',
        'F seven': 'f7',
        'F eight': 'f8',
        'F nine': 'f9',
        'F ten': 'f10',
        'F eleven': 'f11',
        'F twelve': 'f12',
    }
FunctionRef = RuleRef(rule=FunctionKeys(), name="function keys")

class AllCharacters(CompoundRule):
    exported = False

    spec = '<character>'
    extras = [Alternative(name='character', children=(
        LetterRef,
        DigitRef,
        SymbolRef,
    ))]

    def value(self, node):
        actions = node.children[0].value()
        return actions

AllCharacterRef = RuleRef(rule=AllCharacters(), name="allchar")
