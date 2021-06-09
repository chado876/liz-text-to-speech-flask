import spacy

nlp = spacy.load('en_core_web_sm')
stopwords = nlp.Defaults.stop_words

def strip_whitespaces(string):
    return " ".join(string.split())


def tokenize(string):
    string = strip_whitespaces(string)
    doc = nlp(string)
    tokens = []
    for token in doc:
        print(token.text)
        tokens.append(token.text)
    return tokens

def remove_stop_words(tokens):
    stop_words = [word for word in tokens if word in stopwords]
    print(stop_words)

tokens = tokenize("        Tesla isn't      looking at      buying U.S. startup for $6 million")
# remove_stop_words(tokens)


