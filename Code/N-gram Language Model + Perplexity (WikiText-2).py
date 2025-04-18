import nltk
from nltk.util import ngrams
from nltk import word_tokenize
import math

nltk.download('punkt')

def calculate_perplexity(ngrams_list, ngram_freq, total):
    perplexity = 1
    N = len(ngrams_list)
    for ngram in ngrams_list:
        prob = ngram_freq.get(ngram, 1) / total
        perplexity *= 1 / prob
    return perplexity ** (1/N)

def ngram_model(text, n=2):
    tokens = word_tokenize(text.lower())
    ngrams_list = list(ngrams(tokens, n))
    freq_dist = nltk.FreqDist(ngrams_list)
    total = sum(freq_dist.values())

    print(f"Sample {n}-gram:", ngrams_list[:5])
    print("Perplexity:", calculate_perplexity(ngrams_list, freq_dist, total))

if __name__ == "__main__":
    sample = "The quick brown fox jumps over the lazy dog. The dog barked back."
    ngram_model(sample, n=2)
