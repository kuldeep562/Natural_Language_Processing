from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def classify_news():
    data = fetch_20newsgroups(subset='all', categories=['sci.space', 'rec.sport.baseball'])
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)

    print(classification_report(y_test, y_pred, target_names=data.target_names))

if __name__ == "__main__":
    classify_news()
