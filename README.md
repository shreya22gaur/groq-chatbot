# 🤖 Groq AI Chatbot

Live Project Link - https://groq-chatbot-8zua.onrender.com/

A simple AI chatbot built using **Flask** and the **Groq API**. The application features a clean web interface where users can interact with an AI assistant powered by Groq's fast LLM inference.

## 🚀 Features

* 💬 Interactive chatbot interface
* ⚡ Fast responses using the Groq API
* 🎨 Simple and responsive frontend
* 🔒 Secure API key management using environment variables
* ☁️ Ready for deployment on Render

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **LLM API:** Groq
* **Deployment:** Render

---

## 📁 Project Structure

```text
groq-chatbot/
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/groq-chatbot.git
cd groq-chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment

This project is configured for deployment on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Add the following environment variable in your Render dashboard:

| Variable       | Description       |
| -------------- | ----------------- |
| `GROQ_API_KEY` | Your Groq API key |

---

## 📸 Demo

<img width="802" height="470" alt="Screenshot 2026-07-05 172418" src="https://github.com/user-attachments/assets/f79284f8-b290-4d25-8a2b-93d217ad08fd" />


Example:

```
assets/demo.png
```

---

## 🔮 Future Improvements

* Chat history
* Conversation memory
* Dark mode
* Streaming responses
* Voice input/output
* File upload (PDF Q&A)
* Retrieval-Augmented Generation (RAG)
* Multi-model support

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Shreya Gaur**

If you found this project useful, consider giving it a ⭐ on GitHub!
