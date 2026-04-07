# Gemini German Tutor 🇩🇪

An interactive, AI-powered German language learning tool built using the Google Gemini 3 Flash API. This application provides a real-time conversational environment where users can practice their German with immediate feedback and bilingual support.

---

## 📋 Problem Statement

Learning a new language often requires consistent immersion and immediate correction to prevent bad habits from forming. However, many learners face two major hurdles:
1. **Lack of Practice Partners:** Finding a fluent speaker available 24/7 is difficult.
2. **Fear of Mistakes:** Learners are often hesitant to speak in real-life settings due to the fear of being misunderstood or making grammatical errors.

The **Gemini German Tutor** solves this by providing a low-pressure, highly intelligent environment that ensures every interaction is a learning moment through forced bilingual output and instant error correction.

## 🛠 Methodology

The program utilizes the following technical approach:
* **LLM Integration:** Built on the `google-genai` SDK using the `gemini-3-flash-preview` model for high-speed, context-aware responses.
* **System Prompting:** Implements strict behavioral rules via `system_instruction` to ensure the AI maintains its persona as a tutor rather than just a chatbot.
* **Contextual Memory:** Uses the `chats.create` method to maintain session history, allowing the AI to remember previous parts of the conversation.
* **Structured Feedback Loop:** Every response is engineered to follow a specific pattern:
    1.  German response.
    2.  English translation.
    3.  Grammar/Vocabulary correction.
    4.  Engagement via a German follow-up question.

## ✨ Results Achieved

* **Bilingual Immersion:** Successfully maintains a dual-language flow that helps beginners understand the context without leaving the German environment.
* **Instant Pedagogy:** Effectively identifies and corrects common German pitfalls (like cases, verb placement, and gendered nouns) in real-time.
* **High Engagement:** The follow-up question logic ensures that the "conversation loop" never breaks, encouraging longer practice sessions.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* A Google Gemini API Key. You can get one at [Google AI Studio](https://aistudio.google.com/).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gemini-german-tutor.git
   cd gemini-german-tutor
   ```
2. Install the required dependency:
   ```bash
   pip install google-genai
   ```

### Usage
1. Open the script and replace `"YOUR_API_KEY_HERE"` with your actual API key.
2. Run the application:
   ```bash
   python german_tutor.py
   ```
3. Type `exit` or `tschüss` to end the session.

---

## ⚙️ Configuration

The tutor's behavior can be customized within the `types.GenerateContentConfig` section:

| Parameter | Description | Default |
| :--- | :--- | :--- |
| **Temperature** | Controls randomness (0.0 is deterministic, 1.0 is creative) | `0.7` |
| **Model** | The specific Gemini model used | `gemini-3-flash-preview` |
| **System Instruction** | Defines the tutor's personality and rules | See code |

---

## 🤝 Contributing
Contributions are welcome! If you'd like to add features like voice support or specific level-based modules (A1, B2, etc.), please feel free to fork the repo and submit a pull request.

## 📄 License
This project is licensed under the MIT License.
