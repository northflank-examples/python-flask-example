from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/<data>")
def api(data):
    return jsonify({"message": "Successfully received client request for "+data+"."})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
