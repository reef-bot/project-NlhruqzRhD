# content_scanner.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

class ContentScanner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer()
        self.classifier = RandomForestClassifier()

    def preprocess_text(self, text):
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalnum() and word not in self.stop_words]
        return ' '.join(words)

    def train_model(self, messages, labels):
        preprocessed_messages = [self.preprocess_text(message) for message in messages]
        X = self.vectorizer.fit_transform(preprocessed_messages)
        self.classifier.fit(X, labels)

    def predict(self, message):
        preprocessed_message = self.preprocess_text(message)
        X = self.vectorizer.transform([preprocessed_message])
        prediction = self.classifier.predict(X)
        return prediction[0]

# End of content_scanner.py