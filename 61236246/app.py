from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # (use random bytes)

def get_progress():
    DEFAULT_PROGRESS_VALUE = 0
    DEFAULT_PROGRESS_MAX = 100
    return {
        "value": session.get("progress_value", DEFAULT_PROGRESS_VALUE),
        "max": session.get("progress_max", DEFAULT_PROGRESS_MAX),
    }

def set_progress_value(val):
    if val is not None:
        session["progress_value"] = int(val)

def set_progress_max(val):
    if val is not None:
        session["progress_max"] = int(val)

@app.route("/")
def root():
    return render_template("index.html", **get_progress())

@app.route("/progress", methods=["GET", "POST"])
def progress():
    if request.method == "POST":
        set_progress_value(request.form.get("value"))
        set_progress_max(request.form.get("max"))
    return get_progress()
