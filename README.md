# 🤖 Real-Time Chatbot with Google Gemini API

This is a command-line based chatbot application built in Python using the Google Gemini API (via Vertex AI). The chatbot responds to user queries in real-time, simulating a streaming-like response similar to ChatGPT.

---

## 🚀 Features

- Real-time response to any user prompt.
- Simulates line-by-line typing using a streaming effect.
- Error handling for API rate limits and invalid inputs.
- Simple and clean command-line interface.
- Built with Google Cloud's Gemini 1.5 Pro model via Vertex AI.

---

## 📂 Project Structure

```
gemni/
├── app.py           # Main chatbot interface
├── search.py        # Gemini API integration logic
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gemni-chatbot.git
cd gemni-chatbot
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Set Up Google Cloud Gemini
- Enable Vertex AI API on Google Cloud.
- Generate a service account and download the JSON key.
- Set environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/key.json"
```

---

## 🧠 How to Use

```bash
python app.py
```

Sample interaction:
```
🤖 Real-Time ChatBot (type 'exit' to quit)
You: What is the capital of India?
Bot: The capital of India is New Delhi.
```

---

## 🛠️ Tech Stack

- Python 3.10+
- Google Cloud Vertex AI
- Gemini 1.5 Pro API
- `vertexai` Python SDK

---

## 🧪 Sample Questions for Interviews

> Q: How is this chatbot different from a normal static chatbot?  
> A: It simulates real-time responses and connects to Google Gemini API for intelligent, up-to-date answers.

> Q: What model is used for generating responses?  
> A: Gemini 1.5 Pro, served via Google Vertex AI.

> Q: How do you handle API rate limits or errors?  
> A: The app uses try-except blocks to catch and display API errors like 429 (Resource Exhausted).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## 🙋‍♂️ Author

Built with ❤️ by [Your Name](https://github.com/yourusername)