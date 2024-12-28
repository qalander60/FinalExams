from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#Main function
if __name__ == "__main__":
    app.run(debug=True,port=80)