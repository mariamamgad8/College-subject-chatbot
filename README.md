# College Subjects Chatbot

Machine learning chatbot that answers common questions about machine learning concepts.  
The model classifies user questions into intents and returns the corresponding explanation.

---

## Project Structure

```
college-subjects-chatbot/

data/
    college_subjects_chatbot_dataset.csv

notebooks/
    project_workflow.ipynb

models/
    chatbot_model.pkl
    label_encoder.pkl
    tfidf_vectorizer.pkl

src/
    answers.py
    chatbot.py

app.py
streamlit_app.py
requirements.txt
README.md
```

---

## Install Requirements

```
pip install -r requirements.txt
```

or

```
python -m pip install -r requirements.txt
```

---

## Run Terminal Chatbot

```
python app.py
```

Example

```
You: what is machine learning
Bot (ml_definition): Machine learning is a branch of artificial intelligence that enables systems to learn patterns from data.
```

---

## Run Web Chatbot (Streamlit)

```
python -m streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Model Files

These files must exist before running the chatbot:

```
models/chatbot_model.pkl
models/label_encoder.pkl
models/tfidf_vectorizer.pkl
```

They are generated in the notebook during training.

---

## Training

All preprocessing, visualization, and model training are done in:

```
notebooks/project_workflow.ipynb
```

The notebook:
- loads the dataset
- cleans text
- creates visualizations
- performs train/test split
- trains the TF-IDF + Logistic Regression model
- evaluates using Accuracy, Precision, Recall, and F1 Score
- saves the trained model files

---

## Technologies

- Python
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Pandas
- NumPy
