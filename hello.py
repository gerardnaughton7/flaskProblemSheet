# Gerard Naughton G00209309
#webserver 
#import flask
#Origionally adapted from:
# http://flask.pocoo.org/
import flask as fl
app = fl.Flask(__name__)

#return index.html with form
@app.route("/")
def root():
    return app.send_static_file('index.html')

#return the request hello and using get and post method take the name from the form in index.html   
@app.route("/name", methods=["GET", "POST"])
def name():
    return "Hello " + fl.request.form["name"] + "!"

if __name__ == "__main__":
    app.run()