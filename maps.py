
# For repeating of characters.
specialCharMap = {
        "(bar|vertical bar|pipe)": "|",
        "(dash|minus|hyphen)": "-",
        "(dit|period)": ".",
        "comma": ",",
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
        }

compound_symbols = {
        "plus": "+",
        "plus sign": "+",
        "plus twice": "++",
        "plus sign twice": "++",
        "minus": "-",
        "hyphen": "-",
        "dash": "-",
        ",": ",",
        "colon": ":",
        "equal": "=",
        "equal sign": "=",
        "equal twice": "==",
        "equal sign twice": "==",
        "not equal": "!=",
        "plus equal": "+=",
        "minus equal": "-=",
        "greater than": ">",
        "rangle": ">",
        "lange": "<",
        "rangle twice": ">>",
        "lange twice": ">>",
        "rangle equal": ">=",
        "lange equal": "<=",
        "dot": ".",
        "period": ".",
        "lope": "(",
        "len": "(",
        "ren": ")",
        "close paren": ")",
        "lace": "{",
        "open brace": "{",
        "race": "}",
        "close brace": "}",
        "lack": "[",
        "open bracket": "[",
        "rack": "]",
        "close bracket": "]",
        "[double] quote": "\"",
        "open quote": "\"",
        "close quote": "\"",
        "semi": ";",
        "semicolon": ";",
        "bang": "!",
        "exclamation mark": "!",
        "percent": "%",
        "percent sign": "%",
        "star": "*",
        "asterisk": "*",
        "backslash": "\\",
        "slash": "/",
        "tilde": "~",
        "backtick": "`",
        "underscore": "_",
        "underscore twice": "__",
        "dunder": "__",
        "single quote": "'",
        "apostrophe": "'",
        "dollar": "$",
        "dollar sign": "$",
        "caret": "^",
        "arrow": "->",
        "fat arrow": "=>",
        "colon twice": "::",
        "amper": "&",
        "ampersand": "&",
        "amper twice": "&&",
        "ampersand twice": "&&",
        "pipe": "|",
        "pipe twice": "||",
        "hash": "#",
        "number sign": "#",
        "at sign": "@",
        "question": "?",
        "question mark": "?",
}

# Modifiers for the press-command.
modifierMap = {
        "alt": "a",
        "control": "c",
        "shift": "s",
        "super": "w",
        }

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
        "alt": "alt",
        "control": "ctrl",
        "shift": "shift",
        "super": "win",
        }

letterMap = {
        "(alpha|arch)": "a",
        "(bravo|brav) ": "b",
        "(charlie|char) ": "c",
        "(delta|dell) ": "d",
        "(echo|etch) ": "e",
        "(fox) ": "f",
        "(golf) ": "g",
        "(hotel|hark) ": "h",
        "(indigo|ice) ": "i",
        "(julia|jinks) ": "j",
        "(kilo) ": "k",
        "(lie|line) ": "l",
        "(mike) ": "m",
        "(november|nerb) ": "n",
        "(Oscar|ork) ": "o",
        "(papa|pooch) ": "p",
        "(queen) ": "q",
        "(romeo|roy) ": "r",
        "(sierra|soy) ": "s",
        "(tango|tay) ": "t",
        "(uniform|unks) ": "u",
        "(victor|van) ": "v",
        "(whiskey|wes) ": "w",
        "(x-ray|trex) ": "x",
        "(yankee|yang) ": "y",
        "(zulu|zooch) ": "z",
        }

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
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


controlKeyMap = {
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

# F1 to F12. (do these actually work?)
functionKeyMap = {
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

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(compound_symbols)
pressKeyMap.update(functionKeyMap)

letters_map = letterMap
def keyChoice(name="key"):
    return Choice(name, pressKeyMap);
def letterChoice(name="letter"):
    return Choice(name, letterMap); 
def numberChoice(name="number"):
    return Choice(name, numberMap);
