from flask import Blueprint, jsonify, request
from .models import db, Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'))
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@tasks_bp.route('', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@tasks_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task:
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

@tasks_bp.route('/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if task:
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        db.session.commit()
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Task not found'}), 404

@tasks_bp.route('/<int:id>/complete', methods=['PUT'])
def complete_task(id):
    task = Task.query.get(id)
    if task:
        task.completed = True
        db.session.commit()
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

@tasks_bp.route('/<int:id>/incomplete', methods=['PUT'])
def incomplete_task(id):
    task = Task.query.get(id)
    if task:
        task.completed = False
        db.session.commit()
        return jsonify(task.to_dict()), 200
    else:
        return jsonify({'error': 'Task not found'}), 404
