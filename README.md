# **Interview Simulator with GPT and Feedback Analysis**

This project is a Flask-based web application that simulates interview scenarios using OpenAI's GPT-4 for generating responses. Additionally, the app provides feedback on your speaking fluency, word choice, and sentence structure, utilizing the SpaCy NLP library for advanced analysis.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [How to Run](#how-to-run)
7. [How the App Works](#how-the-app-works)
8. [Libraries and Tools Used](#libraries-and-tools-used)

## **Project Overview**

This application allows users to simulate interview questions by speaking into their microphone or typing questions directly. The app responds using OpenAI's GPT-4, and at the end of the interaction, you can request personalized feedback on your speech. The feedback evaluates your fluency, vocabulary richness, sentence complexity, and the use of linking words.

## **Features**

- **Voice Recognition**: Capture your question via the browser's speech-to-text API.
- **GPT Responses**: Get interview-style answers powered by GPT-4.
- **Speech Feedback**: Receive feedback on fluency, word choice, and linking words using SpaCy NLP analysis.
- **Audio Playback**: Both user input and GPT responses are saved and played back as MP3 files.

## **Prerequisites**

Before installing and running this project, ensure you have the following:

- **Python 3.8+** installed on your machine.
- Basic familiarity with Python virtual environments.
- **Internet Connection** (required for interacting with OpenAI's GPT-4).

## **Installation**

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-repository/interview_simulator.git
cd interview_simulator
```

### 2. **Set Up a Virtual Environment**

To isolate the dependencies, create a virtual environment:

 - On Windows:
 ```bash
 python -m venv venv
```

Activate the virtual environment:

- Windows:
```bash
Copiar código
venv\Scripts\activate
```

### 3. **Install the Required Libraries**
Install the dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
4. Install the SpaCy Language Model
```

This app uses SpaCy's English language model for text analysis. Install it using the following command:

```bash
python -m spacy download en_core_web_sm
```

### 4. **Configuration**
-1. OpenAI API Key

To interact with GPT-4, you'll need an OpenAI API key. Follow these steps:

Sign up at OpenAI.
Generate an API key from the OpenAI dashboard.

In the main.py file, replace the placeholder with your API key:

```bash
openai.api_key = 'your-api-key-here'
```
### 6. **How to Run**
Once the virtual environment is activated and dependencies are installed, run the Flask app:

```bash
python main.py
```

You should see output indicating that the Flask development server is running:
```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

Now, open your web browser and go to http://127.0.0.1:5000/. You should see the web interface where you can start asking interview questions and get responses.

### 7. **How the App Works**
1. `Ask a Question: You can either type your question or use the microphone to speak it.
2. GPT-4 Response: The question is sent to OpenAI's GPT-4, which generates a response as if answering an interview question.
3. Audio Feedback: Both your question and GPT’s response are converted into MP3 files, which can be played back directly on the webpage.
4. Request Feedback: Say or type "please give me feedback" to receive detailed feedback about your speaking fluency, word choice, sentence complexity, and linking words.

#### **Logging:**
- Every conversation (question and response) is logged in a text file (logs/conversation_log.txt) with timestamps.

#### **Speech Feedback:**
- Fluency: Checks for filler words like “um” or “uh.”
- Vocabulary Richness: Analyzes the variety of nouns, verbs, adjectives, and adverbs used.
- Sentence Complexity: Determines whether you use multiple sentences or complex sentence structures.
- Linking Words: Detects the use of conjunctions like “and,” “but,” and “because” to assess the flow of your sentences.

### 8. **Libraries and Tools Used**

1. Flask: A lightweight Python web framework for serving the app.
2. OpenAI GPT-4: Generates interview-style responses.
3. SpaCy: A natural language processing library used for analyzing your speech.
4. pyttsx3: Converts text into speech to create audio feedback.
5. SpeechRecognition: Captures voice input from the user (client-side).

#### **Full List of Dependencies (in requirements.txt):**

```bash 
openai==0.27.0
pyttsx3==2.90
Flask==2.3.2
spacy==3.5.0
```
#### **Troubleshooting**

- OpenAI API issues: Ensure your API key is valid and has sufficient quota. You can check your API usage on the OpenAI dashboard.
- Virtual Environment Activation: Ensure that the virtual environment is activated before running the app (check the command prompt for the (venv) prefix).
- SpaCy Model Issues: If the model isn’t downloaded correctly, try reinstalling it using python -m spacy download en_core_web_sm.

#### **Future Improvements**

- Add more advanced analysis on speaking patterns (e.g., pauses, tone).
- Implement real-time feedback on the frontend while speaking.
- Expand language support for feedback in other languages.

### **File Structure**

```bash
/interview_simulator/
│
├── /static/
│   └── /audio/                       # Stores generated audio files
│
├── /logs/                            # Stores conversation logs
│   └── conversation_log.txt          # Text log of user and GPT interactions
│
├── /templates/
│   └── index.html                    # The main HTML template for the front-end
│
├── main.py                           # Flask app with GPT integration, logging, and feedback analysis
├── requirements.txt                  # List of dependencies for Python environment
└── README.md                         # Detailed instructions for running the app
```