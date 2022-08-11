from flask import Blueprint, render_template
from bp_posts.post.DAO.posts import Posts

main_app = Blueprint('main', __name__, template_folder='templates', static_folder='static')
posts = Posts()

@main_app.route('/')
def imdex_page():
    post = posts.get_posts_all()
    return render_template('index.html', posts=post)


