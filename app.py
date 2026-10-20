import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_COLOR = os.getenv("APP_COLOR", "blue").lower()
APP_VERSION = os.getenv("APP_VERSION", "1.0")

COLORS = {
    "blue": "#1976d2",
    "green": "#198754",
}

@app.route("/")
def home():
    color = APP_COLOR if APP_COLOR in COLORS else "blue"
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Blue-Green Demo</title>
        <style>
            body {{
                background: {COLORS[color]};
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 15vh;
                margin: 0;
                min-height: 85vh;
            }}
            h1 {{ font-size: 3rem; }}
            p {{ font-size: 1.3rem; }}
        </style>
    </head>
    <body>
        <h1>{color.upper()} VERSION</h1>
        <p>Blue-Green Deployment Demo</p>
        <p>Application version: {APP_VERSION}</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "color": APP_COLOR,
        "version": APP_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
