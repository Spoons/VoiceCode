from aenea import *


class AwesomeRule(MappingRule):
    exported = True
    mapping = {
        'awesome run': Key('w-r/10'),
        'awesome restart': Key('ws-r'),
        'awesome menu': Key('w-w'),
        'awesome maximize': Key('w-m'),
        'awesome kill': Key('ws-c'),
        'focus left [<n>]': Key('w-h:%(n)d/10'),
        'focus right [<n>]': Key('w-l:%(n)d/10'),
        'focus up [<n>]': Key('w-k:%(n)d/10'),
        'focus down [<n>]': Key('w-j:%(n)d/10'),
        'move left [<n>': Key('sw-h:%(n)d/10'),
        'move right [<n>': Key('sw-l:%(n)d/10'),
        'move up [<n>': Key('sw-k:%(n)d/10'),
        'move down [<n>': Key('sw-j:%(n)d/10'),

        'width shrink [<n>]': Key('as-h:%(n)d/5'),
        'width increase [<n>]': Key('as-l:%(n)d/5'),

        'awesome layout': Key('w-space/5'),

        'desktop <n>': Key('w-%(n)d/10'),
        'set tag <n>': Key('ws-%(n)d/5'),

        'open firefox': Key('w-r/10') + Text("firefox") + Key('enter/10'),
        'open workrave': Key('w-r/10') + Text("workrave") + Key('enter/10'),
        'open terminal': Key('w-enter'),


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
