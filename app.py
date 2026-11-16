
from flask import Flask, jsonify
from flask_cors import CORS
from fertilizer_recommendation import fertilizer_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    fertilizer_bp,
    url_prefix="/api/fertilizer"
)

@app.route("/")
def home():
    return jsonify({
        "message": "Fertilizer API is running successfully"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
