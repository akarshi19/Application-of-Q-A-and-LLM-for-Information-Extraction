# Application of Q&A and LLM for Information Extraction🤖

This project aims to build a robust system for extracting and analyzing information using advanced techniques such as Natural Language Processing (NLP), sentiment analysis, and numerical data comparison. It includes tools to preprocess text, compare sentence similarities, extract contextual keywords, and analyze sentiment for comprehensive information extraction.

## 📚Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

---

## 💡Features

1. **Text Preprocessing**:
   - Tokenization
   - Lemmatization
   - Stopword removal
2. **Sentence Similarity**:
   - Matrix generation for sentence similarity between two texts.
3. **Keyword Extraction**:
   - Identifies major attributes in sentences for context comparison.
4. **Numerical Data Analysis**:
   - Extracts and compares numerical values between sentences.
5. **Sentiment Analysis**:
   - Analyzes and compares the sentiment of sentences.
6. **Comprehensive Evaluation**:
   - Generates a similarity matrix and a final decision matrix to evaluate text.

## 🔧Technologies Used

- **Python Libraries**:
  - `spacy`: For NLP and text preprocessing.
  - `scikit-learn`: For calculating cosine similarity.
  - `nltk`: For sentiment analysis.
  - `numpy`: For matrix operations.
  - `pandas`: For data handling.

## 🛠️ Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/akarshi19/Application-of-Q-A-and-LLM-for-Information-Extraction.git
   cd Application-of-Q-A-and-LLM-for-Information-Extraction
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the required `spacy` model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Ensure NLTK is fully downloaded:

   ```python
   import nltk
   nltk.download('all')
   ```

## ⚙️How It Works

1. **Preprocess Text**:

   - Tokenizes, lemmatizes, and removes stopwords to prepare the text for analysis.

2. **Compare Sentences**:

   - Computes sentence similarities using TF-IDF vectorization and cosine similarity.

3. **Extract Context**:

   - Identifies common keywords to determine the context of similar sentences.

4. **Numerical and Sentiment Analysis**:

   - Extracts numerical values for comparison.
   - Uses sentiment analysis to evaluate and compare sentence sentiment.

5. **Decision Matrix**:

   - Generates a final matrix that consolidates the results of the analysis.

## 🖥️Usage

Run the provided script by defining two input texts (e.g., historical or comparative data). Below is a snippet to execute the main function:

```python
from main import main

text1 = '''Your first text input.'''
text2 = '''Your second text input.'''

main(text1, text2)
```

## 📝Examples

Example 1: Comparing two education-related texts:

Input:

```plaintext
Text 1: Modi increased the education budget by 20%...
Text 2: Gandhi introduced a new Education budget...
```

Output:

```plaintext
Final_Matrix:-
[           Text1      Text2      Output     ]
[budget     20.0       10.0       1          ]
[school     25.0       100.0      1          ]
...
Entity in Text 1 is better than Entity in Text 2
```

Example 2: Comparing personal traits:

Input:

```plaintext
Text 1: Raman is a good boy...
Text 2: Pathak is a bad boy...
```

Output:

```plaintext
Entity in Text 1 is equal to Entity in Text 2
```

## 📣License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project or raise issues for improvement! Reach out if you have any questions or suggestions.

**Happy Coding!**



