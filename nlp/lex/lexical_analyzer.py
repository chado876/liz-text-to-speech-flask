from .tokenizer import Tokenizer
from .lemmatizer import Lemmatizer
from .pos_tagger import PosTagger
from .stemmer import Stemmatizer
from ..parse.parser import Parser

class LexicalAnalyzer:

  def perform_lexical_analysis(string):
      sentences = Tokenizer.sentence_tokenizer(string) #split text into sentences
      tokens = Tokenizer.tokenize(string)
      two_gram_tokens = Tokenizer.n_gram_tokenize(2, tokens)
      stop_words = Tokenizer.remove_stop_words(tokens)
      normalized_tokens = Tokenizer.normalize_tokens(tokens)
      lemmatized_tokens = Lemmatizer.lemmatize(tokens)
      tokens_pos = PosTagger.tag_pos(tokens)
      stemmed_tokens = Stemmatizer.stem(tokens)

      pos_sentences = []
      
      for sentence in sentences:
        pos_sentence = (PosTagger.tag_pos(Tokenizer.tokenize(sentence)))
        pos_sentences.append(pos_sentence)

      Parser.generate_parse_trees(pos_sentences)


      print('Sentences: ', sentences)
      # print('Tokens: ', tokens)
      # print('Two Grams: ', two_gram_tokens)
      # print('Stop Words: ', stop_words)
      # print('Normalized Tokens: ', normalized_tokens)
      # print('Lemmatized Tokens: ', lemmatized_tokens)
      # print('Part of Speech of Tokens: ', tokens_pos)
      # print('Stemmatized Tokens: ', stemmed_tokens)



# text = """"

# The door slammed on the watermelon.
# She moved forward only because she trusted that the ending she now was going through must be followed by a new beginning.
# It was always dangerous to drive with him since he insisted the safety cones were a slalom course.
# """
# perform_lexical_analysis(text)