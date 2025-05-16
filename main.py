from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

messages = []

@app.route("/" , methods = ['GET'])
def index():
    return render_template("index.html", msgs=messages)
@app.route('/api/msg', methods=['POST'])
def receive():
     data = request.get_json(force=True) 
     text = data.get('text', '')
     messages.append(text)
     return {'status': 'ok'}, 200
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)