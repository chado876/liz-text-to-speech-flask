import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import os

class Parser:

        def generate_parse_tree(pos_tokens_sentence):
            #Extract all parts of speech from any text
            chunker = RegexpParser("""
                                NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                                P: {<IN>}               #To extract Prepositions
                                V: {<V.*>}              #To extract Verbs
                                PP: {<P> <NP>}          #To extract Prepostional Phrases
                                VP: {<V> <NP|PP>*}      #To extarct Verb Phrases
                                """)
                        # Print all parts of speech in above sentence
            output = chunker.parse(pos_tokens_sentence)
            print("Extraction result for sentence \n", output)
        #     output.draw()
            cf = CanvasFrame()
            t = Tree.fromstring('(S (NP this tree) (VP (V is) (AdjP pretty)))')
            tc = TreeWidget(cf.canvas(),t)
            tc['node_font'] = 'arial 14 bold'
            tc['leaf_font'] = 'arial 14'
            tc['node_color'] = '#005990'
            tc['leaf_color'] = '#3F8F57'
            tc['line_color'] = '#175252'
            cf.add_widget(tc,10,10) # (10,10) offsets
            cf.print_to_file('parse_output/tree.ps')
            cf.destroy()
            os.system('magick convert parse_output/tree.ps parse_output/tree.pdf')