import os
from datetime import datetime
from flask import Flask, request, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET')
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html", datetime = str(datetime.now()))

if __name__ == "__main__":
        app.run()
