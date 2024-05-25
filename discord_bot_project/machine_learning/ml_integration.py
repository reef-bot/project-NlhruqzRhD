# ml_integration.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

class MLIntegration:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = RandomForestClassifier()
        
    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
        return ' '.join(stemmed_tokens)
    
    def train_model(self, X_train, y_train):
        X_train_processed = [self.preprocess_text(text) for text in X_train]
        X_train_vectorized = self.vectorizer.fit_transform(X_train_processed)
        self.classifier.fit(X_train_vectorized, y_train)
        # Save the trained model
        with open('model.pkl', 'wb') as model_file:
            pickle.dump(self.classifier, model_file)
        with open('vectorizer.pkl', 'wb') as vectorizer_file:
            pickle.dump(self.vectorizer, vectorizer_file)
    
    def predict(self, text):
        text_processed = self.preprocess_text(text)
        text_vectorized = self.vectorizer.transform([text_processed])
        with open('model.pkl', 'rb') as model_file:
            self.classifier = pickle.load(model_file)
        prediction = self.classifier.predict(text_vectorized)
        return prediction

# End of ml_integration.py