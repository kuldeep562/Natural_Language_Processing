from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

def sentiment_analysis():
    # Download dataset manually from https://ai.stanford.edu/~amaas/data/sentiment/
    data = load_files("aclImdb/train/", categories=["pos", "neg"], encoding="utf-8")
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))

if __name__ == "__main__":
    sentiment_analysis()
