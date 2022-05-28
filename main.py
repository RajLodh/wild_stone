from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def user():
    return "API"

@app.route('/predict')
def home():
    return 'html'

if __name__ == '__main__':
    app.run(debug=True)