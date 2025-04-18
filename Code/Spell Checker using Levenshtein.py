from difflib import get_close_matches

def spell_checker(word, dictionary):
    suggestions = get_close_matches(word, dictionary, n=3, cutoff=0.7)
    return suggestions if suggestions else ["No suggestion"]

if __name__ == "__main__":
    dictionary = ["apple", "banana", "orange", "mango", "grape"]
    test_words = ["appel", "banan", "ornge", "grap"]

    for word in test_words:
        print(f"Input: {word} -> Suggestions: {spell_checker(word, dictionary)}")
