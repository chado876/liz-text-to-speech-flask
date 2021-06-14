from os import name
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
                print("\033[94m Extraction result for sentence \033[0m \n", output)
            FileUtil.generate_tree_pdf(extractions, treeFileName)

        def print_named_entities(pos_sentences):
            named_entities = []
            for sentence in pos_sentences:
                ne_tree = nltk.ne_chunk(sentence)
                print("\n\033[94m============Named Entity Tree============\033[0m \n", ne_tree)

                for tree in ne_tree:
                    if hasattr(tree, 'label'):
                       named_entities.append(tree.label() + ' - ' + ' '.join(attribute[0] for attribute in tree))
            print("\n\033[94m============Named Entities in Text============\033[0m \n", named_entities)
           
            

                
