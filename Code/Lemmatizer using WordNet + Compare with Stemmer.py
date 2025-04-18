import nltk
from nltk.corpus import gutenberg
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def compare_lemmatization():
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    sample = gutenberg.raw('austen-emma.txt')[:1000]
    words = word_tokenize(sample)

    for word in words[:20]:
        print(f"{word} -> Stem: {stemmer.stem(word)} | Lemma: {lemmatizer.lemmatize(word)}")

if __name__ == "__main__":
    compare_lemmatization()
