import nltk
import random
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from flask import Flask, render_template, request, url_for, redirect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aladinh00-010montext'

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    # Tokenize and lower the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords and lemmatize each token
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    
    return tokens

pairs = [
    ["hi|hello|hey|hy|yoh|what's up|hey buddy", ["Hello!", "Hi there!", "Hey!", "Hello, how can I assist you today!"]],
    ["how are you today|how is you|how are you doing|how do you do|how are you", ["I'm doing well, thank you!", "I'm great. How about you?", "I'm cool, so what's up?"]],
    ["who is your developer|who developed you|who is your co-founder|who created you", ["I was developed by Harison.O.O.", "My co-founder is Harison.O.O.", "That's a nice question, I was developed by developer Harison.O.O.", "I was developed by developer Harison.O.O."]],
    ["okay|cool|thanks|thank you|your welcome|ok", ["You're welcome, how can I help you today?", "That's awesome", "I appreciate it, I hope you're cool also"]],
    ["what is your name|what is your identity|how do i call you", ["You can simply call me DNI.", "I'm D.N.I chatbot."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means 'DIGNITY NATURES YOUR IDENTITY', which is a move developed by Dev Aladinh.", "DIGNITY NATURES YOUR IDENTITY", "This is an abbreviation meaning 'Your Dignity Natures Your Identity'"]],
    ["which services do you provide|what are the things you offer|services you offer|things you offer|what do you do", ["I mainly offer services related to technology", "My main focus is to provide you with tech-related things", "I can offer you a variety of things mainly dwelling around tech."]],
    ["quit|q|close|bye|exit|goodbye", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool it was nice interacting with you."]],
    ["who is Harison.O.O|harison is who|who is Harison", ["This name refers to my creator and developer, a computer science student at one of the main universities in Kenya", "Harison is a tech student at Murang'a university in Kenya", "Harison is a coding enthusiast who came up with the idea to develop a chatbot called D.N.I."]],
    ["which programming language were you developed of|which programming language was used in your development", ["I was made using Python language.", "It's primarily based on the Python-Flask framework.", "The base language is Python."]],
    ["what is AI|explain AI|what is artificial intelligence", ["AI stands for Artificial Intelligence, which refers to machines or software mimicking human intelligence.", "Artificial Intelligence involves algorithms that enable machines to solve problems, learn, and make decisions."]],
]

chat_history = []

def chatbot_response(user_input):
    tokens = preprocess(user_input)
    error_message = "OOPS!! The response seems not to be found."
    
    # Loop through pairs and find a match using set intersection
    return next((random.choice(pair[1]) for pair in pairs
                 if any(set(preprocess(keyword)).intersection(tokens) 
                        for keyword in pair[0].lower().split('|'))), error_message)

"""
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load a pre-trained word2vec model (you can download a pre-trained model like GloVe or Word2Vec)
model = Word2Vec.load('word2vec.model')

def preprocess(text):
    # Simple preprocessing like tokenization and lowercasing
    return [word.lower() for word in text.split() if word.isalpha()]

def get_sentence_vector(sentence):
    tokens = preprocess(sentence)
    vectors = [model.wv[word] for word in tokens if word in model.wv]  # Get vectors for each word
    return np.mean(vectors, axis=0) if vectors else None  # Return the average of the word vectors

def chatbot_response(user_input):
    user_vector = get_sentence_vector(user_input)
    if user_vector is None:
        return "Sorry, I didn't understand that."

    best_response = None
    best_similarity = 0
    
    # Example question-response pairs
    pairs = [
        ("what is Python", "Python is a programming language."),
        ("tell me about Python", "Python is a powerful and versatile programming language."),
        ("how are you", "I'm just a program, but thanks for asking!"),
    ]

    for question, response in pairs:
        question_vector = get_sentence_vector(question)
        if question_vector is not None:
            similarity = cosine_similarity([user_vector], [question_vector])[0][0]
            if similarity > best_similarity:
                best_similarity = similarity
                best_response = response

    return best_response if best_response else "Sorry, I couldn't find a match."

"""

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input").strip()
    if not user_input:
        response = "Please enter a valid message"
    else:
        response = chatbot_response(user_input)

    chat_history.append({"user_input": user_input, "response": response})
    
    return render_template("home.html", user_input=user_input, response=response)


@app.route("/history")
def history():    
    return render_template('index.html', chat_history=chat_history)

@app.route("/clear_history", methods=["POST"])
def clear_history():
    global chat_history
    chat_history = []
    return redirect(url_for("history"))

if __name__ == "__main__":
    app.run(debug=True)