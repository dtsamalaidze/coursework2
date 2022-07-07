from flask import Blueprint, render_template
from utils import Posts

post_app = Blueprint('post', __name__, template_folder='templates', static_folder='static')
posts = Posts()


@post_app.route('/<int:uid>')
def post_page(uid):
    post = posts.get_post_by_post_id(uid)
    comments = posts.get_comments_by_post_id(uid)
    return render_template('post/post.html',
                           name=post['poster_name'],
                           post=post['content'],
                           avatar=post['poster_avatar'],
                           pic=post['pic'],
                           views_count=post['views_count'],
                           comments=comments,
                           count_comments=len(comments)
                           )
