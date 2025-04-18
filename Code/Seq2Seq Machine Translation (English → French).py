import torch
from transformers import MarianMTModel, MarianTokenizer

def translate_en_to_fr(text):
    model_name = 'Helsinki-NLP/opus-mt-en-fr'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)
    return output

if __name__ == "__main__":
    english_text = "Hello, how are you doing today?"
    french = translate_en_to_fr(english_text)
    print("English:", english_text)
    print("French:", french)
