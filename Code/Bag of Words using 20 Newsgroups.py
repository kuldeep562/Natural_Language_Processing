from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer

def bow_model():
    data = fetch_20newsgroups(subset='train', categories=['rec.sport.hockey', 'sci.space'])
    vectorizer = CountVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(data.data[:5])

    print("Feature Names:", vectorizer.get_feature_names_out()[:10])
    print("BoW Shape:", vectors.shape)

if __name__ == "__main__":
    bow_model()
