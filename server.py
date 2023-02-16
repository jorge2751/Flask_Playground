from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/play')
def play():
    return render_template("play.html", times=3)

@app.route('/play/<int:times>')
def play_times(times):
    return render_template("play.html", times=times)

@app.route('/play/<int:times>/<string:color>')
def play_times_color(times, color):
    return render_template("play.html", times=times, color=color)

if __name__=="__main__":
    app.run(debug=True, port=5000)