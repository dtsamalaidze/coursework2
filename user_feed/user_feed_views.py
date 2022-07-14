from flask import Blueprint, render_template

from post.post_views import posts
from utils import Posts

user_feed_app = Blueprint('user_feed', __name__, template_folder='templates', static_folder='static')
posts = Posts()

@user_feed_app.route('/<username>')
def user_feed_page(username):
    post = posts.get_post_by_user(str(username))
    return render_template('index.html', posts=post)
