from flask import Blueprint, render_template

from post.post_views import posts

main_app = Blueprint('main', __name__, template_folder='templates', static_folder='static')


@main_app.route('/')
def imdex_page():
    post = posts.get_posts_all()
    return render_template('index.html', posts=post)
