# Kifrom flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "TELEGRAM_BOT_TOKEN"  # o'z tokeningni shu yerga qo'y

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            # Foydalanuvchiga javob
            payload = {"chat_id": chat_id, "text": f"Siz yozdingiz: {text}"}
            requests.post(URL, json=payload)
    return "Bot ishlayapti!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)nobote
