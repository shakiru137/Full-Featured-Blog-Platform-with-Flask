from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from app import db
from app.admin import bp
from app.models import User, Post, Comment

@bp.before_request
def restrict_to_admins():
    if not current_user.is_authenticated or not current_user.is_admin:
        abort(403)

@bp.route('/')
@bp.route('/dashboard')
def dashboard():
    users_count = User.query.count()
    posts_count = Post.query.count()
    comments_count = Comment.query.count()
    return render_template('admin/dashboard.html', title='Admin Dashboard',
                           users_count=users_count, posts_count=posts_count, comments_count=comments_count)

@bp.route('/users')
def users():
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('admin/users.html', title='Manage Users', users=users)

@bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user == current_user:
        flash('You cannot delete yourself!', 'danger')
    else:
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted!', 'success')
    return redirect(url_for('admin.users'))

@bp.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('admin/posts.html', title='Manage Posts', posts=posts)

@bp.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success')
    return redirect(url_for('admin.posts'))

@bp.route('/comments')
def comments():
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.order_by(Comment.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('admin/comments.html', title='Manage Comments', comments=comments)

@bp.route('/comments/<int:comment_id>/delete', methods=['POST'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted!', 'success')
    return redirect(url_for('admin.comments'))
