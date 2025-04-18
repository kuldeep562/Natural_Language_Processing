# NLP Practical Assignment II – 2024

This repository contains implementations of ten practical Natural Language Processing (NLP) tasks as part of the assignment for the Department of Computer Science, Gujarat University.

## 📁 Repository Structure

```
nlp-practical-assignment-ii-2024/
│
├── LICENSE
├── README.md
├── requirements.txt
├── datasets/
│   └── README.md
│
├── task_01_tokenizer/
├── task_02_stemming/
├── task_03_lemmatizer/
├── task_04_bow/
├── task_05_tfidf/
├── task_06_morphological_analyzer/
├── task_07_regex_patterns/
├── task_08_edit_distance/
├── task_09_preprocessing_pipeline/
└── task_10_spell_checker/
```

Each `task_xx_*` folder contains the Python implementation of the corresponding NLP task.

## ✅ Task Descriptions

1. **Tokenizer**  
   Split a text into sentences and words.  
   Dataset: [Reuters-21578](https://archive.ics.uci.edu/ml/datasets/reuters-21578+text+categorization+collection)

2. **Stemming**  
   Apply the Porter Stemming algorithm.  
   Dataset: [Brown Corpus](https://www.nltk.org/nltk_data/)

3. **Lemmatizer**  
   Use WordNet lemmatizer and compare with stemming.  
   Dataset: [Gutenberg Corpus](https://www.nltk.org/nltk_data/)

4. **Bag of Words (BoW)**  
   Convert documents into numerical vectors.  
   Dataset: [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/)

5. **TF-IDF**  
   Extract important text features using TF-IDF.  
   Dataset: [IMDB Movie Reviews](https://ai.stanford.edu/~amaas/data/sentiment/)

6. **Morphological Analyzer**  
   Identify root forms and morphological features.  
   Dataset: [Universal Dependencies](https://universaldependencies.org/)

7. **Regex Pattern Extraction**  
   Extract emails, dates, etc., using regular expressions.  
   Dataset: [Enron Email Dataset](https://www.cs.cmu.edu/~enron/)

8. **Levenshtein Edit Distance**  
   Compare pairs of words using edit distance.  
   Dataset: [WordNet](https://wordnet.princeton.edu/) or custom dataset.

9. **Text Preprocessing Pipeline**  
   Includes tokenization, normalization, and vectorization.  
   Dataset: [Amazon Reviews](https://registry.opendata.aws/amazon-reviews/)

10. **Spell Checker**  
    Suggest corrections using edit distance.  
    Dataset: [Birkbeck Spelling Error Corpus](http://ota.ox.ac.uk/desc/2464)

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nlp-practical-assignment-ii-2024.git
   cd nlp-practical-assignment-ii-2024
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Run individual task scripts located inside `task_xx_*` folders.

## 📄 License

See [LICENSE](LICENSE) for license details.
