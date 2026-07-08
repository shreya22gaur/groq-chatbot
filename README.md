# 🤖 Groq AI Chatbot with Persistent Memory

Live Link : https://groq-chatbot-8zua.onrender.com/

An intelligent AI chatbot built using **Flask**, **Groq API**, and **SQLite** that provides real-time AI conversations with **persistent chat memory**. Unlike a basic chatbot, this application stores conversations in a local SQLite database, allowing chat history to remain available even after refreshing the browser.

---

## 📸 Preview



Example:

<img width="1063" height="627" alt="image" src="https://github.com/user-attachments/assets/e4fe6e14-1ffc-487c-8882-19524c1d4449" />


---

## ✨ Features

- 🤖 AI-powered conversations using the **Groq API**
- 💾 Persistent chat history using **SQLite**
- 🔄 Conversation history remains after page refresh
- 🎨 Modern responsive user interface
- ⚡ Fast AI responses
- 🗑️ Clear chat functionality
- 🌐 Deployable on Render
- 🔐 Environment variable support using `.env`

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask (Python)

### AI Model
- Groq API
- Llama 3.3 70B Versatile

### Database
- SQLite

### Deployment
- Render

---

## 📂 Project Structure

```
groq-chatbot/
│
├── app.py
├── database.py
├── requirements.txt
├── Procfile
├── .gitignore
├── .env
├── chat.db
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

---

### 2. Navigate to the project

```bash
cd YOUR_REPOSITORY
```

---

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create a `.env` file

```
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
```

---

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

This project can be deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Remember to add these environment variables on Render:

- `GROQ_API_KEY`
- `SECRET_KEY`

---

## 🗄️ Database

The chatbot stores conversations in a SQLite database (`chat.db`).

Each message is stored with:

- Role (User/Assistant)
- Message Content

This allows conversations to persist across page refreshes.

---

## 📷 Screenshots

### Home Page

*(Add screenshot here)*

### Chat Interface

*(Add screenshot here)*

---

## 🔮 Future Improvements

- 💬 Multiple chat conversations
- 🌙 Dark mode
- 📝 Markdown rendering
- 💻 Code syntax highlighting
- 📄 PDF upload and chat
- 🔍 Web search integration
- 🎤 Voice input
- 🤖 Agentic AI with tools
- ☁️ PostgreSQL cloud database

---

## 👩‍💻 Author

**Shreya Gaur**

- GitHub: https://github.com/shreya22gaur

---

## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub!
