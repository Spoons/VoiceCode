from aenea import *


class VimRule(MappingRule):
    mapping = {
        "vim test": Key('k')
    }
vim_context = aenea.ProxyAppContext(title='VIM')

grammar = Grammar("vim", context=vim_context)
grammar.add_rule(VimRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
grammar = None
