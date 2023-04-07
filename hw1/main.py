from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("file.html", url='https://lookw.ru/8/828/1476173423-125.jpg')

if __name__ == '__main__':
   app.run(host='0.0.0.0')