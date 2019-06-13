from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("base.html")

@app.route('/info/',methods=['POST'])
def collect_data():
    email=request.form['mail']
    return ("Hello user, your email id is "+email)

if __name__=='__main__':
    app.run(debug=True)