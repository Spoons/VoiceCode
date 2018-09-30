from aenea import *


class AwesomeRule(MappingRule):
    exported = True
    mapping = {
        'awesome run': Key('w-r/10'),
        'awesome restart': Key('ws-r'),
        'open terminal': Key('w-enter'),
        'awesome menu': Key('w-w'),
        'awesome maximize': Key('w-m'),
        'awesome kill': Key('ws-c'),
        'next window [<n>]': Key('w-j:%(n)d/5'),
        'previous window [<n>]': Key('w-k:%(n)d/5'),
        'awesome urgent': Key('w-u'),

        'next (screen|monitor|display) [<n>]': Key('cw-j:%(n)d/5'),
        'previous (screen|monitor|display) [<n>]': Key('cw-k:%(n)d/5'),
        'awesome change (screen|monitor|display) [<n>]': Key('w-o:%(n)d/5'),

        'awesome (switch|move)': Key('ws-j/5'),
        'awesome (switch|move) last': Key('ws-k/5'),
        'awesome [width] left [<n>]': Key('w-h:%(n)d/5'),
        'awesome [width] right [<n>]': Key('w-l:%(n)d/5'),

        'awesome layout': Key('w-space/5'),
        'awesome swap': Key('w-space/5'),

        'desktop <n>': Key('w-%(n)d/10'),
        'awesome tag <n>': Key('ws-%(n)d/5'),

        'open firefox': Key('w-r/10') + Text("firefox") + Key('enter/10'),
        'open workrave': Key('w-r/10') + Text("workrave") + Key('enter/10'),


    }
    extras = [
        IntegerRef("n", 1, 9)
    ]
    defaults = {
        "n": 1,
    }

awesome_context = aenea.ProxyPlatformContext('linux')
grammar = Grammar("awesome", context=awesome_context)
grammar.add_rule(AwesomeRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
grammar = None
