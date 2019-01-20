import os 
from aenea import *
from common import *
# Make sure dragonfly errors show up in NatLink messages.
# dragonfly.log.setup_log()

# Load _repeat.txt which contains formatting functions
config = Config("words")
namespace = config.load()


# load commonly misspelled words into saved_words
saved_words = []
word_path = "C:\\Natlink\\Natlink\\Macrosystem\\words_list.txt"
try:
    with open(word_path, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) > 2:# and word not in Letters().returnMap():
                saved_words.append(line.strip())
except Exception as e:
    print("Unable to open: " + word_path)
    print(e)

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


# TODO: revisit custom dictation tends to only custom words when they are the
# only word of the dictation contains alternative which contains custom words
# and dictation
saved_word_list = List("saved_word_list", saved_words) 
saved_word_list_ref = ListRef(None, saved_word_list) 
custom_dictation = Alternative([saved_word_list_ref, Dictation()], name="dictation")

# create our formatting role which contains the format functions and are custom dictation
class FormatRule(MappingRule):
    exported = False
    mapping  = format_functions
    extras   = [custom_dictation]
