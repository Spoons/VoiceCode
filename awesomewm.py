from aenea import *


class AwesomeRule(MappingRule):
    exported = True
    mapping = {
        'awesome run': Key('a-r/10'),
        'awesome restart': Key('as-r'),
        'awesome menu': Key('a-w'),
        'awesome maximize': Key('a-m'),
        'awesome kill': Key('as-c'),
        'focus left [<n>]': Key('a-h:%(n)d/10'),
        'focus right [<n>]': Key('a-l:%(n)d/10'),
        'focus up [<n>]': Key('a-k:%(n)d/10'),
        'focus down [<n>]': Key('a-j:%(n)d/10'),
        'increase master [<n>]': Key('sa-h:%(n)d/10'),
        'decrease master [<n>]': Key('sa-l:%(n)d/10'),
        'move previous [<n>]': Key('sa-k:%(n)d/10'),
        'move next [<n>]': Key('sa-j:%(n)d/10'),

        'width shrink [<n>]': Key('as-h:%(n)d/5'),
        'width increase [<n>]': Key('as-l:%(n)d/5'),

        'awesome layout': Key('a-space/5'),
        'awesome swap [<n>]': Key('a-o:%(n)d/5'),

        'desktop <n>': Key('a-%(n)d/10'),
        'set tag <n>': Key('as-%(n)d/5'),

        'open firefox': Key('a-r/10') + Text("firefox") + Key('enter/10'),
        'open workrave': Key('a-r/10') + Text("workrave") + Key('enter/10'),
        'open terminal': Key('a-enter'),


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
