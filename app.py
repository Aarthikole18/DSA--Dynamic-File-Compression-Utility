from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import os
import pandas as pd

from src.compress import compress_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/compress",
    methods=["POST"]
)
def compress():

    file = request.files["file"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    result = compress_file(
        filepath
    )

    return render_template(
        "result.html",
        result=result
    )


@app.route("/dashboard")
def dashboard():

    history_file = (
        "outputs/compression_history.csv"
    )

    data = []

    if os.path.exists(
        history_file
    ):

        df = pd.read_csv(
            history_file
        )

        data = df.to_dict(
            orient="records"
        )

    return render_template(
        "dashboard.html",
        data=data
    )


@app.route("/history")
def history():

    history_file = (
        "outputs/compression_history.csv"
    )

    data = []

    if os.path.exists(
        history_file
    ):

        df = pd.read_csv(
            history_file
        )

        data = df.to_dict(
            orient="records"
        )

    return render_template(
        "history.html",
        data=data
    )

@app.route("/stats")
def stats():

    history_file = "outputs/compression_history.csv"

    stats = {
        "operations": 0,
        "avg_ratio": 0,
        "total_saved": 0
    }

    if os.path.exists(history_file):

        df = pd.read_csv(history_file)

        if len(df) > 0:

            stats = {
                "operations": len(df),
                "avg_ratio": round(df["ratio"].mean(), 2),
                "total_saved": int(df["saved_bytes"].sum())
            }

    return render_template(
        "stats.html",
        stats=stats
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )