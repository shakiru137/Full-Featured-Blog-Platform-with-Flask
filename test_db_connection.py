from app import create_app, db
from app.models import User, Post, Comment

app = create_app()

def test_connection():
    with app.app_context():
        try:
            # Try to query the database
            users_count = User.query.count()
            posts_count = Post.query.count()
            comments_count = Comment.query.count()
            
            print(f"Connection successful!")
            print(f"Users: {users_count}")
            print(f"Posts: {posts_count}")
            print(f"Comments: {comments_count}")
            
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

if __name__ == '__main__':
    test_connection()
