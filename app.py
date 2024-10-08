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
    ["how are you today|how are you doing|how are you", ["I'm doing well, thank you!", "I'm great. How about you?", "I'm cool, so what's up?"]],
    ["who is your developer|who developed you|who is your co-founder|who created you", ["I was developed by Harison.O.O.", "My co-founder is Harison.O.O.", "That's a nice question, I was developed by developer Harison.O.O.", "I was developed by developer Harison.O.O."]],
    ["okay|cool|thanks|thank you|your welcome|ok", ["You're welcome, how can I help you today?", "That's awesome", "I appreciate it, I hope you're cool also"]],
    ["what is your name|what is your identity|how do i call you", ["You can simply call me DNI.", "I'm D.N.I chatbot."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means 'DIGNITY NATURES YOUR IDENTITY', which is a move developed by Dev Aladinh.", "DIGNITY NATURES YOUR IDENTITY", "This is an abbreviation meaning 'Your Dignity Natures Your Identity'"]],
    ["which services do you provide|what are the things you offer|services you offer|things you offer|what do you do", ["I mainly offer services related to technology", "My main focus is to provide you with tech-related things", "I can offer you a variety of things mainly dwelling around tech."]],
    ["quit|q|close|bye|goodbye", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool it was nice interacting with you."]],
    ["who is Harison.O.O|harison is who|who is Harison", ["This name refers to my creator and developer, a computer science student at one of the main universities in Kenya", "Harison is a tech student at Murang'a university in Kenya", "Harison is a coding enthusiast who came up with the idea to develop a chatbot called D.N.I."]],
    ["which programming language were you developed of|which programming language was used in your development", ["I was made using Python language.", "It's primarily based on the Python-Flask framework.", "The base language is Python."]],
]

chat_history = []

def chatbot_response(user_input):
    tokens = preprocess(user_input)  # Preprocess the user's input
    response = None
    error_message = "OOPS!! The text seems not to be found in the database."
    
    for pair in pairs:
        keywords = pair[0].lower().split('|')  # Get the pattern keywords
        for keyword in keywords:
            keyword_tokens = preprocess(keyword)  # Preprocess the keyword as well
            # Check if there's an overlap between the tokens in the user input and the keyword tokens
            if any(token in tokens for token in keyword_tokens):
                response = random.choice(pair[1])  # Select a random response from matched pair
                return response  # Return the response immediately after finding a match
    
    # If no response is found, return the error message
    return error_message


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