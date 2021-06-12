import re
from nltk.util import ngrams
import nltk
from nltk import tokenize

class Tokenizer:

    def tokenize(string):
        pattern = re.compile(r"([-\s.,;!?])+")
        tokens = pattern.split(string)
        tokens = [x for x in tokens if x and x not in '- \t\n.,;!?']
        return tokens
    
    def sentence_tokenizer(string):
        return tokenize.sent_tokenize(string)

    def n_gram_tokenize(n, tokens):
        n_gram_tokens = list(ngrams(tokens, n))
        return n_gram_tokens

    def remove_stop_words(tokens):
        nltk.download('stopwords')
        stop_words = nltk.corpus.stopwords.words('english') 

        token_stop_words = [sw for sw in tokens if sw and sw in stop_words]
        return token_stop_words


    def normalize_tokens(tokens):
        normalized_tokens = [token.lower() for token in tokens]
        return normalized_tokens



    # sentence = """Thomas Jefferson wasn't began building Monticello at the age of 26."""
    # tokens = tokenize(sentence)

    # remove_stop_words(tokens)
    # normalize_tokens(tokens)

