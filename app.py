#Python Program to Return an Simple HTML Page of an Application that has been containerized.
from flask import Flask
import os
import socket

app= Flask(__name__)

@app.route("/")
def hello():
    html = "<h1 style='text-align:center;margin:20px;'>Hello World!!</h1>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)