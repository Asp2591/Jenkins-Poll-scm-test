from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1>Hello Guyssss !! Atharva Here</h2>'
@app.route('/about')
def about():
    return '<h1>Hello Guyssss !! Atharva Patkar Here</h2>'


if __name__=="__main__":
    app.run("0.0.0.0",port=8181)
