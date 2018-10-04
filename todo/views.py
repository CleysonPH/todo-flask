def configure(app):
    @app.route('/')
    def index():
        return 'Index Page'


    @app.route('/create/')
    def create():
        return 'Create Page'


    @app.route('/<id>/update/')
    def update(id):
        return f'Update page {id}'


    @app.route('/<id>/delete/')
    def delete(id):
        return f'Delete page {id}'
