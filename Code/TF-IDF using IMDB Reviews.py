from sklearn.feature_extraction.text import TfidfVectorizer
import os

def load_imdb_subset():
    # Assume you have IMDB dataset downloaded locally in ./aclImdb/train/pos and ./neg
    pos_dir = "./aclImdb/train/pos"
    neg_dir = "./aclImdb/train/neg"
    texts = []
    for f in os.listdir(pos_dir)[:5]:
        with open(os.path.join(pos_dir, f), encoding="utf8") as file:
            texts.append(file.read())
    return texts

def tfidf_vectorization():
    docs = load_imdb_subset()
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)
    print("TF-IDF Shape:", X.shape)
    print("Top Words:", vectorizer.get_feature_names_out()[:10])

if __name__ == "__main__":
    tfidf_vectorization()
