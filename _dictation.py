from aenea import *

class InsertMode(MappingRule):
    mapping = {
        "<text>": Text("%(text)s")
    }
    extras = [
        Dictation("text")
    ]


InsertModeGrammar = Grammar("InsertMode")
InsertModeGrammar.add_rule(InsertMode())
InsertModeGrammar.load()
InsertModeGrammar.disable()

class InsertModeEnabler(CompoundRule):
    spec = "dictate"

    def _process_recognition(self, node, extras):
        print "Enabling Insert Mode"
        if InsertModeGrammar:
            InsertModeGrammar.enable()
        if InsertModeDisablerGrammar:
            InsertModeDisablerGrammar.enable()
        if InsertModeEnablerGrammar:
            InsertModeEnablerGrammar.disable()

InsertModeEnablerGrammar = Grammar("InsertMode Enabler")
InsertModeEnablerGrammar.add_rule(InsertModeEnabler())
InsertModeEnablerGrammar.load()

class InsertModeDisabler(CompoundRule):
    spec = "dictate"

    def _process_recognition(self, node, extras):
        print "Disabling Insert Mode"
        if InsertModeGrammar:
            InsertModeGrammar.disable()
        if InsertModeDisablerGrammar:
            InsertModeDisablerGrammar.disable()
        if InsertModeEnablerGrammar:
            InsertModeEnablerGrammar.enable()

InsertModeDisablerGrammar = Grammar("InsertMode Disabler")
InsertModeDisablerGrammar.add_rule(InsertModeDisabler())
InsertModeDisablerGrammar.load()


def unload():
    global InsertModeGrammar
    if InsertModeGrammar: 
        InsertModeGrammar.unload()
    InsertModeGrammar = None

    global InsertModeEnablerGrammar
    if InsertModeEnablerGrammar:
        InsertModeEnablerGrammar.unload()
    InsertModeEnablerGrammar = None

    global InsertModeDisablerGrammar
    if InsertModeDisablerGrammar:
        InsertModeDisablerGrammar.unload()
    InsertModeDisablerGrammar = None
