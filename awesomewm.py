from aenea import *


class AwesomeRule(MappingRule):
    mapping = {
        'awesome run': Key('w-r'),
        'awesome restart': Key('ws-r'),
        'open terminal': Key('w-enter'),
        'awesome menu': Key('w-w'),
        'awesome maximize': Key('w-m'),
        'awesome kill': Key('ws-c'),
        'next window [<n>]': Key('w-j:%(n)d'),
        'previous window [<n>]': Key('w-k:%(n)d'),
        'awesome urgent': Key('w-u'),
        'desktop <n>': Key('w-%(n)d'),
        'next [screen|monitor|display] [<n>]': Key('cw-j:%(n)d'),
        'previous [screen|monitor|display] [<n>]': Key('cw-k:%(n)d'),
        'awesome switch': Key('ws-j'),
        'awesome switch last': Key('ws-k'),
        'awesome [width] left [<n>]': Key('w-h:%(n)d'),
        'awesome [width] right [<n>]': Key('w-l:%(n)d'),
        'awesome layout': Key('w-space'),
        'awesome window move [<n>]': Key('w-o:%(n)d'),
        'awesome tag <n>': Key('ws-%(n)d'),

    }
    extras = [
        IntegerRef("n", 1, 9)
    ]
    defaults = {
        "n": 1,
    }
