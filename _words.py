from dragonfly import (
    ActionBase,
    Alternative,
    AppContext,
    Choice,
    Compound,
    CompoundRule,
    Config,
    DictList,
    DictListRef,
    Dictation,
    Empty,
    Function,
    Grammar,
    IntegerRef,
    Key,
    List,
    ListRef,
    MappingRule,
    Mimic,
    Mouse,
    Optional,
    Pause,
    Repeat,
    Repetition,
    RuleRef,
    RuleWrap,
    Text,
)

from maps import *
# Make sure dragonfly errors show up in NatLink messages.
# dragonfly.log.setup_log()

# Load _repeat.txt.
config = Config("words")
namespace = config.load()

# Load commonly misrecognized words saved to a file.
# TODO: Revisit.
saved_words = []

import os 

word_path = "C:\\Natlink\\Natlink\\Macrosystem\\word_list.txt"
try:
    with open(word_path, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) > 2 and word not in letters_map:
                saved_words.append(line.strip())
except Exception as e:
    print("Unable to open: " + word_path)
    print(e)

saved_word_list = List("saved_word_list", saved_words)

# Here we prepare the action map of formatting functions from the config file.
# Retrieve text-formatting functions from this module's config file. Each of
# these functions must have a name that starts with "format_".
format_functions = {}
if namespace:
    print "loading namespace"
    for name, function in namespace.items():
        if name.startswith("format_") and callable(function):
            spoken_form = function.__doc__.strip()

            # We wrap generation of the Function action in a function so
            #  that its *function* variable will be local.  Otherwise it
            #  would change during the next iteration of the namespace loop.
            def wrap_function(function):
                def _function(dictation):
                    formatted_text = function(dictation)
                    Text(formatted_text).execute()
                return Function(_function)

            action = wrap_function(function)
            format_functions[spoken_form] = action

saved_word_list_ref = ListRef(None, saved_word_list)
custom_dictation = Alternative([saved_word_list_ref, Dictation()], name="dictation")

class FormatRule(MappingRule):
    mapping  = format_functions
    extras   = [Dictation("dictation")]

grammar = Grammar("hey buddy")
grammar.add_rule(FormatRule())
grammar.load()
