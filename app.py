from flask import Flask, render_template, request, url_for, redirect
from fuzzywuzzy import process
import logging, random

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aladinh00-010montext'

"""
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
"""
    
pairs = [
    ("what is Python", ["Python is a programming language.", "Python is known for its simplicity and versatility.", "Python is used for web development, AI, and more."]),
    ("tell me about Python", ["Python is a powerful and versatile programming language.", "Python is great for beginners and professionals alike.", "Python is often used in data science and automation."]),
    ("how are you", ["I'm just a program, but thanks for asking!", "I’m doing great, how about you?", "I'm fully operational, thanks for asking!"]),
    ("hi", ["Hello!", "Hi there!", "Hey, how can I assist you today?"]),
    ("who is your developer", ["I was developed by Harison.O.O.", "Harison.O.O is my creator, a tech enthusiast.", "I owe my existence to Harison.O.O."]),
    ("what is your name", ["You can simply call me DNI AI.", "My name is DNI AI.", "I'm known as D.N.I AI."]),
]

chat_history = []
questions = [question for question, _ in pairs]

def chatbot_response(user_input):
    # Get the best match for the user input
    best_match = process.extractOne(user_input, questions)
    best_question, score = best_match
    
    # If the score is high enough, return the corresponding response
    if score >= 70: 
        index = questions.index(best_question)
        return random.choice(pairs[index][1]) # Pick a random response from the list
    
    return "Sorry, I couldn't find a response."

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