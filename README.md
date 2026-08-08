# 🌱 BuddyAI

**A friendly AI companion for talking, practicing communication, and taking a breath.**

BuddyAI is an AI companion designed to provide a comfortable space where people can talk openly, express themselves, practice conversations, and get encouragement without fear of judgment.

The goal isn't to replace real friendships or human relationships. Instead, BuddyAI is designed to help people become more comfortable expressing themselves and communicating with others.

## Features

* Natural, conversational interaction
* Remembers the current conversation
* Friendly and respectful AI personality
* Communication practice
* English conversation practice
* Stress-relief conversations
* Talk-it-out mode for expressing thoughts
* Sort-it-out mode for thinking through problems
* Distraction mode for taking your mind off things
* Conversation starter prompts
* New conversation option

## Why BuddyAI?

Many people find it difficult to talk openly with others.

Sometimes they are afraid of being judged, don't know how to start a conversation, or simply need a comfortable space to organize their thoughts.

BuddyAI aims to provide a low-pressure environment where users can:

* Express what they are feeling
* Practice communicating with others
* Improve conversational confidence
* Practice English naturally
* Take a break from stressful thoughts
* Think through everyday problems

BuddyAI is a companion for conversation and practice, not a replacement for real-world relationships or professional help.

## Tech Stack

* **Python**
* **Streamlit** — Web application interface
* **Groq API** — LLM inference
* **Llama 3.3 70B** — Language model
* **python-dotenv** — Environment variable management

## Project Structure

```text
BuddyAI/
│
├── app.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

## Run BuddyAI Locally

### 1. Clone the repository

```bash
git clone https://github.com/Vyshnavi-Pati/Buddy-AI
cd BuddyAI
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your environment file

Create a `.env` file in the project folder:

```text
GROQ_API_KEY=your_groq_api_key_here
```

You need to provide your own Groq API key.

**Never commit your `.env` file or expose your API key publicly.**

### 5. Run the application

```bash
streamlit run app.py
```

BuddyAI will then open in your browser.

## Privacy & API Keys

The repository does not contain a Groq API key.

The API key should be stored as an environment variable and never committed to GitHub.

The hosted version uses a server-side API key, while anyone running the project locally should use their own API key.

Avoid sharing passwords, financial information, or other highly sensitive personal information with the application.

## Live Demo

**Try BuddyAI:** https://buddy-ai-bw79mv532plmnhuqewq2mh.streamlit.app/

## Source Code

**GitHub:** https://github.com/Vyshnavi-Pati/Buddy-AI

## Project Status

BuddyAI is currently a working project with a deployed web application.

Future improvements may include:

* More personalized conversation modes
* Better long-term memory controls
* Additional communication practice scenarios
* Improved response handling
* More privacy-focused deployment options
* Additional language-learning capabilities

## Disclaimer

BuddyAI is an AI companion and communication practice tool.

It is not a human, therapist, doctor, counselor, or replacement for professional support or real-world relationships.

If someone is experiencing serious emotional distress or immediate danger, they should seek appropriate real-world help.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Built with Python, Streamlit, and Groq.
