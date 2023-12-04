# simple lesk algorithm as defined on wikipedia:
# function SIMPLIFIED LESK(word,sentence) returns best sense of word
# best-sense <- most frequent sense for word
# max-overlap <- 0
# context <- set of words in sentence
# for each sense in senses of word do
# signature <- set of words in the gloss and examples of sense
# overlap <- COMPUTEOVERLAP (signature,context)
# if overlap > max-overlap then
# max-overlap <- overlap
# best-sense <- sense
# end return (best-sense)

from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from itertools import chain

class SimpleLesk:
    ps = PorterStemmer()    
    def lesk(self, context, keyword, stem=True):
        best_sense = wn.synsets(keyword, pos=wn.NOUN)[0]
        max_overlaps = 0
        lesk_sense = None
        context = context.split()
        for ss in wn.synsets(keyword):
            lesk_dictionary = []
            # the lesk algorithm relies heavily on the context and word definition
            # sharing a lot of words
            lesk_dictionary+= ss.definition().split()
            lesk_dictionary+= ss.lemma_names()    

            if stem == True: 
                lesk_dictionary = [self.ps.stem(i) for i in lesk_dictionary]
                context = [self.ps.stem(i) for i in context] 

            overlaps = set(lesk_dictionary).intersection(context)

            if len(overlaps) > max_overlaps:
                lesk_sense = ss
                max_overlaps = len(overlaps)
        # in the case that a context shares no words with the definition, return the first sense of the word
        if lesk_sense is None: return best_sense
        return lesk_sense