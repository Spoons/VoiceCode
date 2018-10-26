# module for dictating words and basic sentences
#
# (based on the multiedit module from dragonfly-modules project)
# (heavily modified)
# (the original copyright notice is reproduced below)
#
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>

import aenea
import aenea.misc
import aenea.vocabulary
import aenea.configuration
import aenea.format

from aenea import *
from symbols import symbolChoice
from letters import letterChoice

saved_words = ['var', 'console', 'vim', 'sudo', 'num', 'int', 'void', 'kait']
saved_words_list = List("saved_words_list", saved_words)
saved_words_ref = ListRef(None, saved_words_list)

mixed_dictation = Alternative([Dictation(), saved_words_ref], "mixed_dictation")
custom_dictation = Alternative([saved_words_ref], "custom_dictation")

class LocalFormat:
    def format_phrase(words):
        string = ' '.join([w.lower() for w in words])
        return(string)

    def format_with_spaces(words):
        words.append("")
        string = ' '.join([w.lower() for w in words])
        return(string)
    fmap = {'word': format_phrase,
            'phrase': format_with_spaces}

class CustomDictationRule(MappingRule):
    mapping = {
            "my phrase <custom_dictation>": Text('%(custom_dictation)s'),
            }
    extras = [custom_dictation]


local_format = ['word', 'phrase']
aenea_format = ['proper', 'camel', 'rel-path', 'abs-path', 'score', 'sentence', 
            'scope-resolve', 'jumble', 'dotword', 'dashword', 'natword', 
            'snakeword']
class AeneaFormatRule(CompoundRule):
    spec = ('[upper | lower] ( ' + ' | '.join(local_format + aenea_format) + ') [<mixed_dictation>]')
    extras = [Dictation(name='dictation'), mixed_dictation]

    def value(self, node):
        words = node.words()
        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'lower'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace('-', '') for word in words]
        if words[0].lower() in ('upper', 'lower'):
            del words[0]

        if words[0] in local_format:
            function = LocalFormat.fmap[words[0]]
        else:
            function = getattr(aenea.format, 'format_%s' % words[0].lower())

        formatted = function(words[1:])

        # empty formatted causes problems here
        print "  ->", formatted
        return Text(formatted)
