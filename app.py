from flask import Flask, request, jsonify
from models import Task, db

app = Flask(__name__)

# Create a Task
@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.json.get('title')
    description = request.json.get('description')

    if not title or not description:
        return jsonify({'message': 'Bad Request. Title and description are required.'}), 400

    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201

# Update a Task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'message': 'Task not found.'}), 404

    title = request.json.get('title')
    description = request.json.get('description')
    completed = request.json.get('completed')

    if title:
        task.title = title
    if description:
        task.description = description
    if completed is not None:
        task.completed = completed

    db.session.commit()

    return jsonify(task.to_dict())

# Delete a Task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'message': 'Task not found.'}), 404

    db.session.delete(task)
    db.session.commit()

    return '', 204

# Mark a Task as Complete/Incomplete
@app.route('/tasks/<int:task_id>/completed', methods=['PUT'])
def mark_task_completed(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'message': 'Task not found.'}), 404

    completed = request.json.get('completed')

    if completed is not None:
        task.completed = completed

    db.session.commit()

    return jsonify(task.to_dict())

# Get All Tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()

    return jsonify([task.to_dict() for task in tasks])
