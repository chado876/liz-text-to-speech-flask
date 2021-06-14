from newspaper import Article
import nltk
import speechUtil as speechUtil
from random import randrange
from nlp.lex.lexical_analyzer import LexicalAnalyzer


def process_article(articleLink, treeFileName):
    article = Article(articleLink)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    articleText = article.text
    LexicalAnalyzer.perform_lexical_analysis(articleText, treeFileName)
    randNum = randrange(1,900)
    filename = "article" + str(randNum)
    speechUtil.synthesize_and_save_to_file(articleText, filename)
    return filename
    
