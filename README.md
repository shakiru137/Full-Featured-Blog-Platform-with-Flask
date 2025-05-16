# Full-Featured Blog Platform with Flask, PostgreSQL, and Docker

## Project Description

This project implements a full-featured blog platform using the Flask web framework, a PostgreSQL database, and Docker containerization. It includes user authentication, post management, comment functionality, an admin dashboard, and pagination.

## Features

- **User Authentication:**
  - Register, login, and logout functionality.
  - Secure password hashing.
  - Session management using Flask-Login.
- **Post Management:**
  - Users can create, edit, and delete posts.
  - Posts include a title, body, and timestamp.
  - Posts are displayed in reverse chronological order.
- **Comment Functionality:**
  - Authenticated users can comment on posts.
  - Comments are tied to specific posts and users.
  - Admins can delete any comment.
- **Admin Dashboard:**
  - Admin users can log in to a dedicated dashboard.
  - The dashboard provides an overview of all posts, comments, and users.
  - Admins can manage (view/delete) posts, comments, and users.
- **Database:**
  - PostgreSQL database for data storage.
  - SQLAlchemy models for User, Post, and Comment.
- **Containerization:**
  - Docker and Docker Compose for containerizing the application.
  - Separate services for Flask and PostgreSQL.
- **Installation Script:**
  - A Bash script (`setup.sh`) automates the setup process.
  - Checks for the following dependencies:
    - Docker
    - Python
    - pip
    - PostgreSQL
    - Required Python packages (defined in `requirements.txt`)
  - Prevents common errors by ensuring all dependencies are met.
- **Pagination:**
  - Post listings are paginated (5 posts per page).
  - User profile pages display the user's posts and comments with pagination.

## Technical Details

- **Framework:** Flask (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** Flask-Login
- **Password Hashing:** (Handled by Flask-Login)
- **Containerization:** Docker and Docker Compose
- **Scripting:** Bash

## Project Structure

The project structure is organized as follows:

├── app/│ ├── **init**.py│ ├── models.py # SQLAlchemy models for User, Post, Comment│ ├── routes.py # Flask routes for the application│ ├── forms.py # Flask forms for user input validation│ ├── templates/ # HTML templates│ │ ├── base.html│ │ ├── index.html│ │ ├── login.html│ │ ├── register.html│ │ ├── post.html│ │ ├── user.html│ │ ├── admin/ # Admin dashboard templates│ │ │ ├── dashboard.html│ │ │ ├── users.html│ │ │ ├── posts.html│ │ │ ├── comments.html│ ├── static/ # Static files (CSS, JavaScript)├── migrations/ # Alembic database migration scripts (if applicable)├── requirements.txt # Python dependencies├── config.py # Configuration settings├── docker-compose.yml # Docker Compose configuration├── Dockerfile # Dockerfile for the Flask application├── setup.sh # Bash script for setup and dependency check├── README.md # Project documentation (this file)

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Run the Setup Script:**

    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

    - This script will check for the required dependencies (Docker, Python, pip, PostgreSQL) and install the necessary Python packages. It will also create the database and run migrations.

3.  **Configure Environment Variables:**

    - Create a `.env` file in the project root.
    - Add the following variables, adjusting the values as necessary:
      ```
      SECRET_KEY=<your_secret_key> # Generate a random, secure key
      DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database_name>
      # Example:  DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/blogdb
      ```
      - **SECRET_KEY:** A secret key for Flask. Generate a long, random string.
      - **DATABASE_URL:** The connection string for your PostgreSQL database. Make sure the user, password, host, port, and database name are correct. If you're using Docker Compose (as provided), the database service name (`db`) will be resolvable within the Docker network.

4.  **Run with Docker Compose (Recommended):**

    ```bash
    docker-compose up -d
    ```

    - This will start the Flask application and the PostgreSQL database in separate containers. The `-d` flag runs them in detached mode (in the background).

5.  **Access the Application:**

    - Once the containers are running, the application will be accessible at `http://localhost:5000` (or the port you configured in your Flask application).

## Database Setup (If Not Using Docker Compose)

If you are not using Docker Compose, you need to set up your PostgreSQL database manually:

1.  **Install PostgreSQL:** Install PostgreSQL on your system if you haven't already.
2.  **Create a Database:** Create a new PostgreSQL database for the application.
3.  **Create a User and Grant Privileges (Optional):** It's recommended to create a dedicated PostgreSQL user for the application and grant it the necessary privileges on the database.
4.  **Set the `DATABASE_URL`:** Make sure the `DATABASE_URL` in your `.env` file is correctly set to point to your PostgreSQL database.
5.  **Run Migrations:**
    ```bash
    flask db upgrade
    ```
    - This will create the database tables as defined in your SQLAlchemy models. (You might need to install `flask-migrate`: `pip install flask-migrate`)

## Seeding the Database

To populate the database with initial data (e.g., an admin user), you can use the following (adjust as needed):

1.  **Run the Flask Shell:**
    ```bash
    flask shell
    ```
2.  **Import the models and create data:**

    ```python
    from app.models import User, Post, Comment
    from app import db
    from werkzeug.security import generate_password_hash

    # Create an admin user
    admin = User(username='admin', email='admin@example.com', password_hash=generate_password_hash('adminpass'), is_admin=True)
    db.session.add(admin)

    # Create some sample users
    user1 = User(username='johndoe', email='john@example.com', password_hash=generate_password_hash('userpass'))
    user2 = User(username='janedoe', email='jane@example.com', password_hash=generate_password_hash('userpass'))
    db.session.add(user1)
    db.session.add(user2)

    # Create some sample posts
    post1 = Post(title='Welcome to the Blog', body='This is the first post!', user=admin)
    post2 = Post(title='Another Post', body='This is another interesting post.', user=user1)
    db.session.add(post1)
    db.session.add(post2)

    # Create some sample comments
    comment1 = Comment(body='This is a great post!', user=user2, post=post1)
    comment2 = Comment(body='I agree!', user=user1, post=post1)
    db.session.add(comment1)
    db.session.add(comment2)

    db.session.commit()
    print("Database seeded!")
    ```

    - This is example code. You can adapt it to create different users, posts, and comments. **Important:** Use `generate_password_hash` as shown to securely hash passwords.

## Accessing the Application

- **Web Interface:** Open your web browser and go to `http://localhost:5000` (or the appropriate URL if you've configured a different port or domain).
- **Admin Interface:** The admin interface is accessible through the standard login, but only users with `is_admin` set to `True` in the database will be able to access the admin-specific views.
