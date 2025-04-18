import spacy

# Load spaCy NER model
def named_entity_recognition(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text} -> {ent.label_}")

if __name__ == "__main__":
    sample = "Barack Obama was born in Hawaii and became the President of the United States."
    named_entity_recognition(sample)
