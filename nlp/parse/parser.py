import nltk
from nltk import RegexpParser
import fileUtil as FileUtil

class Parser:

        def generate_parse_trees(pos_tokens_sentences, treeFileName):
            #Extract all parts of speech from any text 
            #RegexpParser 
            grammar = RegexpParser("""
                                NP: {<DT>?<JJ>*<NN>?<NNS>?<NNP>?<NNPS>}    #To extract Noun Phrases
                                P: {<IN>}               #To extract Prepositions
                                V: {<V.*>}              #To extract Verbs
                                PP: {<P> <NP>}          #To extract Prepostional Phrases
                                VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                                """)
            extractions = []
            for x in pos_tokens_sentences:  #parse sentences one by one
                output = grammar.parse(x) 
                extractions.append(output)
                print("Extraction result for sentence \n", output)
            FileUtil.generate_tree_pdf(extractions, treeFileName)

