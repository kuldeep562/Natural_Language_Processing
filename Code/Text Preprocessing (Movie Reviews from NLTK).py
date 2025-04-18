import nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_movie_reviews():
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    fileids = movie_reviews.fileids()[:3]
    for fileid in fileids:
        words = movie_reviews.words(fileid)
        filtered = [w for w in words if w.lower() not in stop_words]
        tokens = word_tokenize(" ".join(filtered[:100]))
        print("\n--- Preprocessed ---")
        for w in tokens[:10]:
            print(f"{w} -> Stem: {stemmer.stem(w)}, Lemma: {lemmatizer.lemmatize(w)}")

if __name__ == "__main__":
    preprocess_movie_reviews()
