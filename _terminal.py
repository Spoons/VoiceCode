from aenea import *

def ListToChoice(clist, name):
    command_dictionary = {}
    for command in clist:
        command_dictionary[command] = command
    return(Choice(name, command_dictionary))

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
    'diff --cached',
]

apt = ListToChoice([
        'apt update',
        'apt dist-upgrade',
        'apt autoremove',
], 'apt')

commands = ListToChoice([
    'tmux',
    'df -h',
], 'commands')


slap = Key('enter')
class TerminalRule(MappingRule):
    mapping = {
        'git': Text('git '),
        'git <gitcommand>': Text('git %(gitcommand)s '),
        'dotgit <gitcommand>': Text('dg %(gitcommand)s '),
        'go': Text('cd '),
        'go home': Text('cd ~') + slap,
        'go root': Text('cd /') + slap,
        'cp': Text('cp -r'),
        'fuzzy': Text('c') + slap,
        'fuzzy select': Key('c-t'),
        'fuzzy home': Text('ch') + slap,
        'rsync': Text('rsync '),
        'yay': Text('yay'),
        'make dir': Text('mkdir '),
        'python': Text('python'),
        'python two': Text('python2 '),
        'tee mux': Text('tmux '),
        'list': Text('ls -ltr ') + slap,
        'exit': Text('exit'),

        'yay': Text('yay'),
        'x prop': Text('xprop') + slap,
        'sudo': Text('sudo'),
        'sudo sue': Text('sudo su') + slap,
        'sue': Text('su'),
        'stop': Key('c-d'),
        'suspend': Key('c-z'),
        'resume': Text('fg') + slap,
        'system control': Text('systemctl'),
        'up directory': Text('../'),
        'clear line': Key('c-c'),
        'ssh': Text('ssh '),
        '<apt>': Text('%(apt)s'),
        '<commands>': Text('%(commands)s'),
        'paste': Key('cs-v'),

    }
    extras = [
        ListToChoice(git_array, "gitcommand"),
        apt,
        commands,
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

