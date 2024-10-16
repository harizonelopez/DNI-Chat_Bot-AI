from flask import Flask, render_template, url_for, redirect, request
from fuzzywuzzy import process
import logging, random

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aladinh00-010montext'
    
pairs = [
    # Basic greetings and interactions
    ("hi|yoh|yoh man|hy|hello|hey", ["Hello!", "Hi there!", "Hey, how can I assist you today?", "Hi! What's up?"]),
    ("how are you", ["I'm just a program, but thanks for asking!", "I’m doing great, how about you?", "I'm fully operational, thanks for asking!"]),
    ("good morning|morning", ["Good morning! How can I help you today?", "Morning! I hope you have a great day!", "Good morning, ready to learn something new?"]),
    ("good night|night", ["Good night! Take care.", "Good night, talk to you soon!", "Good night, don't let the bugs bite (the programming kind)!"]),

    # Python-related questions
    ("what is Python", ["Python is a programming language.", "Python is known for its simplicity and versatility.", "Python is used for web development, AI, and more."]),
    ("tell me about Python", ["Python is a powerful and versatile programming language.", "Python is great for beginners and professionals alike.", "Python is often used in data science and automation."]),
    ("what can you do with Python", ["You can build web apps, automate tasks, analyze data, and more.", "Python is used in AI, machine learning, web development, and scripting.", "Python’s flexibility allows it to be used in almost any software project."]),
    ("who uses Python", ["Developers, data scientists, and even non-programmers use Python.", "Python is popular among software developers, researchers, and startups.", "From Google to Netflix, many companies use Python for various tasks."]),
    
    # Tech-related questions
    ("what is AI|explain AI|what is artificial intelligence", ["AI stands for Artificial Intelligence, which refers to machines mimicking human intelligence.", "AI involves algorithms that enable machines to solve problems, learn, and make decisions.", "Artificial Intelligence can be seen in things like chatbots, recommendation systems, and self-driving cars."]),
    ("what is machine learning", ["Machine learning is a branch of AI where systems learn from data without being explicitly programmed.", "Machine learning allows computers to learn patterns and make predictions based on data.", "Machine learning algorithms are used in things like recommendation engines and speech recognition."]),
    ("what is data science", ["Data science is a field focused on extracting insights from data.", "Data scientists use statistics, programming, and machine learning to analyze data.", "It’s all about using data to make better decisions or build intelligent systems."]),
    ("what is cloud computing", ["Cloud computing is the delivery of services like storage and computing power over the internet.", "With cloud computing, you can access services on-demand without owning the infrastructure.", "Cloud computing is used for scalable solutions like hosting websites or apps."]),

    # Chatbot-specific questions
    ("who is your developer|who developed you", ["I was developed by Harison.O.O.", "Harison.O.O is my creator, a tech enthusiast.", "I owe my existence to Harison.O.O."]),
    ("what is your name", ["You can simply call me DNI AI.", "I'm known as DNI AI.", "My name is DNI AI, nice to meet you."]),
    ("who created you", ["I was developed by Harison.O.O.", "I’m the brainchild of Harison.O.O.", "Harison.O.O is the one who built me."]),

    # General knowledge questions
    ("what is the internet", ["The internet is a global network of interconnected computers.", "The internet allows information to be shared worldwide instantly.", "It’s the system that connects millions of computers globally, allowing for communication and information exchange."]),
    ("what is a computer", ["A computer is an electronic device that processes data.", "Computers are used to perform calculations, store data, and run applications.", "A computer can execute instructions to perform a variety of tasks."]),
    ("what is a website", ["A website is a collection of web pages accessed via the internet.", "Websites can contain information, media, or provide services online.", "It’s a location on the internet containing one or more web pages accessible via a URL."]),
    
    # Farewell phrases
    ("goodbye|bye|see you", ["Goodbye!", "Bye! Hope to talk again soon.", "See you later!", "Take care, until next time!"]),
    ("quit|exit|q|close", ["Goodbye!", "Closing now, take care!", "Bye! Hope to see you again soon."]),
    
    # Questions about the chatbot’s abilities
    ("what can you do", ["I can help answer questions about programming and technology.", "I’m here to assist you with tech-related queries.", "I can chat with you, answer questions, and provide tech knowledge."]),
    ("what services do you provide|how can you help", ["I can help answer programming questions, especially about Python and technology.", "I’m a chatbot designed to assist with tech-related questions.", "I provide information and help with various programming and tech queries."]),
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

@app.route("/clear_history")
def clear_history():
    global chat_history
    chat_history = []
    return redirect(url_for("history"))

if __name__ == "__main__":
    app.run(debug=True)