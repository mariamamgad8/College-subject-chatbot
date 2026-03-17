import streamlit as st
from src.chatbot import CollegeSubjectsChatbot

st.set_page_config(page_title="College Subjects Chatbot", page_icon="🎓", layout="centered")

@st.cache_resource
def load_bot():
    return CollegeSubjectsChatbot()

bot = load_bot()

st.title("🎓 College Subjects Chatbot")
st.write("Ask a question about machine learning concepts.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_question = st.text_input("Enter your question")

if st.button("Ask") and user_question.strip():
    intent, response = bot.get_response(user_question)
    st.session_state.chat_history.append(
        {
            "question": user_question,
            "intent": intent,
            "response": response
        }
    )

if st.session_state.chat_history:
    st.subheader("Chat History")
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Predicted Intent:** `{chat['intent']}`")
        st.markdown(f"**Bot:** {chat['response']}")
        st.divider()