from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


from datetime import datetime

x = datetime.now().min == 5
