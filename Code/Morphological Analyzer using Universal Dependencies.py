import spacy

# Download language model (first time use)
# python -m spacy download en_core_web_sm

def morphological_analysis(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for token in doc:
        print(f"{token.text:<12} | Lemma: {token.lemma_:<12} | POS: {token.pos_:<10} | Morph: {token.morph}")

if __name__ == "__main__":
    sample = "The children are playing in the park while their parents are watching."
    morphological_analysis(sample)
