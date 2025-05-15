from app import create_app, db
from app.models import User, Post, Comment

app = create_app()

with app.app_context():
    db.create_all()  # This creates all the tables in the database

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
