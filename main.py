from flask import Flask, request, jsonify
import openai
import os
import requests

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def analyze_sentiment(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "คุณคือโมเดลวิเคราะห์ข่าวการเงินแบบสั้นๆ ตอบกลับแค่คำว่า Bullish, Bearish หรือ Neutral เท่านั้น"},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return {"error": "Missing 'text' field"}, 400

    result = analyze_sentiment(text)
    send_telegram_message(f"🧠 ข้อความ: {text}")
    send_telegram_message(f"📊 วิเคราะห์: {result}")
    return {"result": result}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
