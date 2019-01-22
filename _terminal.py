from aenea import *
git_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in git_array:
    gitcommand[command] = command

class TerminalRule(MappingRule):
    mapping = {
        'git': Text('git'),
        'git <gitcommand>': Text('git %(gitcommand)s'),
        'move': Text('mv '),
        'cp': Text('cp -r'),
        'fuzzy': Text('c'),
        'fuzzy select': Key('c-t'),
        'fuzzy home': Text('ch'),
        'rsync': Text('rsync '),
        'yay': Text('yay'),
        'make dir': Text('mkdir '),
        'python': Text('python'),
        'python two': Text('python2 '),
        'tee mux': Text('tmux '),
        'list': Text('ls -ltr '),
        'exit': Text('exit'),
        'yay': Text('yay'),
        'x prop': Text('xprop'),
        'sudo': Text('sudo'),
        'sue': Text('su'),
        'stop': Key('c-d'),
        'suspend': Key('c-z'),
        'resume': Text('fg'),
        'system control': Text('systemctl'),
        'up directory': Text('../'),
    }
    extras = [
         Choice('gitcommand', gitcommand)
    ]

terminal_context = ProxyAppContext(title='urxvt')
grammar = Grammar('terminal')
grammar.add_rule(TerminalRule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

        # rsync
        # cd
        # sensors
        # yay
        # wine
        # mkdir
        # python
        # python2
        # tmuxg
        # ls
        # exit
        # c-d
        # xprop
        # sudo
        # su
        # startx
        # fdisk
        # df
        # pass
        # ssh
        # mount
        # umount
        # tree
        # systemctl
        # pkill
        # fg
        # 'suspend'

