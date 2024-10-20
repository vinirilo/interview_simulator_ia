from flask import Flask, render_template, request, jsonify
import openai
import pyttsx3
import os
import uuid
import datetime
import spacy

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = 'your-api-key-here'

# Initialize pyttsx3 for text-to-speech and SpaCy for language processing
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")

# Create directories if they don't exist
AUDIO_DIR = os.path.join('static', 'audio')
LOG_DIR = os.path.join('logs')
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, 'conversation_log.txt')

# List of filler words for fluency analysis
FILLER_WORDS = ['uh', 'um', 'like', 'you know', 'so']

# Logging function
def log_conversation(user_question, gpt_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{timestamp} - Me: {user_question}\n")
        log_file.write(f"{timestamp} - GPT: {gpt_response}\n\n")

# Generate audio from text
def generate_audio(text, prefix):
    audio_filename = f"{prefix}_{uuid.uuid4()}.mp3"
    audio_path = os.path.join(AUDIO_DIR, audio_filename)
    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    return audio_filename

# GPT integration
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Analyze speech for feedback using SpaCy
def analyze_speech(text):
    feedback = []
    
    # Fluency analysis
    filler_word_count = sum(text.lower().count(word) for word in FILLER_WORDS)
    if filler_word_count > 0:
        feedback.append(f"You used {filler_word_count} filler word(s), which can affect fluency.")
    else:
        feedback.append("Great! No filler words detected, indicating good fluency.")
    
    # Using SpaCy for advanced analysis
    doc = nlp(text)
    sentence_count = len(list(doc.sents))
    if sentence_count > 1:
        feedback.append(f"Your speech had {sentence_count} sentences, which shows variety in sentence structure.")
    else:
        feedback.append("Try to use more complex sentence structures to improve sentence variety.")
    
    noun_count = sum(1 for token in doc if token.pos_ == "NOUN")
    verb_count = sum(1 for token in doc if token.pos_ == "VERB")
    adj_count = sum(1 for token in doc if token.pos_ == "ADJ")
    adv_count = sum(1 for token in doc if token.pos_ == "ADV")
    feedback.append(f"Your speech included {noun_count} nouns, {verb_count} verbs, {adj_count} adjectives, and {adv_count} adverbs.")
    
    linking_words = [token.text for token in doc if token.dep_ in ['cc', 'mark']]
    if linking_words:
        feedback.append(f"You used the following linking words: {', '.join(linking_words)}.")
    else:
        feedback.append("Consider using more linking words to improve flow.")
    
    return ' '.join(feedback)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.json.get("question")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    if "please give me feedback" in user_question.lower():
        feedback = analyze_speech(user_question)
        return jsonify({"response": feedback, "user_audio_url": None, "gpt_audio_url": None})

    prompt = f"I am preparing for an interview. The user asked: {user_question}. Respond like an interviewer."
    gpt_response = chat_with_gpt(prompt)
    log_conversation(user_question, gpt_response)

    user_audio_filename = generate_audio(user_question, 'user')
    gpt_audio_filename = generate_audio(gpt_response, 'gpt')

    return jsonify({
        "response": gpt_response,
        "user_audio_url": f"/static/audio/{user_audio_filename}",
        "gpt_audio_url": f"/static/audio/{gpt_audio_filename}"
    })

if __name__ == '__main__':
    app.run(debug=True)