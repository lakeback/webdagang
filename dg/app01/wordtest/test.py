# import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

text = "NLTK is a powerful Python library for working with human language data."
tokens = word_tokenize(text)
print("Tokens:", tokens)

lemmatizer = WordNetLemmatizer()
wds = lemmatizer.lemmatize('working')
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmatized Tokens:", lemmatized_tokens)
