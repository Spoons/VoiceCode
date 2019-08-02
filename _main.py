# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import keyboard
import words

release = Key("shift:up, ctrl:up, alt:up, win:up")




dictation = RuleRef(name="dictation", rule=words.FormatRule())

command_list = []
command_list.append(RuleRef(rule=keyboard.KeystrokeRule()))
command_list.append(dictation)
commands = Alternative(command_list, name="commands")

sequence = Repetition(commands, min=1, max=10, name="sequence")



class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = ("[<sequence>] "
    "[terminal <dictation>] "
    "[<n> times] ")
    extras = [
        sequence,  # Sequence of actions defined above.
        dictation,
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
        "dictation": [],
        "sequence": [],
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        dictation = extras["dictation"]
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
            if dictation:
                dictation.execute();
            release.execute()

grammar = Grammar("root rule")
grammar.add_rule(RepeatRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
