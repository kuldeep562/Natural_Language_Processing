import nltk
from nltk.corpus import reuters
from nltk.tokenize import sent_tokenize, word_tokenize

# Ensure necessary corpora are downloaded
nltk.download('reuters')
nltk.download('punkt')

def tokenize_reuters():
    files = reuters.fileids()[:5]  # Using a small subset for demo
    for file_id in files:
        text = reuters.raw(file_id)
        print(f"\n--- File: {file_id} ---")
        sentences = sent_tokenize(text)
        print(f"Sentences: {sentences[:2]}")  # Show first 2
        for sentence in sentences[:2]:
            words = word_tokenize(sentence)
            print(f"Words: {words}")

if __name__ == "__main__":
    tokenize_reuters()
