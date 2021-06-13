import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
import fileUtil as FileUtil

class Parser:

        def generate_parse_trees(pos_tokens_sentences, treeFileName):
            #Extract all parts of speech from any text
            chunker = RegexpParser("""
                                NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                                P: {<IN>}               #To extract Prepositions
                                V: {<V.*>}              #To extract Verbs
                                PP: {<P> <NP>}          #To extract Prepostional Phrases
                                VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                                """)
                        # Print all parts of speech in above sentence
            extractions = []
            for x in pos_tokens_sentences:
                output = chunker.parse(x)
                extractions.append(output)
                print("Extraction result for sentence \n", output)
                #output.draw()
            FileUtil.generate_tree_pdf(extractions, treeFileName)

