from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
  name = request.form.get('name')
  if name is None:
      return "hello fellow earthling\n", 200
  return f"hello {name}\n", 200

