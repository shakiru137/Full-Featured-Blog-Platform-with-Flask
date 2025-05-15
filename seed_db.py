from app import create_app, db
from app.models import User, Post, Comment
from datetime import datetime, timedelta
import random

app = create_app()

def seed_database():
    with app.app_context():
        # Create admin user
        admin = User(
            username='admin',
            email='admin@example.com',
            is_admin=True
        )
        admin.set_password('adminpassword')
        
        # Create regular users
        users = [admin]
        for i in range(1, 5):
            user = User(
                username=f'user{i}',
                email=f'user{i}@example.com',
                is_admin=False
            )
            user.set_password(f'password{i}')
            users.append(user)
        
        db.session.add_all(users)
        db.session.commit()
        
        # Create posts
        posts = []
        for i in range(1, 16):
            user = random.choice(users)
            post = Post(
                title=f'Sample Post {i}',
                body=f'This is the content of sample post {i}. It contains some text to demonstrate how posts are displayed in our blog platform.',
                created_at=datetime.utcnow() - timedelta(days=random.randint(0, 30)),
                author=user
            )
            posts.append(post)
        
        db.session.add_all(posts)
        db.session.commit()
        
        # Create comments
        comments = []
        for post in posts:
            # Add 1-5 comments per post
            for _ in range(random.randint(1, 5)):
                user = random.choice(users)
                comment = Comment(
                    body=f'This is a sample comment on the post "{post.title}".',
                    created_at=datetime.utcnow() - timedelta(days=random.randint(0, 15)),
                    author=user,
                    post=post
                )
                comments.append(comment)
        
        db.session.add_all(comments)
        db.session.commit()
        
        print('Database seeded successfully!')

if __name__ == '__main__':
    seed_database()
