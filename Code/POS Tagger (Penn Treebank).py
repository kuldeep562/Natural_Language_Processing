import nltk
from nltk.corpus import treebank

nltk.download('treebank')

def pos_tagging():
    sentences = treebank.tagged_sents()[:5]
    for sent in sentences:
        print(sent)

if __name__ == "__main__":
    pos_tagging()
