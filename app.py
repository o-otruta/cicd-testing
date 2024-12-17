from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# API: Отримання списку користувачів
@app.route("/api/users", methods=["GET"])
def get_users():
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
    ]
    return jsonify(users)

# API: Додавання нового користувача
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = {
        "id": 3,
        "name": data.get("name"),
        "email": data.get("email"),
    }
    return jsonify(new_user), 201

# HTML-сторінка для тестування Selenium
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
