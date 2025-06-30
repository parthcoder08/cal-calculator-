 from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT (update) an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(i)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)