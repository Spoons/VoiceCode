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

saved_words = ['sudo', 'num', 'int', 'void', 'kait']
saved_words_list = List("saved_words_list", saved_words)
saved_words_ref = ListRef(None, saved_words_list)

mixed_dictation = Alternative([Dictation(), saved_words_ref], "mixed_dictation")
custom_dictation = Alternative([saved_words_ref], "custom_dictation")

class LocalFormat:
    def format_phrase(words):
        string = ' '.join([w.lower() for w in words[1:]])
        return(string)

    def format_with_spaces(words):
        words.append("")
        string = ' '.join([w.lower() for w in words[1:]])
        return(string)
    fmap = {'phrase': format_phrase,
            'word': format_with_spaces}

class CustomDictationRule(MappingRule):
    mapping = {
            "my phrase <custom_dictation>": Text('%(custom_dictation)s'),
            }
    extras = [custom_dictation]

#class RawDictationRule(MappingRule):
#
#class CharacterRule(MappingRule):
#    mapping = {
#            "<letter>": Key("%(letter)s"),
#            }
#    extras = [
#            letterChoice("letter"),
#            ]
#

#class LetterRule(MappingRule):
#    mapping = {
#        "<letter>": Key("%(letter)s"),
#    }
#    extras = [
#        letterChoice("letter"),
#    ]
#
#letter_sequence = Repetition(
#    Alternative([RuleRef(rule = LetterRule())]),
#    min = 1, max = 10, name = "letter_sequence")
#
#class CharacterSequenceRule(CompoundRule):
#    spec = '<letter_sequence>'
#    extras = [letter_sequence]
#    
#    def value(self, node):
#        words = node.words()
#        return Text(words)


class SymbolFormatRule(MappingRule):
    mapping = {
            "pad <symbol>": Text(' %(symbol)s '),
    }

    extras = [symbolChoice("symbol")]


local_format = ['word', 'phrase']
class AeneaFormatRule(CompoundRule):
    spec = ('[upper | lower] ( proper | camel | rel-path | abs-path | score | sentence | '
            'scope-resolve | jumble | dotword | dashword | natword | '
            'snakeword' + ' | '.join(local_format) + ') [<mixed_dictation>]')
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

        formatted = function(words)

        # empty formatted causes problems here
        print "  ->", formatted
        return Text(formatted)
