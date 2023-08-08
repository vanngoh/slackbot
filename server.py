from flask import Flask
from threading import Thread

app = Flask("")

@app.route('/')
def home():
  return {"hello": "world"}

def run():
  app.run(host='0.0.0.0',port=8888)

def run_background():
  t = Thread(target=run)
  t.start()