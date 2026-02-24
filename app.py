from flask import Flask, render_template

app= Flask (__name__)

@app.route("/")
def index():
    return "<h1> Seher Sanghani </h1><h2> 2403936 </h2>"

@app.route("/resume")
def resume():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)