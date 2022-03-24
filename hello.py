from pickle import APPEND
from flask import Flask

@APPEND.route('/')
def index():
    return {
        "msg": "success",
        "data": "welcome to use flask."
    }

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# debug=True