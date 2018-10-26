# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import keyboard
import words
import programs
import awesomewm

release = Key("shift:up, ctrl:up, alt:up, win:up")

alternatives = []
alternatives.append(RuleRef(rule=keyboard.KeystrokeRule()))
# alternatives.append(RuleRef(rule=words.AeneaFormatRule()))
# alternatives.append(RuleRef(rule=words.CustomDictationRule()))
alternatives.append(RuleRef(rule=programs.ProgramsRule()))
alternatives.append(RuleRef(rule=awesomewm.AwesomeRule()))


root_action = Alternative(alternatives, name="root_action")
sequence = Repetition(root_action, min=1, max=5, name="sequence")

FormatRuleRef = RuleRef(rule=words.FormatRule())
dictation = Repetition(FormatRuleRef, min=1, max=5, name="dictation")

class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "[<sequence>] [<dictation>] [<n> times] "
    extras = [
        sequence,  # Sequence of actions defined above.
        dictation,
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
        "sequence": [],
        "dictation": []
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        dictation = extras["dictation"]
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
            for action in dictation:
                action.execute();
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
