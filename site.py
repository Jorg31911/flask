from flask import Flask

app = Flask(__name__)


@app.route("/")
def principal():
    return "<h1> Hola mundo 2 </h1>"


if __name__ == '__main__':
    app.run()
