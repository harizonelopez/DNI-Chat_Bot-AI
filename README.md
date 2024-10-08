# D.N.I. Chatbot

**D.N.I. (Dignity Natures Your Identity) Chatbot** is a simple web-based chatbot application developed using Python and the Flask framework. The chatbot is designed to handle basic conversational interactions using predefined responses and NLTK's `Chat` utility.

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
- **Clear History**: Provides an option to clear the chat history.

## Installation

### Prerequisites

- Python 3.x
- Flask
- NLTK (Natural Language Toolkit)

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

## Usage

- Navigate to the home page of the chatbot and start typing your messages.
- The chatbot will respond based on predefined patterns.


]
