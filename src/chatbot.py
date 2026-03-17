import joblib
from src.answers import INTENT_RESPONSES


class CollegeSubjectsChatbot:
    def __init__(self):
        self.model = joblib.load("models/chatbot_model.pkl")
        self.encoder = joblib.load("models/label_encoder.pkl")
        self.vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

    def predict_intent(self, question):
        question_vec = self.vectorizer.transform([question])
        pred = self.model.predict(question_vec)[0]
        intent = self.encoder.inverse_transform([pred])[0]
        return intent

    def get_response(self, question):
        intent = self.predict_intent(question)
        response = INTENT_RESPONSES.get(intent, "Sorry, I don't know the answer.")
        return intent, response