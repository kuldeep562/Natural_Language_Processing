import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = nltk.word_tokenize(text)
    return " ".join(tokens)

def pipeline_example():
    raw_docs = [
        "This product is amazing! Loved it!! 😍",
        "Worst purchase ever. Waste of money. :(",
    ]

    cleaned_docs = [preprocess(doc) for doc in raw_docs]
    vectorizer = CountVectorizer()
    features = vectorizer.fit_transform(cleaned_docs)

    print("Cleaned Docs:", cleaned_docs)
    print("Features Shape:", features.shape)
    print("Vocabulary:", vectorizer.get_feature_names_out())

if __name__ == "__main__":
    pipeline_example()
