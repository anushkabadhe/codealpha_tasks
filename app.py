import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# FAQ Data
faq_data = {

    "hi":
    "Hello! How can I help you today?",

    "hello":
    "Hi! Welcome to the FAQ Chatbot.",

    "how are you":
    "I am fine. Thank you for asking.",

    "what is your name":
    "I am an AI FAQ Chatbot built using Python and NLP.",

    "who created you":
    "I was created as part of an AI internship project.",

    "bye":
    "Goodbye! Have a great day.",

    "what is ai":
    "AI stands for Artificial Intelligence. It enables machines to simulate human intelligence.",

    "what is machine learning":
    "Machine Learning is a branch of AI that allows systems to learn from data.",

    "what is deep learning":
    "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",

    "what is data science":
    "Data Science is the process of extracting insights from data using statistics and machine learning.",

    "what is nlp":
    "NLP stands for Natural Language Processing. It helps computers understand human language.",

    "what is computer vision":
    "Computer Vision enables computers to understand and analyze images and videos.",

    "what is python":
    "Python is a popular programming language used in AI, web development, and data science.",

    "what is java":
    "Java is an object-oriented programming language widely used for enterprise and Android applications.",

    "what is c language":
    "C is a procedural programming language and the foundation for many modern languages.",

    "what is streamlit":
    "Streamlit is a Python framework used for building web applications quickly.",

    "what is tensorflow":
    "TensorFlow is an open-source machine learning framework developed by Google.",

    "what is pytorch":
    "PyTorch is an open-source deep learning framework developed by Meta.",

    "what is sklearn":
    "Scikit-learn is a Python library used for machine learning tasks.",

    "what is numpy":
    "NumPy is a Python library used for numerical computations and array processing.",

    "what is pandas":
    "Pandas is a Python library used for data manipulation and analysis.",

    "what is matplotlib":
    "Matplotlib is a Python library used for data visualization and plotting graphs.",

    "what is api":
    "API stands for Application Programming Interface. It allows software applications to communicate with each other.",

    "what is database":
    "A database is an organized collection of data stored electronically.",

    "what is sql":
    "SQL stands for Structured Query Language and is used to manage databases.",

    "what is mysql":
    "MySQL is a relational database management system.",

    "what is cloud computing":
    "Cloud computing provides computing resources over the internet.",

    "what is cyber security":
    "Cyber Security protects systems, networks, and data from digital attacks.",

    "what is encryption":
    "Encryption converts data into a secure format that can only be read by authorized users.",

    "what is blockchain":
    "Blockchain is a distributed digital ledger technology.",

    "what is internet of things":
    "IoT refers to interconnected devices that communicate through the internet.",

    "what is big data":
    "Big Data refers to extremely large datasets that require advanced tools for analysis.",

    "what is operating system":
    "An operating system manages computer hardware and software resources.",

    "what is windows":
    "Windows is an operating system developed by Microsoft.",

    "what is linux":
    "Linux is an open-source operating system widely used in servers and development.",

    "what is android":
    "Android is a mobile operating system developed by Google.",

    "what is web development":
    "Web development involves creating websites and web applications.",

    "what is frontend development":
    "Frontend development focuses on the user interface of websites.",

    "what is backend development":
    "Backend development focuses on server-side logic and databases.",

    "what is html":
    "HTML stands for HyperText Markup Language and is used to structure web pages.",

    "what is css":
    "CSS stands for Cascading Style Sheets and is used for styling web pages.",

    "what is javascript":
    "JavaScript is a programming language used to make web pages interactive.",

    "what is react":
    "React is a JavaScript library used for building user interfaces.",

    "what is git":
    "Git is a distributed version control system.",

    "what is github":
    "GitHub is a platform used for hosting and managing Git repositories.",

    "what is software testing":
    "Software testing is the process of evaluating software to identify defects.",

    "what is agile":
    "Agile is a software development methodology focused on iterative development.",

    "what is data structure":
    "A data structure is a way of organizing and storing data efficiently.",

    "what is algorithm":
    "An algorithm is a step-by-step procedure used to solve a problem.",

    "what is chatbot":
    "A chatbot is a software application that simulates human conversation.",

    "what is cosine similarity":
    "Cosine similarity measures the similarity between two text vectors.",

    "what is tfidf":
    "TF-IDF is a technique used to convert text into numerical vectors for NLP tasks."
}


# Text Preprocessing Function
def preprocess(text):
    return text.lower().strip()


# Extract Questions
questions = list(faq_data.keys())

# Process Questions
processed_questions = [
    preprocess(question)
    for question in questions
]


# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)


# Function to Find Best Answer
def get_answer(user_question):

    processed_input = preprocess(user_question)

    input_vector = vectorizer.transform(
        [processed_input]
    )

    similarity_scores = cosine_similarity(
        input_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    return faq_data[
        questions[best_match_index]
    ]


# Streamlit UI
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 FAQ Chatbot")

st.write(
    "Ask questions about AI, Python, Machine Learning, NLP, Data Science, etc."
)

user_question = st.text_input(
    "Enter Your Question"
)

if st.button("Ask"):

    if user_question.strip() != "":

        answer = get_answer(
            user_question
        )

        st.success(answer)

    else:

        st.warning(
            "Please enter a question."
        )