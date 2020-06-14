from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Website Homepage"

@app.route('/about/')
def home():
    return "website content served here"

if __name__=='__main__':
    app.run(debug=True)