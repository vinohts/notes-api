from flask import Flask, jsonify, request

app = Flask(__name__)
notes = []

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Notes API!"})

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json() or {}
    text = data.get("text")
    if not text:
        return jsonify({"error": "text field is required"}), 400
    note = {"id": len(notes) + 1, "text": text}
    notes.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
