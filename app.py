from flask import Flask, render_template, request, redirect, url_for
import random
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aladinh00-010montext'

pairs = [
    ["who is Harison.O.O|harison is who|who is Harison", ["This name refers to my creator and developer, a computer science student at one of the main universities in Kenya", "Harison is a tech student at Murang'a university in Kenya", "Harison is a coding enthusiast who came up with the idea to develop a chatbot called D.N.I."]],
    ["hi|hello|hey|hy|yoh what's up|hey niggah|hey buddy", ["Hello!", "Hi there!", "Hey!", "Hello, how can I assist you today!"]],
    ["how are you|how are you today|how are you doing", ["I'm doing well, thank you!", "I'm great. How about you?", "I'm cool, so what's up?"]],
    ["okay|cool|thanks|thank you|your welcome|ok", ["Your welcome, how can I help you today", "That's awesome", "I appreciate, I hope you are cool also"]],
    ["what is your name|what is your identity|how do i call you", ["You can simply call me DNI as your wish.", "I'm D.N.I chatbot."]],
    ["which services do you provide|what are the things you offer|services you offer|things you offer|what do you do", ["I mainly offer services related to technology", "My main focus is to provide you with tech related things", "I can offer you with variety of things mainly dwelling around tech."]],
    ["quit|q|close", ["Goodbye!", "Bye!", "Nice chatting with you.", "Cool, it was nice interacting with you."]],
    ["what is DNI|what is D.N.I", ["The word D.N.I simply means 'DIGNITY NATURES YOUR IDENTITY', which is a move developed by Dev Aladinh.", "DIGNITY NATURES YOUR IDENTITY", "This is an abbreviation which means that your Dignity Natures Your Identity"]],
    ["which programming language were you developed of|which programming language was used in  your development", ["I was made using pythoon language", "basically its python-flask framework", "the base language is python"]],
    ["who is your developer|who developed you|who is your co-founder|who created you|who created DNI|who created D.N.I chatbot", ["I'm was developed by Harison.O.O", "My co-founder is Harison.O.O", "That's a nice question, I was developed by developer Harison.O.O", "I was developed by developer Harison.O.O"]],
]

chat_history = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chat():
    error_message = "OOPS!! The text seems not to be found in the database."
    user_input = request.form["user_input"].lower()
    response = None
    
    for pair in pairs:
        keywords = pair[0].lower().split('|')
        for keyword in keywords:
            if keyword in user_input:
                response = random.choice(pair[1])
                return render_template("home.html", user_input=user_input, response=response, error_message=error_message)
    
    chat_history.append({"user_input": user_input, "response": response})
    print(f"Chat history:", chat_history)
    
    return render_template("home.html", user_input=user_input, response=response, error_message=error_message)

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