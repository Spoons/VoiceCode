# module for dictating words and basic sentences
#
# (based on the multiedit module from dragonfly-modules project)
# (heavily modified)
# (the original copyright notice is reproduced below)
#
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

import aenea
import aenea.misc
import aenea.vocabulary
import aenea.configuration
import aenea.format

from aenea import (
    AeneaContext,
    AppContext,
    Alternative,
    CompoundRule,
    Dictation,
    DictList,
    DictListRef,
    Grammar,
    IntegerRef,
    Literal,
    ProxyAppContext,
    MappingRule,
    NeverContext,
    Repetition,
    RuleRef,
    Sequence
)

from aenea import (
    Key,
    Text
)


lastFormatRuleLength = 0
# lastFormatRuleWords = []
# class NopeFormatRule(CompoundRule):
#     spec = ('nope')
#
#     def value(self, node):
#         global lastFormatRuleLength
#         print "erasing previous format of length", lastFormatRuleLength
#         return Key('backspace:' + str(lastFormatRuleLength))
#
# class ReFormatRule(CompoundRule):
#     spec = ('that was [upper | natural] ( proper | camel | rel-path | abs-path | score | sentence | '
#             'scope-resolve | jumble | dotword | dashword | natword | snakeword | brooding-narrative)')
#
#     def value(self, node):
#         global lastFormatRuleWords
#         words = lastFormatRuleWords
#         words = node.words()[2:] + lastFormatRuleWords
#         print words
#
#         uppercase = words[0] == 'upper'
#         lowercase = words[0] != 'natural'
#
#         if lowercase:
#             words = [word.lower() for word in words]
#         if uppercase:
#             words = [word.upper() for word in words]
#
#         words = [word.split('\\', 1)[0].replace('-', '') for word in words]
#         if words[0].lower() in ('upper', 'natural'):
#             del words[0]
#
#         function = getattr(aenea.format, 'format_%s' % words[0].lower())
#         formatted = function(words[1:])
#
#         global lastFormatRuleLength
#         lastFormatRuleLength = len(formatted)
#         return Text(formatted)
def format_phrase(words):
    string = ' '.join([w.lower() for w in words[1:]])
    return(string)
    
def format_with_spaces(words):
    words.append("")
    string = ' '.join([w.lower() for w in words[1:]])
    return(string)


mixed_dictation = Alternative([Dictation(), saved_words_list])

class FormatRule(CompoundRule):
    spec = ('[upper | natural] ( phrase | spocks | proper | camel | rel-path | abs-path | score | sentence | '
            'scope-resolve | jumble | dotword | dashword | natword | snakeword | brooding-narrative) [<dictation>] [reserved]')
    extras = [Dictation(name='dictation')]

    local_format_rules = ['phrase', 'spocks']


    def value(self, node):
        words = node.words()
        if words[-1] is 'reserved':
            words = words[:-1]
        print "format rule:", words

        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'natural'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace('-', '') for word in words]
        if words[0].lower() in ('upper', 'natural'):
            del words[0]

        formatted = ""
        print words
        if words[0] not in self.local_format_rules:
            function = getattr(aenea.format, 'format_%s' % words[0].lower())
            formatted = function(words[1:])
            global lastFormatRuleWords
            lastFormatRuleWords = words[1:]

            global lastFormatRuleLength
            lastFormatRuleLength = len(formatted)
        else:
            if str(words[0]) == 'phrase':
                formatted = format_phrase(str(words))
            if str(words[0]) == 'spocks':
                formatted = format_with_spaces(words)

        # empty formatted causes problems here
        print "  ->", formatted
        return Text(formatted)
