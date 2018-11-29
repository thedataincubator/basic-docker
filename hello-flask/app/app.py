from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_age():
  name = request.form.get('name')
  if name is None:
      return "hello fellow earthling", 200
  return f"hello {name}", 200

