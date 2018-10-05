from datetime import datetime
from flask import render_template, redirect, request, current_app, url_for, flash


def configure(app):
    @app.route('/')
    def index():
        todos = current_app.db.todos.find()

        return render_template('index.html', todos=todos)


    @app.route('/create/', methods=('GET', 'POST'))
    def create():
        if request.method == 'GET':
            return render_template('create.html')

        error = None

        title = request.form['title']
        
        delivery_date = request.form['delivery']
        try:
            delivery_date = datetime.strptime(delivery_date, '%d/%m/%Y').date()

            if delivery_date <= datetime.now().date():
                error = 'A data de entrga não pode ser menor que a data atual'
        except:
            error = 'A data de entrega está invalida!'
        
        if error is not None:
            flash(error)
            return redirect(url_for('create'))
        
        description = request.form['description']

        current_app.db.todos.insert_one({'title': title,'delivery_date': delivery_date.strftime('%d/%m/%Y'), 'description': description})

        return redirect(url_for('index'))


    @app.route('/<id>/update/', methods=('GET', 'POST'))
    def update(id):
        todo = current_app.db.todos.find_one({'_id': id})

        if request.method == 'GET':
            return render_template('update.html', todo=todo)

        title = request.form['title']
        description = request.form['description']

        current_app.db.todos.update_one({'_id': todo['_id']}, {'$set': {'title': title, 'description': description}})

        return redirect(url_for('index'))


    @app.route('/<id>/delete/')
    def delete(id):
        current_app.db.todos.delete_one({'_id': id})

        return redirect(url_for('index'))
