"""Common values and functions for """
import string
import aenea

_GETTEXT_FUNC = lambda text: text
# pylint: disable=unnecessary-lambda
_ = lambda text: _GETTEXT_FUNC(text)

def set_translator(gettext_function):
    """Change translatorfunc (language change)."""
    global _GETTEXT_FUNC
    _GETTEXT_FUNC = gettext_function

def extract_values(node, types, recurse=False):
    """Return list of values from children matching types."""
    matches = []
    for child in node.children:
        if isinstance(child.actor, types):
            matches.append(child.value())
        if recurse:
            matches.extend(extract_values(child, types, True))
    return matches

def text_to_keystr(text):
    """Translate string to keynames for Key."""
    if text is None:
        return None
    charnames = {
        '<': 'langle',
        '{': 'lbrace',
        '[': 'lbracket',
        '(': 'lparen',
        '>': 'rangle',
        '}': 'rbrace',
        ']': 'rbracket',
        ')': 'rparen',
        '&': 'ampersand',
        "'": 'apostrophe',
        '*': 'asterisk',
        '@': 'at',
        '\\': 'backslash',
        '`': 'backtick',
        '|': 'bar',
        '^': 'caret',
        ':': 'colon',
        ',': 'comma',
        '$': 'dollar',
        '.': 'dot',
        '"': 'dquote',
        '=': 'equal',
        '!': 'exclamation',
        '#': 'hash',
        '-': 'hyphen',
        '%': 'percent',
        '+': 'plus',
        '?': 'question',
        ';': 'semicolon',
        '/': 'slash',
        '~': 'tilde',
        '_': 'underscore',
        ' ': 'space',
        '\n': 'enter',
        '\r\n': 'enter',
        '\t': 'tab',
    }
    for character in string.lowercase + string.digits:
        charnames[character] = character
    for character in string.uppercase:
        charnames[character] = 's-{}'.format(character)
    return ','.join(
        [charnames[character] for character in str(text)])

class Text(aenea.Text):

    """Text object that works with any Xdo version."""

    def _execute_events(self, events):
        return Key(text_to_keystr(events[0])).execute()

    def __str__(self):
        return self._spec

class Key(aenea.Key):

    """Key with useful str method."""

    def __str__(self):
        return self._spec

def join_actions(joiner, values):
    """
    Join Action objects with a text.

    Useful for multipart rules.

    Parameters
    ----------
    joiner: str
        text to be typed in between parts
    values: List[dragonfly.DynStrActionBase]
        list of actions to be joined with joiner

    Raises
    ------
    None

    Returns
    -------
    dragonfly.DynStrActionBase
    """
    if len(values) == 0:
        return
    elif len(values) == 1:
        return values[0]
    result = values[0]
    for value in values[1:]:
        result += Text(joiner)
        result += value
    return result

def sum_actions(actions):
    """
    Sum actions.

    Parameters
    ----------
    actions: List[dragonfly.DynStrActionBase],
        actions to be summed

    Raises
    ------
    None

    Returns
    -------
    dragonfly.DynStrActionBase
    """
    if len(actions) == 0:
        return None
    elif len(actions) == 1:
        return actions[0]
    result = actions[0]
    for action in actions[1:]:
        result += action
    return result

def execute_keystr(text):
    """Type out text."""
    Key(text_to_keystr(text)).execute()
