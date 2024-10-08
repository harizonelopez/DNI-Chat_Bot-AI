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
    ["who is Harison.O.O|harison is who|who is Harison", ["This name refers to my creator and developer, a computer science student at one of the main universities in Kenya", "Harison is a tech student at Murang'a university in Kenya", "Harison is a coding enthusiast who came up with the idea to develop a chatbot called D.N.I."]],
    ["hi|hello|hey|hy|yoh what's up|hey buddy", ["Hello!", "Hi there!", "Hey!", "Hello, how can I assist you today!"]],
    ["how are you|how are you today|how are you doing", ["I'm doing well, thank you!", "I'm great. How about you?", "I'm cool, so what's up?"]],
    ["okay|cool|thanks|thank you|your welcome|ok", ["You're welcome, how can I help you today?", "That's awesome", "I appreciate it, I hope you're cool also"]],
    ["what is your name|what is your identity|how do i call you", ["You can simply call me DNI.", "I'm D.N.I chatbot."]],
    ["which services do you provide|what are the things you offer|services you offer|things you offer|what do you do", ["I mainly offer services related to technology", "My main focus is to provide you with tech-related things", "I can offer you a variety of things mainly dwelling around tech."]],
    ["quit|q|close", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool, it was nice interacting with you."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means 'DIGNITY NATURES YOUR IDENTITY', which is a move developed by Dev Aladinh.", "DIGNITY NATURES YOUR IDENTITY", "This is an abbreviation meaning 'Your Dignity Natures Your Identity'"]],
    ["which programming language were you developed of|which programming language was used in your development", ["I was made using Python language.", "It's primarily based on the Python-Flask framework.", "The base language is Python."]],
    ["who is your developer|who developed you|who is your co-founder|who created you", ["I was developed by Harison.O.O.", "My co-founder is Harison.O.O.", "That's a nice question, I was developed by developer Harison.O.O.", "I was developed by developer Harison.O.O."]],
]

chat_history = []

def chatbot_response(user_input):
    tokens = preprocess(user_input)  # Preprocess the user's input
    response = None
    error_message = "OOPS!! The text seems not to be found in the database."
    
    # Iterate through the pairs to find a matching pattern
    for pair in pairs:
        keywords = pair[0].lower().split('|')  # Get the pattern keywords
        for keyword in keywords:
            keyword_tokens = preprocess(keyword)  # Preprocess the keyword as well
            if set(keyword_tokens).issubset(set(tokens)):  # Check if keyword tokens match user tokens
                response = random.choice(pair[1])
                break
        if response:
            break
    
    # If no response is found, return the error message
    if not response:
        response = error_message
    
    return response


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