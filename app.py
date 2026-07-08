from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os

from database import (
    init_db,
    save_message,
    get_messages,
    clear_messages
)

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
secret_key = os.getenv("SECRET_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

app = Flask(__name__)
app.secret_key = secret_key

# -----------------------------
# Initialize Database
# -----------------------------
init_db()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please enter a message."})

    # Save user's message
    save_message("user", user_message)

    # Read previous conversation
    messages = get_messages()

    # Add system prompt if database is empty
    if len(messages) == 1:
        messages.insert(
            0,
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        )

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7
        )

        answer = response.choices[0].message.content

        # Save assistant reply
        save_message("assistant", answer)

        return jsonify({"reply": answer})

    except Exception as e:

        print("Error:", e)

        return jsonify({"reply": str(e)})


@app.route("/clear", methods=["POST"])
def clear():

    clear_messages()

    return jsonify(
        {
            "status": "success"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)