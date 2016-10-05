from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/name/<name>")
def name(name):
    return "Your name is %s" % name

if __name__ == "__main__":
    app.run()