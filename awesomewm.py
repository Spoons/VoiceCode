from aenea import *


class AwesomeRule(MappingRule):
    exported = False
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
        'desktop <n>': Key('w-%(n)d/10'),
        'next [screen|monitor|display] [<n>]': Key('cw-j:%(n)d/5'),
        'previous [screen|monitor|display] [<n>]': Key('cw-k:%(n)d/5'),
        'awesome switch': Key('ws-j/5'),
        'awesome switch last': Key('ws-k/5'),
        'awesome [width] left [<n>]': Key('w-h:%(n)d/5'),
        'awesome [width] right [<n>]': Key('w-l:%(n)d/5'),
        'awesome layout': Key('w-space/5'),
        'awesome swap': Key('w-space/5'),
        'awesome window move [<n>]': Key('w-o:%(n)d/5'),
        'awesome tag <n>': Key('ws-%(n)d/5'),
        'open firefox': Key('w-r/10') + Text("firefox") + Key('enter/10'),

    }
    extras = [
        IntegerRef("n", 1, 9)
    ]
    defaults = {
        "n": 1,
    }
