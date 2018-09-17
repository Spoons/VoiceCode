from aenea import *

class AwesomeRule(MappingRule):
    mapping = {
        'awesome run': Key('w-r'),
        'awesome restart': Key('ws-r'),
        'open terminal': Key('w-enter'),
        'awesome menu': Key('w-w'),
        'awesome maximize': Key('w-m'),
        'awesome kill': Key('ws-c'),
        'next window': Key('w-j'),
        'previous window': Key('w-k'),
        'awesome urgent': Key('w-u'),
        'desktop <n>': Key('w-%(n)d'),
        'next screen': Key('cw-j'),
        'previous screen': Key('cw-k'),
        'awesome switch': Key('ws-j'),
        'awesome switch last': Key('ws-k'),
        'awesome width increase': Key('w-h'),
        'awesome width shrink': Key('w-l'),
        'awesome layout': Key('w-space'),
        'awesome window next': Key('w-o'),
        'awesome tag <n>': Key('ws-%(n)d'),

    }
    extras = [
        IntegerRef("n", 1, 9)
    ]
