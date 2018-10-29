# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import keyboard
import words
import programs
import awesomewm

release = Key("shift:up, ctrl:up, alt:up, win:up")


repeated_commands = []
repeated_commands.append(RuleRef(rule=keyboard.KeystrokeRule()))
repeated_commands.append(RuleRef(rule=programs.ProgramsRule()))
repeated_commands.append(RuleRef(rule=awesomewm.AwesomeRule()))


commands = Alternative(repeated_commands, name="commands")
sequence = Repetition(commands, min=1, max=5, name="sequence")
sequence2 = Repetition(commands, min=1, max=5, name="sequence2")

dictation = RuleRef(name="single_dictation", rule=words.FormatRule())
dictation_sequence = Repetition(dictation, min=1, max=5, name="dictation")



class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = ("[<sequence>] "
    "([<dictation>] [terminal <single_dictation>]) "
    "[<sequence2>] "
    "[<n> times] ")
    extras = [
        sequence,  # Sequence of actions defined above.
        sequence2,  # Sequence of actions defined above.
        dictation,
        dictation_sequence,
        IntegerRef("n", 1, 100),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
        "dictation_sequence": [],
        "single_dictation": [],
        "sequence": [],
        "sequence2": [],
        "dictation": []
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        sequence2 = extras["sequence2"]  # A sequence of actions.
        dictation = extras["dictation"]
        single_dictation = extras["single_dictation"]
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
            for action in dictation:
                action.execute();
            for action in sequence2:
                action.execute()
            if single_dictation:
                single_dictation.execute();
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
