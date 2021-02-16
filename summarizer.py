import re
import urllib.request as urllib2
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarizer():
    response = urllib2.urlopen('https://en.wikipedia.org/wiki/Los_Angeles')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    article = ""
    for i in soup.find_all('p'):
        article += i.text
    article = re.sub(r'\[[0-9]*\]', ' ', article)

    parser = PlaintextParser.from_string(article, Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    lexrank_summary = lex_rank_summarizer(parser.document, sentences_count=10)
    final_version = ""
    for sentence in lexrank_summary:
        final_version += str(sentence)
    return final_version

print(summarizer())