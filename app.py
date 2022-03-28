from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    title = "Welcome to conference page"
    return render_template('base.html',title=title)

if __name__=='__main__':
    app.run(debug=True)