from .tokenizer import Tokenizer
from .lemmatizer import Lemmatizer
from .pos_tagger import PosTagger
from .stemmer import Stemmatizer
from ..parse.parser import Parser

class LexicalAnalyzer:

  def perform_lexical_analysis(string, treeFileName):
      sentences = Tokenizer.sentence_tokenizer(string) #split text into sentences
      tokens = Tokenizer.tokenize(string)
      two_gram_tokens = Tokenizer.n_gram_tokenize(2, tokens)
      stop_words = Tokenizer.remove_stop_words(tokens)
      normalized_tokens = Tokenizer.normalize_tokens(tokens)
      lemmatized_tokens = Lemmatizer.lemmatize(tokens)
      tokens_pos = PosTagger.tag_pos(tokens)
      stemmed_tokens = Stemmatizer.stem(tokens)

      print('============SENTENCES============ \n ', sentences)
      print('============TOKENS============ \n ', tokens)
      print('============BI-GRAMS============ \n ', two_gram_tokens)
      print('============STOP WORDS============ \n ', stop_words)
      print('============NORMALIZED TOKENS============ \n ', normalized_tokens)
      print('============LEMMATIZED TOKENS============ \n ', lemmatized_tokens)
      print('============PARTS OF SPEECH============ \n', tokens_pos)
      print('============STEMMATIZED TOKENS============ \n', stemmed_tokens)
      
      pos_sentences = []
      
      for sentence in sentences:
        pos_sentence = (PosTagger.tag_pos(Tokenizer.tokenize(sentence)))
        pos_sentences.append(pos_sentence)

      Parser.generate_parse_trees(pos_sentences, treeFileName)
