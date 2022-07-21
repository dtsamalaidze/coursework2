import logging
from flask import Blueprint, render_template
from bp_posts.post.DAO.comment import Comment
from bp_posts.post.DAO.posts import Posts
from exceptions.exceptions import FileNotFound


logging.basicConfig(filename="logs/basic.log", level=logging.INFO)
post_app = Blueprint('post', __name__, template_folder='templates', static_folder='static')
posts = Posts()
comments = Comment()


@post_app.route('/<int:uid>')
def post_page(uid):
    logging.info(f'Открываю станицу с индексом: {uid}', )
    post = posts.get_post_by_post_id(uid)
    comment = comments.get_comments_by_post_id(uid)
    try:
        return render_template('post.html',
                               post=post['content'],
                               avatar=post['poster_avatar'],
                               pic=post['pic'],
                               views_count=post['views_count'],
                               comments=comment,
                               count_comments=len(comment)
                               )
    except TypeError:
        logging.info(f'Не удалось открыть станицу с индексом: {uid}')
        raise FileNotFound(f'Не удалось открыть станицу с индексом: {uid}')




