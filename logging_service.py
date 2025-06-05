Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, request
... 
... app = Flask(__name__)
... 
... messages = {}
... 
... @app.route("/logging", methods=["POST", "GET"])
... def log_request():
...     if request.method == "POST":
...         _id = request.form['id']
...         _msg = request.form['msg']
...         messages[_id] = _msg
...         print("Received message:", _msg)
...         return "Success"
...     elif request.method == "GET":
...         return messages
...     else:
...         abort(400)
... 
... if __name__ == '__main__':
