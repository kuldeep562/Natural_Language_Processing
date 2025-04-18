import nltk
from nltk.corpus import brown
from nltk.stem import PorterStemmer

nltk.download('brown')

def stem_brown_corpus():
    stemmer = PorterStemmer()
    words = brown.words(categories='news')[:100]
    for word in words:
        print(f"{word} -> {stemmer.stem(word)}")

if __name__ == "__main__":
    stem_brown_corpus()
