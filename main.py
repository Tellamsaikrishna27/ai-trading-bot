from flask import Flask
import threading
import time
app = Flask(name)
@app.route('/')
def home():
    return "AI Trading Bot Running"
def bot_loop():
    while True:
        print("Bot Running...")
        time.sleep(60)
threading.Thread(target=bot_loop).start()
if name == "main":
import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
