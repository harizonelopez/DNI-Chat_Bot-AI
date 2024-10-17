# DNI AI Chatbot

**DNI (Dignity Natures Your Identity) Chatbot** is a simple web-based chatbot application developed using Python and the Flask framework. The chatbot is designed to handle the conversational interactions using predefined responses by use of fuzzywuzzy process response utility.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)


## Project Overview

D.N.I. Chatbot is a Flask web application that simulates a simple conversation with users. It responds to user input based on predefined rules and can handle basic greetings, information about the chatbot, and other simple queries.

The primary goal of this project is to demonstrate the use of Flask for building a web-based chatbot and how to integrate it with basic natural language processing tools like NLTK.

## Features

- **Simple Conversations**: The chatbot can handle greetings, questions about its identity, and basic information.
- **Predefined Responses**: Uses a set of predefined responses based on keywords and patterns.
- **Chat History**: Displays the chat history for the current session.
- **Contextual Conversations**: Tracks the context of the conversation, allowing for relevant follow-up responses.
- **Learning Mode**: Offers interactive programming-related guidance and explanations, helping users learn Python and technology concepts.
- **Error Handling Assistance**: Helps users troubleshoot programming errors by recognizing common mistakes and offering suggestions.
- **Dynamic Topic Suggestions**: After answering a query, the chatbot can suggest related topics for further exploration.
- **Natural Language Programming**: Users can describe tasks in natural language, and the chatbot translates them into Python code snippets.


## Installation

### Prerequisites

- Python 3.x
- Flask
- fuzzywuzzy

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/harizonelopez/dni-chatbot.git
    cd dni-chatbot
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/Scripts/activate  # On Mac use `venv\bin\activate`
    ```

3. **Install the Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    python app.py
    ```

5. **Access the Application**:

    Open your web browser and go to `http://127.0.0.1:5000`