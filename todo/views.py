from flask import render_template, redirect, request, current_app, url_for


def configure(app):
    @app.route('/')
    def index():
        todos = current_app.db.todos.find()

        return render_template('index.html', todos=todos)


    @app.route('/create/', methods=('GET', 'POST'))
    def create():
        if request.method == 'GET':
            return render_template('create.html')

        title = request.form['title']
        description = request.form['description']

        current_app.db.todos.insert_one({'title': title, 'description': description})

        return redirect(url_for('index'))


    @app.route('/<id>/update/')
    def update(id):
        return f'Update page {id}'


    @app.route('/<id>/delete/')
    def delete(id):
        return f'Delete page {id}'
