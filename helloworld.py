from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Guys !! Atharva Here</h2>'

if __name__=="__main__":
    app.run("0.0.0.0",port=7070)
