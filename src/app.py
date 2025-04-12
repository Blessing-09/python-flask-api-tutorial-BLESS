from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {
        "label": "My first API task",
        "done": False
    },
    {
        "label": "My second task", 
        "done": False
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['GET'])
def get_todo(position):
    if 0 < position <= len(todos):
        return jsonify(todos[position - 1])
    return jsonify({"message": "Invalid position"}), 404

@app.route('/todos', methods=['POST'])
def add_new_todo():
    add_task = request.get_json()
    todo = {
        "label": add_task['label'],
        "done": False
        }
    todos.append(todo)
    return jsonify(todo)

@app.route('/todos/<int:position>', methods=['PUT'])
def update_todo(position):
    if 0 < position <= len(todos):
        update_request = request.get_json()
        requested_position = position - 1
        todos[requested_position]['label'] = update_request['label']
        return jsonify(todos[requested_position])
    else:
        return jsonify({"error": "Invalid position"}), 400


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 < position <= len(todos):
        deleted = todos.pop(position - 1)
        return jsonify ({"message": "Todo deleted", "todo": deleted})
    return jsonify({"message": "Todo not found"}),400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)