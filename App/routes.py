import os
from bson.objectid import ObjectId
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app

main = Blueprint('main',__name__)

@main.route('/')
def index():
    tasks = current_app.db.tasks.find()
    return render_template('index.html', tasks = tasks)

@main.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        current_app.db.tasks.insert_one({'content': task_content, 'completed': False})
        flash('Task added successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/complete_task/<task_id>')
def complete_task(task_id):
    current_app.db.tasks.update_one({'_id': ObjectId(task_id)}, {'$set': {'completed': True}})
    flash('Task marked as completed!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete_task/<task_id>')
def delete_task(task_id):
    current_app.db.tasks.delete_one({'_id': ObjectId(task_id)})
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.index'))

@main.route('/update_task/<task_id>',methods=['GET','POST'])
def update_task(task_id):
    if request.method == 'POST':
        new_conetent = request.form.get('content')
        if new_conetent:
            current_app.db.tasks.update_one({'_id':ObjectId(task_id)},{'$set':{'content' : new_conetent}})
            flash('Task Updated Successfully!','success')
        return redirect(url_for('main.index'))
    task = current_app.db.tasks.find_one({'_id':ObjectId(task_id)})
    return render_template('update.html',task = task)
